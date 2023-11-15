import subprocess
import json
import yaml
import re

def load_api_keys(api_keys_file):
    try:
        api_file_path = api_keys_file
        with open(api_file_path, "r") as api_file:
            api_keys = yaml.load(api_file, Loader=yaml.FullLoader)
            return api_keys
    except FileNotFoundError:
        print(f"El archivo {api_keys_file} no se encontró en la ruta especificada.")
        return {}

def run_the_harvester(target, api_keys_file="/home/alumne/Escriptori/Code/Curs/projecte-23-24/api-keys.yaml"):
    api_keys = load_api_keys(api_keys_file)

    command = f"/usr/local/bin/theHarvester -d {target} -b all"

    try:
        print(f"Ejecutando comando: {command}")
        output_bytes = subprocess.check_output(command, shell=True)
        output = output_bytes.decode('utf-8')  
        print("The Harvester se ha ejecutado correctamente.")

        result_data = {'target': target, 'results': output}
        with open('harvester_results.json', 'w') as json_file:
            json.dump(result_data, json_file)

        return [result_data]
    except Exception as e:
        print(f"Error al ejecutar The Harvester: {str(e)}")
        return [{'target': target, 'error': str(e)}]
