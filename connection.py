import wmi

class Connection:

    def __init__(self, server, user, password):
        self.physical_connection = None
        self.virtual_connection = None
        self.server = server
        self.user = user
        self.password = password

    def register_physical(self):
        connection = wmi.connect_server (
            server = self.server ,
            user = self.user,
            password = self.password
        )
        self.physical_connection = wmi.WMI(wmi=connection)


    def register_virtual(self):
        connection = wmi.connect_server (
            server = self.server ,
            user = self.user,
            password = self.password,
            namespace = "root\\virtualization\\v2"
        )
        self.virtual_connection = wmi.WMI(wmi=connection)



