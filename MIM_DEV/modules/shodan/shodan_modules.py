import shodan
import json
import requests
from MIM_DEV.data.config import SHODAN_API_KEY

# Funció per obtenir informació bàsica d'una adreça IP associada a un domini
def shodan1(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)
    results = []

    try:
        # Resol l'adreça IP associada al domini
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)
        hostip = resolved.json().get(domini_objectiu)

        if hostip:
            # Obtenim informació bàsica de l'adreça IP
            host = api.host(hostip)
            result = {
                'IP': host['ip_str'],
                'Organització': host.get('org', 'n/a')
            }
            results.append(result)

    except Exception as e:
        results.append("Error: " + str(e))

    return results

# Funció per obtenir informació detallada d'una adreça IP associada a un domini
def shodan2(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)
    results = []

    try:
        # Resol l'adreça IP associada al domini
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)
        hostip = resolved.json().get(domini_objectiu)

        if hostip:
            # Obtenim informació detallada de l'adreça IP
            host = api.host(hostip)
            result = {
                'Noms de domini': ', '.join(host.get('hostnames', ['N/A'])),
                'Ports oberts': [{'Port': item['port']} for item in host['data']]
            }
            results.append(result)

    except Exception as e:
        results.append("Error: " + str(e))

    return results

# Funció per obtenir informació dels ports oberts d'una adreça IP associada a un domini
def shodan3(domini_objectiu):
    api = shodan.Shodan(SHODAN_API_KEY)
    results = []

    try:
        # Resol l'adreça IP associada al domini
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY
        resolved = requests.get(dnsresolve)
        resolved_data = resolved.json()

        if domini_objectiu in resolved_data:
            hostip = resolved_data[domini_objectiu]
            # Obtenim informació dels ports oberts
            host = api.host(hostip)

            port_data = []
            for item in host['data']:
                port_result = {
                    'Port': item['port'],
                    'Info': item['data'].split("\n")[0]
                }
                port_data.append(port_result)

            results = port_data

    except Exception as e:
        results.append("Error: " + str(e))

    return results

# Funció per buscar adreces IP amb un servei específic en un domini
def shodan4(service_name, domini_objectiu):
    results = []

    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        dnsresolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domini_objectiu + '&key=' + SHODAN_API_KEY

        resolved = requests.get(dnsresolve)
        resolved_data = resolved.json()

        if domini_objectiu in resolved_data:
            hostip = resolved_data[domini_objectiu]

            # Cerquem adreces IP amb un servei específic en el domini
            query = f'product:"{service_name}" hostname:"{domini_objectiu}"'
            service_results = api.search(query)

            if service_results['total'] > 0:
                for result in service_results['matches']:
                    service_result = {
                        'IP': result['ip_str'],
                        'Port': result['port']
                    }
                    results.append(service_result)

    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results
