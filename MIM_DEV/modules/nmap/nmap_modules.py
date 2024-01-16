import nmap

def nmap1(xarxa):
    # Crear una instància de l'escàner Nmap
    escaneig = nmap.PortScanner()
    # Realitzar un escaneig de descobriment de l'host (Ping Scan) a la xarxa especificada
    escaneig.scan(hosts=xarxa, arguments='-n -sP')
    # Obtenir la llista d'adreces IP trobades a la xarxa
    llista_hosts = escaneig.all_hosts()

    return {'message': f'Les adreces IP trobades a la xarxa {xarxa} són les següents:', 'hosts': llista_hosts}

def nmap2(ip2):
    # Crear una nova instància de l'escàner Nmap
    escaneig = nmap.PortScanner()
    # Realitzar un escaneig TCP SYN a l'adreça IP especificada, obtenint informació dels ports oberts
    escaneig.scan(hosts=ip2, arguments='-n -sS -sV -p-')
    # Inicialitzar una llista buida per emmagatzemar informació dels ports oberts
    llista_ports = []

    if ip2 in escaneig.all_hosts():
        # Si l'adreça IP està activa, obtenir informació dels ports TCP
        protocols = escaneig[ip2]
        if 'tcp' in protocols:
            for port, protocol_info in protocols['tcp'].items():
                # Crear un diccionari amb informació del port
                port_info = {
                    'port': port,
                    'protocol': 'tcp',
                    'service': protocol_info['name'],
                    'state': protocol_info['state'],
                }
                # Afegir la informació del port a la llista
                llista_ports.append(port_info)

    missatge = f'Els ports oberts a la IP {ip2} són els següents:'

    return {'message': missatge, 'ports': llista_ports}

def nmap3(ip3, ports):
    # Crear una nova instància de l'escàner Nmap
    escaneig = nmap.PortScanner()

    # Realitzar un escaneig específic dels ports a l'adreça IP especificada
    escaneig.scan(hosts=ip3, ports=ports, arguments='-n -sV')

    # Inicialitzar una llista buida per emmagatzemar informació dels serveis i versions
    llista_servicios_versiones = []

    if ip3 in escaneig.all_hosts():
        for port, port_info in escaneig[ip3]['tcp'].items():
            # Crear un diccionari amb informació del servei i versió
            servicio_version = {
                'service': port_info.get('name', 'N/A'),
                'version': port_info.get('version', 'N/A'),
            }
            # Afegir la informació del servei i versió a la llista
            llista_servicios_versiones.append(servicio_version)

        missatge = f'Els serveis i versions a la IP {ip3} i ports {ports} són els següents:'
    
    else:
        missatge = f'No s\'ha trobat cap servei a la IP {ip3} i ports {ports}.'
    
    return {'message': missatge, 'services_versions': llista_servicios_versiones}

def nmap4(ip4, ports4):
    try:
        # Intentar realitzar un escaneig amb la detecció de vulnerabilitats
        escaneig = nmap.PortScanner()
        escaneig.scan(hosts=ip4, ports=ports4, arguments='-sV --script vulners')

        # Inicialitzar una llista buida per emmagatzemar informació de vulnerabilitats
        llista_vulnerabilitats = []

        for ip_address in escaneig.all_hosts():
            # Tornar a escanejar per obtenir informació més detallada sobre les vulnerabilitats
            escaneig.scan(hosts=ip_address, ports=ports4, arguments='-sV --script vulners')

            for protocol in escaneig[ip_address].all_protocols():
                ports = escaneig[ip_address][protocol].keys()
                for port in ports:
                    port_info = escaneig[ip_address][protocol][port]
                    vulnerabilities = port_info.get('script', {}).get('vulners', [])

                    for vulnerability in vulnerabilities:
                        # Crear un diccionari amb informació de la vulnerabilitat
                        llista_vulnerabilitats.append({
                            'ip_address': ip_address,
                            'port': port,
                            'protocol': protocol,
                            'service': port_info['name'],
                            'vulnerability': vulnerability,
                        })

        if not llista_vulnerabilitats:
            missatge = f'No shan trobat vulnerabilitats en la IP {ip4}, ports {ports4}.'
        else:
            missatge = f'Vulnerabilitats a la IP {ip4}, ports {ports4} son los següents:'

        return {'message': missatge, 'vulnerabilities': llista_vulnerabilitats}

    except Exception as e:
        # Capturar qualsevol excepció i imprimir un missatge d'error
        print(f'Otro error: {str(e)}')
        return {'message': f'Otro error: {str(e)}', 'vulnerabilities': []}
