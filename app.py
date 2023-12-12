# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import json
import telebot
from MIM_DEV.modules.shodan.shodan_modules import shodan1, shodan2, shodan3, shodan4
from MIM_DEV.modules.harvester.harvester_modules import run_the_harvester
from MIM_DEV.data.config import TELEGRAM_API_KEY

bot = telebot.TeleBot(TELEGRAM_API_KEY)

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

all_results = []

@app.route('/')
def index():
    return render_template('index.html')

def clean_results(results):
    cleaned_results = []
    
    if isinstance(results, list):
        for result in results:
            if isinstance(result, dict):
                cleaned_result = {}
                for key, value in result.items():
                    cleaned_key = key.replace(' ', '').replace("'", '')
                    if isinstance(value, str):
                        cleaned_value = value.replace(' ', '').replace("'", '')
                    else:
                        cleaned_value = value  # Mantén el valor tal como está para otros tipos
                    cleaned_result[cleaned_key] = cleaned_value
                cleaned_results.append(cleaned_result)
            elif isinstance(result, str):
                cleaned_results.append(result)
    
    return cleaned_results

@app.route('/shodan', methods=['GET', 'POST'])
def shodan_menu():
    global all_results

    if request.method == 'POST':
        domain = request.form.get('domain')

        if domain:
            option = request.form.get('option')
            if option == '1':
                results = shodan1(domain)
            elif option == '2':
                results = shodan2(domain)
            elif option == '3':
                results = shodan3(domain)
            elif option == '4':
                service_name = request.form.get('service_name')
                results = shodan4(service_name, domain)
            else:
                results = []

            if isinstance(results, list) and all(isinstance(result, dict) for result in results):
                all_results.extend(results)

        if 'clear' in request.form:
            all_results = []
            # Puedes agregar aquí la lógica para guardar el resultado en un archivo si es necesario
        elif 'send_results' in request.form:
            if all_results:
                cleaned_results = clean_results(all_results)
                chat_id = '1036744939'
                bot.send_message(chat_id, 'Resultados de Shodan:')
                for result in cleaned_results:
                    bot.send_message(chat_id, str(result))

    return render_template('shodan.html', results=all_results)

@app.route('/harvester', methods=['GET', 'POST'])
def harvester_menu():
    global all_results

    if request.method == 'POST':
        domain = request.form.get('domain')

        if 'clear' in request.form:
            all_results = []
            with open('harvester_results.json', 'w') as json_file:
                json.dump(all_results, json_file)
            chat_id = '1036744939'
            bot.send_message(chat_id, 'Resultados de Harvester eliminados.')
        else:
            try:
                with open('harvester_results.json', 'r') as json_file:
                    file_content = json_file.read()
                    if file_content:
                        all_results = json.loads(file_content)
                    else:
                        all_results = []
            except FileNotFoundError:
                all_results = []

            if domain:
                harvester_results = run_the_harvester(domain)

                if 'results' in harvester_results[0]:
                    all_results.extend(harvester_results)

                with open('harvester_results.json', 'w') as json_file:
                    json.dump(all_results, json_file)

    return render_template('harvester.html', results=clean_results(all_results))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
