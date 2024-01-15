import nmap

def nmap1(xarxa):
    escaneig = nmap.PortScanner()
    escaneig.scan(hosts=xarxa, arguments='-n -sP')
    llista_hosts = escaneig.all_hosts()

    return {'message': f'Les adreces IP trobades a la xarxa {xarxa} són les següents:', 'hosts': llista_hosts}


def nmap2(ip2):
    escaneig = nmap.PortScanner()
    escaneig.scan(hosts=ip2, arguments='-n -sS -sV -p-')
    llista_ports = []

    if ip2 in escaneig.all_hosts():
        protocols = escaneig[ip2]
        if 'tcp' in protocols:
            for port, protocol_info in protocols['tcp'].items():
                port_info = {
                    'port': port,
                    'protocol': 'tcp',
                    'service': protocol_info['name'],
                    'state': protocol_info['state'],
                }
                llista_ports.append(port_info)

    missatge = f'Els ports oberts a la IP {ip2} són els següents:'

    return {'message': missatge, 'ports': llista_ports}

def nmap3(ip3, ports):
    escaneig = nmap.PortScanner()

    escaneig.scan(hosts=ip3, ports=ports, arguments='-n -sV')

    llista_servicios_versiones = []

    if ip3 in escaneig.all_hosts():
        for port, port_info in escaneig[ip3]['tcp'].items():
            servicio_version = {
                'service': port_info.get('name', 'N/A'),
                'version': port_info.get('version', 'N/A'),
            }
            llista_servicios_versiones.append(servicio_version)

        missatge = f'Els serveis i versions a la IP {ip3} i ports {ports} són els següents:'
    
    else:
        missatge = f'No s\'ha trobat cap servei a la IP {ip3} i ports {ports}.'
    
    return {'message': missatge, 'services_versions': llista_servicios_versiones}

def nmap4(ip4, ports4):
    try:
        escaneig = nmap.PortScanner()
        escaneig.scan(hosts=ip4, ports=ports4, arguments='-sV --script vulners')

        llista_vulnerabilitats = []

        for ip_address in escaneig.all_hosts():
            escaneig.scan(hosts=ip_address, ports=ports4, arguments='-sV --script vulners')

            for protocol in escaneig[ip_address].all_protocols():
                ports = escaneig[ip_address][protocol].keys()
                for port in ports:
                    port_info = escaneig[ip_address][protocol][port]
                    vulnerabilities = port_info.get('script', {}).get('vulners', [])

                    for vulnerability in vulnerabilities:
                        llista_vulnerabilitats.append({
                            'ip_address': ip_address,
                            'port': port,
                            'protocol': protocol,
                            'service': port_info['name'],
                            'vulnerability': vulnerability,
                        })

        if not llista_vulnerabilitats:
            missatge = f'No se encontraron vulnerabilidades en la IP {ip4}, puertos {ports4}.'
        else:
            missatge = f'Vulnerabilidades a la IP {ip4}, puertos {ports4} son los siguientes:'

        return {'message': missatge, 'vulnerabilities': llista_vulnerabilitats}

    except Exception as e:
        print(f'Otro error: {str(e)}')
        return {'message': f'Otro error: {str(e)}', 'vulnerabilities': []}