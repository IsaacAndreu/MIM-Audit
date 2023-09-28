import subprocess
import json

def run_the_harvester(target):
    # Comanda per executar The Harvester amb les opcions desitjades
    command = f"theharvester -d {target} -b all -l 500 -f harvester_results.html"
    
    try:
        # Executa la comanda en un subprocess
        subprocess.call(command, shell=True)
        print("The Harvester s'ha executat correctament.")
        
        # Obre l'arxiu resultats.json en mode lectura i guarda els resultats existents en una variable
        with open("resultats.json", "r") as result_file:
            resultats_antigues = result_file.read()

        # Afegir els resultats nous als resultats existents sense esborrar-los
        with open("resultats.json", "w") as result_file:
            result_file.write(resultats_antigues)
            result_file.write(f"Resultats de The Harvester per a {target}:\n")
            with open("harvester_results.html", "r") as harvester_results_file:
                result_file.write(harvester_results_file.read())
                result_file.write("\n\n")

        # Imprimeix l'enllaç al bot de Telegram
        print("Pots trobar els resultats al bot de Telegram: https://t.me/projecte2324_bot")
    
    except Exception as e:
        print(f"Error en executar The Harvester: {str(e)}")
