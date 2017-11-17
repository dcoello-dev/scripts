import nmap 
import netifaces as ni


class NmapExpert:

    def __init__(self):
        self.ifaces = ni.interfaces()

    def filter_hosts(self, arr):
        toret = []
        for host, status, vendor, mac in arr:
            if status == "up":
                hs = dict(host=host)
                if "mac" in mac.keys():
                    hs["mac"] = mac["mac"]
                    if hs["mac"] in vendor.keys():
                        hs["vendor"] = vendor[hs["mac"]]
                    else:
                        hs["vendor"] = "unknown"
                else:
                    hs["mac"] = "unknown"
                    hs["vendor"] = "unknown"
            toret.append(hs)
        return toret

    def get_hash_hosts(self, ifaces=None):
        if ifaces is None:
            ifaces = self.get_nets()
        for iface in ifaces.keys():
            nm = nmap.PortScanner()
            nm.scan(hosts=ifaces[iface],
                    arguments='-n -sP -PE -PA21,23,80,3389,22,445,135,139')
            hosts_list = [(x,
                           nm[x]['status']['state'],
                           nm[x]['vendor'],
                           nm[x]['addresses']) for x in nm.all_hosts()]

            hash_hosts = self.filter_hosts(hosts_list)

        return hash_hosts

    def get_nets(self):
        nets = {}
        for iface in self.ifaces:
            if iface != "lo":
                nets[iface] = ".".join(ni.ifaddresses(iface)[2][0][
                                       "addr"].split(".")[0:3])+".0/24"
            else:
                nets[iface] = ni.ifaddresses(iface)[2][0]["addr"]
        return nets

if __name__ == '__main__':
    nmapex = NmapExpert()
    hash_hosts = nmapex.get_hash_hosts(nmapex.get_nets(ni.interfaces()))
    print hash_hosts
