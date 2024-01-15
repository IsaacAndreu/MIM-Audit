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


            specific_results = results_data.get('results', '')

    
            specific_results = re.sub(r'\[.*?\]\(.*?\)', '', specific_results)

            specific_results = specific_results.replace('*', '')

           
            max_message_length = 4096 
            message_parts = [specific_results[i:i + max_message_length] for i in range(0, len(specific_results), max_message_length)]

            chat_id = '1036744939'

            for part in message_parts[:-1]:  
                bot.send_message(chat_id, part)

            
            bot.send_message(chat_id, message_parts[-1])
    except FileNotFoundError:
        print("File 'harvester_results.json' not found.")
    except Exception as e:
        print(f"Error sending Harvester results to Telegram: {e}")

@app.route('/nmap', methods=['GET', 'POST'])
def nmap_menu():
    global all_results

    try:
        if request.method == 'POST':
            option = request.form.get('option')
            if option == '1':
                xarxa = request.form.get('xarxa')
                result_nmap1 = nmap1(xarxa)

                return render_template('nmap.html', result_nmap1=result_nmap1)

            elif option == '2':
                ip2 = request.form.get('ip2')
                result_nmap2 = nmap2(ip2)
                
                return render_template('nmap.html', result_nmap2=result_nmap2)

            elif option == '3':
                ip3 = request.form.get('ip3')
                ports = request.form.get('ports')
                result_nmap3 = nmap3(ip3, ports)
                
                return render_template('nmap.html', result_nmap3=result_nmap3)

            elif option == '4':
                ip4 = request.form.get('ip4')
                ports4 = request.form.get('ports4')
                result_nmap4 = nmap4(ip4, ports4)
                
                return render_template('nmap.html', result_nmap4=result_nmap4)

            else:
                results = []

                if isinstance(results, list) and all(isinstance(result, dict) for result in results):
                    all_results.extend(results)

    except Exception as e:
        error_message = f"Error en la aplicación: {str(e)}"
        return render_template('error.html', error_message=error_message)

    if 'clear' in request.form:
            all_results.clear()
            send_nmap_results_to_file()

    elif 'send_results' in request.form:
        if all_results:
            chat_id = '1036744939'
            bot.send_message(chat_id, 'Enviando archivo Nmap Results...')
            send_nmap_results_to_file()
            send_nmap_file_to_telegram()

    return render_template('nmap.html', results=all_results)

def send_nmap_results_to_file():
    global all_results
    try:
        with open('nmap_results.json', 'w') as json_file:
            json.dump(all_results, json_file)
    except Exception as e:
        print(f"Error al guardar resultados en nmap_results.json: {e}")

def send_nmap_file_to_telegram():
    global bot
    chat_id = '1036744939'

    try:
        with open('nmap_results.json', 'rb') as file:
            bot.send_document(chat_id, file)
    except Exception as e:
        print(f"Error al enviar archivo a Telegram: {e}")

all_results = []

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
