from properties import Properties
import json


class VM:

    def __init__(self, connection, vname):
        props = Properties()
        props.gather_virtual_information(connection, vname)
        self.name = props.get_vhostname()
        self.status = props.get_vstatus()
        self.disks = props.get_vdisks()
        self.memory = props.get_vmemory_usage()
        self.cpu = props.get_vcpu()

    def __str__(self):
        return json.dumps( self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    
