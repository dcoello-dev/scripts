import nmap


def filter_hosts(arr):
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

nm = nmap.PortScanner()

nm.scan(hosts='192.168.22.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x,
               nm[x]['status']['state'],
               nm[x]['vendor'],
               nm[x]['addresses']) for x in nm.all_hosts()]

hash_hosts = filter_hosts(hosts_list)

for hah in hash_hosts:
    print hah["host"] +"   "+hah["vendor"]+"    "+hah["mac"]
    #print hah
