import subprocess
import json
import yaml
import re

def load_api_keys(api_keys_file):
    try:
        api_file_path = api_keys_file
        # Obrir el fitxer YAML que conté les claus de l'API
        with open(api_file_path, "r") as api_file:
            # Carregar les claus de l'API utilitzant el carregador FullLoader de YAML
            api_keys = yaml.load(api_file, Loader=yaml.FullLoader)
            return api_keys
    except FileNotFoundError:
        print(f"El fitxer {api_keys_file} no s'ha trobat a la ruta especificada.")
        return {}

def run_the_harvester(target, api_keys_file="/home/alumne/Escriptori/Code/Curs/MIM-Audit/api-keys.yaml"):
    # Carregar les claus de l'API
    api_keys = load_api_keys(api_keys_file)

    # Crear la comanda del Harvester amb l'objectiu especificat
    command = f"/usr/local/bin/theHarvester -d {target} -b all"

    try:
        # Executar la comanda i capturar la sortida
        print(f"Executant comanda: {command}")
        output_bytes = subprocess.check_output(command, shell=True)
        output = output_bytes.decode('utf-8')  
        print("The Harvester s'ha executat correctament.")

        # Guardar els resultats en un fitxer JSON
        result_data = {'target': target, 'results': output}
        with open('harvester_results.json', 'w') as json_file:
            json.dump(result_data, json_file)

        return [result_data]
    except Exception as e:
        # Capturar errors en cas que hi hagi algun problema durant l'execució
        print(f"Error en executar The Harvester: {str(e)}")
        return [{'target': target, 'error': str(e)}]
