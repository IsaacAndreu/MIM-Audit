# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import json
import telebot
import re
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
            all_results.clear()
            send_results_to_file()

        elif 'send_results' in request.form:
            if all_results:
                chat_id = '1036744939'
                bot.send_message(chat_id, 'Enviando archivo Shodan Results...')
                send_results_to_file()
                send_file_to_telegram()

    return render_template('shodan.html', results=all_results)

def send_results_to_file():
    global all_results
    try:
        with open('shodan_results.json', 'w') as json_file:
            json.dump(all_results, json_file)
    except Exception as e:
        print(f"Error al guardar resultados en shodan_results.json: {e}")

def send_file_to_telegram():
    global bot
    chat_id = '1036744939'

    try:
        with open('shodan_results.json', 'rb') as file:
            bot.send_document(chat_id, file)
    except Exception as e:
        print(f"Error al enviar archivo a Telegram: {e}")

all_results = []

@app.route('/harvester', methods=['GET', 'POST'])
def harvester_menu():
    global all_results

    if request.method == 'POST':
        domain = request.form.get('domain')

        if 'clear' in request.form:
            all_results.clear()
            send_results_to_file()
            chat_id = '1036744939'
            bot.send_message(chat_id, 'Resultados de Harvester eliminados.')
        elif 'send_results' in request.form:
            send_harvester_results_to_telegram()
        else:
            try:
                with open('harvester_results.json', 'r') as json_file:
                    file_content = json_file.read()
                    if file_content:
                        all_results = json.loads(file_content)
                    else:
                        all_results.clear()
            except FileNotFoundError:
                all_results.clear()

            if domain:
                harvester_results = run_the_harvester(domain)

                if 'results' in harvester_results[0]:
                    all_results.extend(harvester_results)

                send_results_to_file()

    return render_template('harvester.html', results=all_results)

def send_harvester_results_to_telegram():
    try:
        with open('harvester_results.json', 'r') as file:
            results_data = json.load(file)

            # Extraer la sección de resultados específica
            specific_results = results_data.get('results', '')

            # Eliminar los enlaces
            specific_results = re.sub(r'\[.*?\]\(.*?\)', '', specific_results)

            # Eliminar los asteriscos del contenido
            specific_results = specific_results.replace('*', '')

            # Dividir el contenido en partes de longitud máxima permitida por la API de Telegram
            max_message_length = 4096  # Longitud máxima permitida por la API de Telegram
            message_parts = [specific_results[i:i + max_message_length] for i in range(0, len(specific_results), max_message_length)]

            chat_id = '1036744939'

            # Enviar cada parte como un mensaje separado
            for part in message_parts[:-1]:  # Enviar todo excepto la última parte
                bot.send_message(chat_id, part)

            # Enviar la última parte (que contiene correos electrónicos) en otro mensaje
            bot.send_message(chat_id, message_parts[-1])
    except FileNotFoundError:
        print("File 'harvester_results.json' not found.")
    except Exception as e:
        print(f"Error sending Harvester results to Telegram: {e}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
