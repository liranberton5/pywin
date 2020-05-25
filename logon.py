import re
import win32api
import win32evtlog
from win32evtlogutil import SafeFormatMessage

class Logon:
    
    def __init__(self, server, eventid, log_type = "Security"):
        self.server = server
        self.log_type = log_type
        self.flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        #self.flags = win32evtlog.EVENTLOG_BACKWARDS_READ| win32evtlog.EVENTLOG_SEQUENTIAL_READ
        self.logged_users = []
        self.eventid = eventid
        self.log_handle = win32evtlog.OpenEventLog(self.server, self.log_type)

    def read_log_and_extract_event(self):
        events = 1
        while events:
            try:
                events = win32evtlog.ReadEventLog(self.log_handle, self.flags,0)
            except Exception as e:
                print(e)
                raise Exception("Error reading events")
            
            for e in events:
                flag = None
                if e.EventID == self.eventid:
                    data = e.StringInserts
                    if data:
                        current_user = data[5]
                        domain = data[6]
                        logontype = data[8]
                    else: 
                        continue
                    
                    if logontype != "3":
                        continue

                    if domain == "NT AUTHORITY":
                        continue

                    if "$" in current_user:
                        continue

                    for user in self.logged_users:
                        if current_user in user["name"]:
                            user["amount_logins"] += 1 
                            user["last_login"] = str(e.TimeGenerated)
                            flag = True
                            break
                    
                    if not flag:
                        self.logged_users.append({"name": current_user, "last_login": str(e.TimeGenerated), "amount_logins": 1, "domain": domain})

        
    def close_log(self):
        win32evtlog.CloseEventLog(self.log_handle)

    def get_logged_users(self):
        if self.logged_users:
            return self.logged_users
        else:
            self.read_log_and_extract_event() 
            return self.logged_users



#try: # Usage:
#    logon = Logon("lirandev-01.middleeast.corp.microsoft.com", 4624)
#    #logon.read_log()
#    print(logon.get_logged_users())
#finally:
#    logon.close_log()