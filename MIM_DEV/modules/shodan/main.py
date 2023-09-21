import shodan
from mim_dev.data.config.py import SHODAN_API_KEY

def shodan1():
    # Solicitar al usuario una URL
    url = input("Por favor, ingresa una URL (ejemplo: www.ejemplo.com): ")

    # Definir tu clave de API de Shodan
    shodan_api_key = 'tu_clave_de_api_de_shodan'

    # Crear una instancia del cliente de Shodan
    api = shodan.Shodan(shodan_api_key)

    try:
        # Realizar una búsqueda en Shodan basada en la URL proporcionada
        results = api.search(f"hostname:{url}")

        # Imprimir los resultados
        print("Resultados de la búsqueda en Shodan:")
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Hostname: {result['hostnames']}")
            print(f"Organización: {result.get('org', 'N/A')}")
            print(f"País: {result.get('location', 'N/A')}")
            print(f"--------------------------")

    except shodan.APIError as e:
        print(f"Error en la búsqueda de Shodan: {e}")