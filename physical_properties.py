from properties import Properties
from logon import Logon

class PhysicalProperties:

    def __init__(self, connection, get_login = False):
        # Every new property should be defind here with the corresponding method of Properties.properties.gather_physical_information
        prop = Properties()
        prop.gather_physical_information(connection)
        self.hostname = prop.get_hostname()
        self.disks = prop.get_disks()
        self.cpu = prop.get_cpu_usage()
        self.memory = prop.get_memory_usage()
        self.virtualization = None
        login = Logon(self.hostname, 4624)
        try:
            if get_login:
                self.login_info = {"most_login": None, "login_info": login.get_logged_users()}
                login.close_log()
                most_login = {"amount_logins": 0, "name": "None", "last_login": None}
                for user in self.login_info["login_info"]:
                    if user["name"] == "liberton":
                        continue
                    if int(user["amount_logins"]) > int(most_login["amount_logins"]):
                        most_login = user
                self.login_info["most_login"] = most_login
        except Exception as e:
            print(e)
            self.login_info = None

    def get_hostname(self):
        return self.hostname

    def get_disks(self):
        return self.disks

    def get_cpu(self):
        return self.cpu

    def get_memory(self):
        return self.memory

    def get_login_info(self):
        return self.login_info