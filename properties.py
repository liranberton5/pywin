import json, re, xmltodict, pprint
from connection import Connection

class Properties:

    def __init__(self):
        self.cpu = None
        self.disks = None
        self.memory = None
        self.hostname = None
        self.vcpu = None
        self.vdisks = None
        self.vmemory = None
        self.vhostname = None
        self.vstatus = None


    def gather_physical_information(self, connection):
        # Every new info (method) we need should be registered here first
        try:
            self.eval_disks_usage(connection)
            self.eval_hostname(connection)
            self.eval_memory_usage(connection)
            self.eval_cpu_usage(connection)
        except Exception as e:
            print("Something went wrong with gathering physical information.")
            print("Skipping")
            print(e)


    def gather_virtual_information(self, connection, vname):
        # Every new info (method) we need should be registered here first
        try:
            self.eval_vhostname(connection, vname["element_name"])
            self.eval_vstatus(connection, vname["element_name"])
            if self.vstatus == "running":
                self.eval_vdisks_usage(connection, vname["element_name"])
                self.eval_vmemory_usage(connection, vname["element_name"])
                self.eval_vcpu_usage(connection, vname["name"])
        except Exception as e:
            print("Something went wrong with gathering virtual information.")
            print("Skipping")
            print(e)


    def eval_vcpu_usage(self, client, name):
        i = 0
        threshold = 95
        self.vcpu = {"description": "Precent free below threshold", "load": [], "alarm" : "No Alerts", "alarm_msgs": [], "threshold": threshold}
        cpus = client.Msvm_Processor(SystemName=name)
        for cpu in cpus:
            self.vcpu["load"].append({"core":i, "idle":str(100 - int(cpu.LoadPercentage)), "used": int(cpu.LoadPercentage)})
            if 100 - int(cpu.LoadPercentage) < threshold:
                self.vcpu["alarm"] = "Alerts Found"
                self.vcpu["alarm_msgs"].append("cpu usage on core " + cpu.Name + " more then allowed threshold (" + str(threshold) + ")")
            i+=1

    def eval_vdisks_usage(self, client, name):
        threshold = 10
        self.vdisks = {"usage": [], "description": "Precent free below threshold", "alarm": "No Alerts", "alarm_msgs": [], "threshold": threshold}    

        disks_paths = []
        for disk in client.Msvm_StorageAllocationSettingData(Caption = "Hard Disk Image"):
            disks_paths.append(''.join(disk.HostResource))

        image = client.Msvm_ImageManagementService()[0]
        for path in disks_paths:
            if self.vhostname["element_name"] in path:
                disk_state = image.GetVirtualHardDiskState(path)
                xml = disk_state[-1]
                j = json.dumps(xmltodict.parse(xml), indent=4)
                j = json.loads(j)
                for prop in j["INSTANCE"]["PROPERTY"]:
                    if "FileSize" in prop["@NAME"]:
                        used_size = round(int(prop["VALUE"]) / 1024 / 1024 / 1024)
                        
                    if "MinInternalSize" in prop["@NAME"]:
                        total_size = round(int(prop["VALUE"]) / 1024 / 1024 /1024)
                        free_size = total_size - used_size
                        p_used = round(100 *(used_size / total_size))
                        p_free = round(100 *(free_size / total_size))
                self.vdisks["usage"].append({"name": path ,"total_size": str(total_size), "used": str(used_size), "p_used": str(p_used), "p_free": str(p_free), "free": free_size, "threshold": threshold})
                if p_free < threshold:
                    self.vdisks["alarm"] = "Alerts Found"
                    self.vdisks["alarm_msgs"].append("disks capacity on  " + path + " below threshold (" + str(threshold) + ")")

        
    def eval_vstatus(self, client, name):
        status = {
            0: "unknown",
            1: "other",
            2: "running",
            3: "off",
            4: "shutting down",
            5: "not applicable",
            6: "enabled and offline",
            7: "test",
            8: "deferred",
            9: "quiesce",
            10: "starting"
        }
        self.vstatus = status[client.Msvm_SummaryInformation(ElementName=name)[0].EnabledState]


    def eval_vhostname(self, client, name):
        self.vhostname = {"name": client.Msvm_SummaryInformation(ElementName=name)[0].name, "element_name": client.Msvm_SummaryInformation(ElementName=name)[0].ElementName}


    def eval_vmemory_usage(self, client, name):
        threshold = 10
        alarm = "No Alerts"
        alarm_msgs = []
        total = str(round(int(client.Msvm_SummaryInformation(ElementName=name)[0].MemoryUsage) / 1024))
        p_free = str(client.Msvm_SummaryInformation(ElementName=name)[0].MemoryAvailable)
        p_used = 100 - int(p_free)
        free = round(int(total) * ( int(p_free) / 100))
        used = int(total) - free
        if int(p_free) > 99:
            p_free = None
            
        self.vmemory = {"total": str(total), "p_free": str(p_free),"free": str(free), "used": str(used), "description": "Precent free below threshold", "alarm": str(alarm), "alarm_msgs": str(alarm_msgs), "threshold": str(threshold)}
        if int(p_free) < threshold:
            alarm = "Alerts Found"
            alarm_msgs.append("memory usage free precent below threshold (" + str(threshold) + ")")
        

    def eval_cpu_usage(self, client):
        threshold = 95
        self.cpu = {"description": "CPU % idle time", "load": [], "alarm" : "No Alerts", "alarm_msgs": [], "threshold": threshold}
        cpus = client.Win32_PerfFormattedData_PerfOS_Processor()
        for cpu in cpus:
            self.cpu["load"].append({"core":cpu.Name, "idle":cpu.PercentIdleTime, "used": 100-int(cpu.PercentIdleTime)})
            if int(cpu.PercentIdleTime) < threshold:
                self.cpu["alarm"] = "Alerts Found"
                self.cpu["alarm_msgs"].append("cpu usage on core " + cpu.Name + " more then allowed threshold (" + str(threshold) + ")")


    def get_cpu_usage(self):
        return self.cpu


    def eval_memory_usage(self, client):
        threshold = 10
        alarm = "No Alerts"
        alarm_msgs = []
        mem = client.Win32_OperatingSystem()[0]
        total = round(int(mem.TotalVisibleMemorySize) / 1024 / 1024)
        free = round(int(mem.FreePhysicalMemory) / 1024 / 1024)
        used = total - free
        p_free = round(100 *(free / total))
        if p_free < threshold:
            alarm = "Alerts Found"
            alarm_msgs.append("memory usage free precent below threshold (" + str(threshold) + ")")
        self.memory = {"total": total, "p_free": p_free,"free": free, "used": used, "description": "Precent free below threshold", "alarm": alarm, "alarm_msgs": alarm_msgs, "threshold": threshold}


    def eval_disks_usage(self, client):
        try:
            threshold = 20
            self.disks = {"usage": [], "description": "Precent free below threshold", "alarm": "No Alerts", "alarm_msgs": [], "threshold": threshold}
            for disk in client.Win32_LogicalDisk (DriveType=3):
                free = round(int(disk.FreeSpace) / 1024 / 1024 / 1024)
                total = round(int(disk.Size) / 1024 / 1024 / 1024)
                used = total - free
                p_free = round(100 *(free / total))
                p_used = round(100 *(used / total))
                self.disks["usage"].append({"name": disk.Caption ,"p_used": str(p_used), "p_free": str(p_free), "free": str(free), "total_size": str(total), "used": str(used)})
                if p_free < threshold:
                    self.disks["alarm"] = "Alerts Found"
                    self.disks["alarm_msgs"].append("disks capacity on  " + disk.Caption + " below threshold (" + str(threshold) + ")")
        except Exception as e:
            print(e)
            

    def eval_hostname(self, client):
        try:
            self.hostname = client.Win32_ComputerSystem()[0].name
        except:
            pass


    def define_vms(self, client):
        try:
            vms = client.Msvm_ComputerSystem()      
            self.vms = []
            for vm in vms:
                if "Virtual" in vm.Caption:
                    self.vms.append({"element_name": vm.ElementName, "name": vm.Name})
        except:
            pass
    

    def get_hostname(self):
        return self.hostname


    def get_disks(self):
        return self.disks


    def get_vms(self):
        return self.vms


    def get_memory_usage(self):
        return self.memory


    def get_vhostname(self):
        return self.vhostname


    def get_vdisks(self):
        return self.vdisks


    def get_vcpu(self):
        return self.vcpu


    def get_vmemory_usage(self):
        return self.vmemory

    def get_vstatus(self):
        return self.vstatus


    def __str__(self):
        #return str(self.__dict__)
        return json.dumps(self.__dict__, indent=2, separators=(',', ': '))

#server = "lirandev-01.middleeast.corp.microsoft.com"
#user = "liberton"
#password = "IAMdevopshere!1"
#
#conn = Connection(server, user, password)
#
#p = Properties(conn.physical_connection)
#print (p)