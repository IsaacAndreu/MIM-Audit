import subprocess
import json
import netaddr
import yaml
import requests
import telebot
from MIM_DEV.data.config import TELEGRAM_API_KEY
import shutil  # Importa la biblioteca shutil

def load_api_keys(api_keys_file):
    try:
        api_file_path = api_keys_file
        with open(api_file_path, "r") as api_file:
            api_keys = yaml.load(api_file, Loader=yaml.FullLoader)
            return api_keys
    except FileNotFoundError:
        print(f"El archivo {api_keys_file} no se encontró en la ruta especificada.")
        return {}

def run_the_harvester(target, api_keys_file="/projecte-23-24/api-keys.yaml"):
    api_keys = load_api_keys(api_keys_file)

    command = f"/usr/local/bin/theHarvester -d {target} -b all -l 500 -f harvester_results.json"

    try:
        subprocess.call(command, shell=True)
        print("The Harvester se ha ejecutado correctamente.")

        with open("harvester_results.json", "r") as harvester_file:
            harvester_results = harvester_file.read()

        with open("resultats.json", "a") as resultats_file:
            resultats_file.write(harvester_results)

    except Exception as e:
        print(f"Error al ejecutar The Harvester: {str(e)}")

