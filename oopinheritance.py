class Server:
    def __init__(self,name,ip):
        self.name = name
        self.ip = ip
    def show_info(self):
        print(f"name: {self.name}")
        print(f"ip: {self.ip}")

class Securityserver(Server):
    def __init__(self,name,ip,firewall_status):
        super() .__init__(name,ip)
        self.firewall_status = firewall_status
    def show_info(self):
        super() .show_info()
        print(f"firewall_status: {self.firewall_status}")
web =  Securityserver("my security server","198.163.1.1", "active")
web.show_info()
