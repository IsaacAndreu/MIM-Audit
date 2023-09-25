import shodan
import json
import requests

SHODAN_API_KEY = 'n423QbNhqvvDQR5KAtYxtnh1vDwDd3Dn'

def shodan1(domini_objectiu):
    # Crear una instancia del cliente de Shodan
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Resolver el nombre de dominio a una dirección IP
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)        
        hostip = resolved.json().get(domini_objectiu)

        if hostip:
            # Obtener información del host utilizando la IP resuelta
            host = api.host(hostip)

            # Abrir el archivo resultats.json en modo "a" (adjuntar)
            with open("resultats.json", "a") as f:
                f.write("\n" + "##~ DADES ~##" + "\n")
                f.write("IP: %s" % host['ip_str'] + "\n")
                f.write("Organización: %s" % host.get('org', 'n/a') + "\n")

            # Imprimir los resultados en la consola
            print("IP: %s" % host['ip_str'])
            print("Organización: %s" % host.get('org', 'n/a'))
        else:
            print("No se pudo resolver el dominio o no se encontró información en Shodan.")

    except Exception as e:
        print("Error: ", e)


def shodan2(url):
    # Crear una instancia del cliente de Shodan
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Realizar una búsqueda en Shodan basada en la URL proporcionada
        results = api.search(f"hostname:{url}")

        # Imprimir los nombres de dominio y puertos abiertos
        print(f"Nombres de dominio y puertos abiertos para la URL: {url}")
        for result in results['matches']:
            hostnames = result.get('hostnames', 'N/A')
            ports = result.get('ports', 'N/A')
            print(f"IP: {result['ip_str']}")
            print(f"Nombres de dominio: {', '.join(hostnames) if hostnames != 'N/A' else 'N/A'}")
            print(f"Puertos abiertos: {', '.join(map(str, ports)) if ports != 'N/A' else 'N/A'}")
            print(f"--------------------------")

    except shodan.APIError as e:
        print(f"Error en la búsqueda de Shodan: {e}")

def shodan3(url):
    # Crear una instancia del cliente de Shodan
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Realizar una búsqueda en Shodan basada en la URL proporcionada
        results = api.search(f"hostname:{url}")

        # Imprimir el servicio relacionado a cada puerto
        print(f"Servicio relacionado a cada puerto para la URL: {url}")
        for result in results['matches']:
            ports = result.get('ports', 'N/A')
            data = result.get('data', 'N/A')

            print(f"IP: {result['ip_str']}")
            if ports != 'N/A':
                for port in ports:
                    print(f"Puerto: {port}")
                    if data != 'N/A':
                        for banner in data:
                            if banner['port'] == port:
                                print(f"Servicio: {banner.get('service', 'N/A')}")
                    print(f"--------------------------")

    except shodan.APIError as e:
        print(f"Error en la búsqueda de Shodan: {e}")

def shodan4(service_name):
    # Crear una instancia del cliente de Shodan
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Realizar una búsqueda en Shodan basada en el servicio proporcionado
        results = api.search(f"product:{service_name}")

        # Imprimir las IPs y puertos relacionados con el servicio
        print(f"IPs y puertos relacionados con el servicio '{service_name}':")
        for result in results['matches']:
            ip = result['ip_str']
            ports = result.get('ports', 'N/A')
            print(f"IP: {ip}")
            print(f"Puertos: {', '.join(map(str, ports)) if ports != 'N/A' else 'N/A'}")
            print(f"--------------------------")

    except shodan.APIError as e:
        print(f"Error en la búsqueda de Shodan: {e}")




