import shodan
import json
import requests
from MIM_DEV.data.config import SHODAN_API_KEY


def shodan1(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)        
        hostip = resolved.json().get(domini_objectiu)

        if hostip:
            host = api.host(hostip)

            with open("resultats.json", "a") as f:
                f.write("\n" + "##~ Cerca d'informació de l'api de Shodan ~##" + "\n")
                f.write("IP: %s" % host['ip_str'] + "\n")
                f.write("Organizació: %s" % host.get('org', 'n/a') + "\n")

            print("IP: %s" % host['ip_str'])
            print("Organización: %s" % host.get('org', 'n/a'))
        else:
            print("No s'ha pogut resoldre el domini o no s'ha trobat informació a Shodan..")

    except Exception as e:
        print("Error: ", e)


def shodan2(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)
        hostip = resolved.json().get(domini_objectiu)

        if hostip:
            host = api.host(hostip)

            with open("resultats.json", "a") as f:
                f.write("\n" + "##~ Noms de domini i ports oberts ~##" + "\n")
                f.write("Noms de domini: %s" % ', '.join(host.get('hostnames', ['N/A'])) + "\n")
                f.write("Ports oberts:\n")
                for item in host['data']:
                    print("Port: %s" % item['port'])
                    f.write("Port: %s\n" % item['port'])
                    
            print("Informació dels ports oberts i els nombres de dominis esta escrita a resultats.json")
        else:
            print("No s'ha pogut resoldre el domini o no s'ha trobat informació a Shodan.")
    except Exception as e:
        print("Error: ", e)



def shodan3(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        results = api.search(f"hostname:{domini_objectiu}")

        print(f"Servicio relacionado a cada puerto para la domini_objectiu: {domini_objectiu}")
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
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        results = api.search(f"product:{service_name}")

        print(f"IPs y puertos relacionados con el servicio '{service_name}':")
        for result in results['matches']:
            ip = result['ip_str']
            ports = result.get('ports', 'N/A')
            print(f"IP: {ip}")
            print(f"Puertos: {', '.join(map(str, ports)) if ports != 'N/A' else 'N/A'}")
            print(f"--------------------------")

    except shodan.APIError as e:
        print(f"Error en la búsqueda de Shodan: {e}")




