from connection import Connection
from resources import Resources
from virtual_properties import VirtualProperties
from physical_properties import PhysicalProperties
from vm import VM
import json
from tools.pmongo import Mongo
import time, threading, pythoncom
from datetime import datetime

#server = "lirandev-01.middleeast.corp.microsoft.com"

def info(user, password, machine, mongo, dt_string):
    server= machine["name"]
    owner = machine["owner"]
    print("working on server " + server)
    
    resource = Resources(server, owner, dt_string)
    conn = Connection(server, user, password)
    try:
        pythoncom.CoInitialize()
        conn.register_physical()
    except Exception as e:
        print("connection issues with physical namespace " + server)
        print(e)
        mongo.update("systems", {"server": server}, json.loads(str(resource)))
        return

    resource.physical_properties = PhysicalProperties(conn.physical_connection, get_login=True)
    print("got physical info of " + server)
    
    try: 
        conn.register_virtual()
        resource.virtual_properties = VirtualProperties(conn.virtual_connection)
        for vm in resource.virtual_properties.vms_list:
            v = VM(conn.virtual_connection, vm)
            resource.virtual_properties.register_vm(v)     
        print("got virtual info of " + server)   
        resource.physical_properties.virtualization =  resource.virtual_properties.virtualization
    except Exception as e:
        resource.physical_properties.virtualization = "disabled"
        print("Did not find virtual namespace on " + server)
        print(e)
    #print(resource)
    mongo.update("systems", {"server": server}, json.loads(str(resource)))


if __name__ == "__main__":
    user = "liberton"
    password = "IAMdevopshere!1"

    s = time.perf_counter()
    resources = []
    mongo = Mongo()
    servers_list = mongo.get_docs("machines")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    threads = {}
    total_machines=0
    for machine in servers_list:
        total_machines+=1
        threads[machine["name"]] = threading.Thread(target=info, args=(user, password, machine, mongo, dt_string,))
        threads[machine["name"]].start()

    for key, val in threads.items():
        threads[key].join()    
    

    elapsed = time.perf_counter() - s
    mongo.insert_docs("program", [{"exec_discovery": dt_string, "exec_time": elapsed, "discover_machines": str(total_machines)}])
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
