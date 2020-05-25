import json

class Resources:

    def __init__(self, server, owner, dt_string):
        self.server = server
        self.discoverd = dt_string
        self.owner = owner
        self.physical_properties = None
        self.virtual_properties = None

    def get_physical_properties(self):
        return self.physical_properties.__dict__


    def get_virtual_properties(self):
        return self.virtual_properties.__dict__


    def get_vms(self):
        return self.vms


    def __str__(self):
        return json.dumps( self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        