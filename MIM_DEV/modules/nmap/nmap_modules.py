import nmap

def nmap1():
    escaneig = nmap.PortScanner()
    xarxa = input("\nIntrodueix la xarxa a escanejar (ex: 192.168.1.0/24): \n")
    escaneig.scan(hosts = xarxa, arguments = '-n -sP')
    llista_hosts = escaneig.all_hosts()
    f = open("resultats.json", "a")
    f.write("\n" + "##~ HOSTS DE LA XARXA " + xarxa + " ~##" + "\n")
    print("Els hosts trobats són:")
    for host in llista_hosts:
        print(host)
        f.write(host + "\n")

def nmap2():
    escaneig = nmap.PortScanner()
    target = input("\nIntrodueix la IP o el nom del host a escanejar (ex: 192.168.1.0): \n")
    escaneig.scan(hosts=target, arguments='-n -sS -sV -p-')
    f = open("resultats.json", "a")
    f.write("\n" + "##~ ESCANEIG DE PORTS OBERTS DEL HOST " + target + " ~##" + "\n")
    for host in escaneig.all_hosts():
        if escaneig[host].state() == 'up':
            ports_oberts = escaneig[host]['tcp'].keys()
            print(f"Ports oberts en {host}:")
            for port in ports_oberts:
                print(f"- Port {port} ({escaneig[host]['tcp'][port]['name']})")
                f.write(f"- Port {port} ({escaneig[host]['tcp'][port]['name']})\n")

def nmap3():
    nm = nmap.PortScanner()
    target = input("\nIntrodueix la IP o el nom del host a escanejar (ex: 192.168.1.0): \n")
    port_range = input("\nIntrodueix el rang de ports a escanejar (ex: 80,443 o 1-1024): \n")
    nm.scan(hosts=target, arguments='-n -sS -sV -p' + port_range)
    f = open("resultats.json", "a")
    f.write("\n" + "##~ ESCANEIG DELS SERVEIS DEL RANG DE PORTS " +port_range + " DEL HOST" +target + " ~##" + "\n")
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            open_ports = nm[host]['tcp'].keys()
            print(f"Serveis i versions trobats en {host}:")
            for port in open_ports:
                print(
                    f"- Port {port} ({nm[host]['tcp'][port]['name']}): {nm[host]['tcp'][port]['product']} {nm[host]['tcp'][port]['version']}")
                f.write(f"- Port {port} ({nm[host]['tcp'][port]['name']}): {nm[host]['tcp'][port]['product']} {nm[host]['tcp'][port]['version']}\n")

def nmap4():
    nm = nmap.PortScanner()
    target = input("\nIntrodueix la IP o el nom del host a escanejar (ex: 192.168.1.0): \n")
    port = input("\nIntrodueix el port a escanejar: \n")
    nm.scan(hosts=target, arguments='-n -sS -sV -p' + port)
    f = open("resultats.json", "a")
    f.write("\n" + "##~ VULNERABILITAT DEL SERVEI SITUAT AL PORT " +port + " DEL HOST " +target + " ~##" + "\n")
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            service_name = nm[host]['tcp'][int(port)]['name']
            print(f"Vulnerabilitats trobades en {host} ({service_name}):")
            vulnerabilities = nm[host]['tcp'][int(port)]
            for vulnerability in vulnerabilities:
                print(f"- {vulnerability} : {vulnerabilities[vulnerability]}")
                f.write(f"- {vulnerability} : {vulnerabilities[vulnerability]}\n")