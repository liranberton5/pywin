from properties import Properties
import json
from vm import VM

class VirtualProperties:

    def __init__(self, connection):
        props = Properties()
        props.define_vms(connection)
        self.vms_list = props.get_vms()
        self.vms_props = []
        if self.vms_list:
            self.virtualization = "enabled"
        else:
            self.virtualization = "disabled"
    
    def get_vms(self):
        return self.vms_list

    def register_vm(self, vm):
        self.vms_props.append(vm)

    def get_vms_props(self):
        return self.vms_props

    def __str__(self):
        if isinstance(self, VM):
            print("instance of VM")
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

        if isinstance(self, VirtualProperties):
            print("instance of VirtualProperties")
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
