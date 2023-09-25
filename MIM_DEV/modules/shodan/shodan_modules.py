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
                f.write("Organización: %s" % host.get('org', 'n/a') + "\n")

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
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)
        resolved_data = resolved.json()

        if domini_objectiu in resolved_data:
            hostip = resolved_data[domini_objectiu]
            host = api.host(hostip)

            with open("resultats.json", "w") as f:
                f.write("\n" + "##~ SERVEIS VINCULATS A PORTS ~##" + "\n")
                for item in host['data']:
                    print("Port: %s" % item['port'])
                    f.write("Port: %s" % item['port'] + "\n")
                    objecte = item['data'].split("\n")
                    print(objecte[0])
                    f.write(objecte[0] + "\n")
        else:
            print("No se pudo resolver el dominio o no se encontró información en Shodan.")

    except Exception as e:
        print("Error: ", e)

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




