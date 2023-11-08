# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import json  # Agrega esta línea para importar el módulo 'json'
from MIM_DEV.modules.shodan.shodan_modules import shodan1, shodan2, shodan3, shodan4
from MIM_DEV.modules.harvester.harvester_modules import run_the_harvester
from MIM_DEV.data.config import SHODAN_API_KEY
from MIM_DEV.data.config import TELEGRAM_API_KEY
import telebot
import multiprocessing

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
        elif 'send_results' in request.form:
            cleaned_results = clean_results(all_results)

            chat_id = '1036744939' 
            bot.send_message(chat_id, 'Resultados de Shodan:')
            for result in cleaned_results:
                bot.send_message(chat_id, str(result))

    return render_template('shodan.html', results=all_results)

def run_the_harvester_process(domain):
    run_the_harvester(domain, api_keys_file="/home/alumne/Escriptori/Code/Curs/projecte-23-24/api-keys.yaml")

@app.route('/harvester', methods=['GET', 'POST'])
def harvester_menu():
    processing = False
    show_loading_message = False
    results = None

    if request.method == 'POST':
     domain = request.form.get('domain')
     if domain:
        processing = True
        show_loading_message = True
        p = multiprocessing.Process(target=run_the_harvester_process, args=(domain,))
        p.start()
        p.join()  # Esperar a que el proceso de TheHarvester termine
        with open("/home/alumne/Escriptori/Code/Curs/projecte-23-24/harvester_results.json", "r") as file:
            results = json.load(file)
        show_loading_message = False
    
    return render_template('harvester.html', results=results, processing=processing, show_loading_message=show_loading_message)

@app.route('/check_harvester_results')
def check_harvester_results():
    global all_results
    return jsonify({'results_ready': len(all_results) > 0})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    bot.polling()


