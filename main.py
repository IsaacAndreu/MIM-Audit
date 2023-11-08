import datetime
import logging
import os
from pyfiglet import Figlet
import shodan
import requests
import json
import telebot
import subprocess
import nmap
import re
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from MIM_DEV.modules.shodan import shodan_modules
from MIM_DEV.data.config import TELEGRAM_API_KEY
from MIM_DEV.modules.harvester import harvester_modules
from MIM_DEV.modules.nmap.nmap_modules import nmap1, nmap2, nmap3, nmap4
from MIM_DEV.modules.enum4linux.enum4linux_modules import run_enum4linux

banner = Figlet(font='isometric4')

data = datetime.datetime.today()
datastring = data.strftime("%d-%m-%Y")
format_data = "Auditoria realitzada a data de " + datastring

token = TELEGRAM_API_KEY
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_file(message):
    chat_id = message.chat.id
    file_paths = ["/home/alumne/Escriptori/Code/Curs/projecte-23-24/resultats.json"] 

    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id, file)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    chat_id = message.chat.id
    message_id = message.message_id

    for i in range(5):
        try:
            bot.delete_message(chat_id, message_id - i)
        except telebot.apihelper.ApiTelegramException as e:
            if "message to delete not found" in str(e):
                pass
            else:
                print(f"Error al eliminar el mensaje: {e}")
    
    print(banner.renderText("# MIM #"))
    os._exit(0)

with open("resultats.json", "w") as f:
    f.write(format_data + "\n")

def is_valid_url(url):
    url_pattern = re.compile(r'^[a-zA-Z0-9.-]+.[a-zA-Z]{2,6}(/?|/.*?)$')
    return re.match(url_pattern, url) is not None

def is_valid_number(input_str):
    return input_str.isdigit()

print(banner.renderText("# M I M #"))
print("## Benvingut al menú del projecte ##")
print("## Versió 1.0 ##")
print("## Programat per Marc Queral, Max Segura, Isaac Andreu ##")
print("## Programa defensiu dissenyat per neutralitzar possibles amenaces," "\n" " reforçar la seguretat del sistema i garantir l'integritat dels"
      "\n" " dispositius i serveis de la xarxa. \n")

print("Escull una de les següents opcions: \n")

def menuprincipal():
    print("1. Shodan API")
    print("2. Harvester")
    print("3. Escaneig")
    print("4. Auditoria SSH")
    print("5. Enumeració")
    print("6. Rebre resultats i sortir")
    print("7. Sortir sense resultats")

while True:
    menuprincipal()
    option = int(input())
    if option == 1:
        print("Has escollit el menú de Shodan API. Ara, escull una de les següents opcions:\n")

        def menushodan():
            print("1. Cerca d'informació de l'API de Shodan")
            print("2. Noms de domini i ports oberts")
            print("3. Servei relacionat a cada port")
            print("4. A quines IP i quins ports puc trobar aquest servei?")
            print("5. Tornar al menú principal")
            print("6. Rebre resultats i sortir")
            print("7. Sortir sense resultats")

        while True:
            menushodan()
            option = int(input())
            if option == 1:
                while True:
                    domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                    if is_valid_url(domini_objectiu):
                        shodan_modules.shodan1(domini_objectiu)
                        break
                    else:
                        print("URL no válida. Introdueix una URL válida.")
            elif option == 2:
                while True:
                    domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                    if is_valid_url(domini_objectiu):
                        shodan_modules.shodan2(domini_objectiu)
                        break
                    else:
                        print("URL no válida. Introdueix una URL válida.")
            
            elif option == 3:
                while True:
                    domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                    if is_valid_url(domini_objectiu):
                        shodan_modules.shodan3(domini_objectiu)
                        break
                    else:
                        print("URL no válida. Introdueix una URL válida.")
            
            elif option == 4:
                while True:
                    domini_objectiu = input("Insereix un objectiu en format URL (ex: www.google.com\n")
                    service_name = input("Insereix el nom del servei que vols escanejar :\n")
                    if is_valid_url(domini_objectiu):
                        shodan_modules.shodan4(service_name, domini_objectiu)
                        break
                    else:
                        print("URL no válida. Introdueix una URL válida.")

            elif option == 5:
                break

            elif option == 6:
                f.close()
                print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
                bot.polling()

            elif option == 7:
                f.close()
                os._exit(0)
        
    elif option == 2:
        print("Has triat el menú de The Harvester. Escull una de les següents opcions:\n")
        
        def menuharvester():
            print("1. Executar The Harvester")
            print("2. Rebre resultats i sortir")
            print("3. Tornar al menú principal")
            print("4. Sortir del programa")

        while True:
            menuharvester()
            option = int(input())
            if option == 1:
                print("Introdueix l'objectiu (domini o adreça IP):")
                target = input()
                harvester_modules.run_the_harvester(target) 

            elif option == 2:
                f.close()
                print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
                bot.polling()

            elif option == 3:
                break 

            elif option == 4:
                f.close()
                os._exit(0)

    elif option == 3:
        print("Has escollit el menu d'escaneig (Nmap). Ara, escull una de les següents opcions:\n")

        def menunmap():
            print("1. Descobreix hosts de xarxa")
            print("2. Escaneig de ports oberts")
            print("3. Llistar serveis i versions d'un, un rang o tots els ports")
            print("4. Llistar vulnerabilitats d'un, un rang o tots els serveis")
            print("5. Tornar al menu principal")
            print("6. Rebre resultats i sortir")
            print("7. Sortir sense resultats\n")

        while True:
            menunmap()
            option = int(input())
            if option == 1:
                nmap1()

            elif option == 2:
                nmap2()

            elif option == 3:
                nmap3()

            elif option == 4:
                nmap4()
                
            elif option == 5:
                break

            elif option == 6:
                f.close()
                print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
                bot.polling()

            elif option == 7:
                f.close()
                os._exit(0)
        break

    elif option == 4:
        print("Has escollit el menú d'auditoria SSH. Ara, escull les següents opcions:\n")


    elif option == 5:
        print("Has escollit el menú d'escaneig (Enum4linux). Ara, escull les següents opcions:\n")

        def menuenum4():
            print("1. Executar Enum4linux")
            print("2. Rebre resultats i sortir")
            print("3. Tornar al menú principal")
            print("4. Sortir del programa")
        
        while True:
            menuenum4()
            option = int(input())
            if option == 1:
                print("Introduiu l'objectiu (domini o adreça IP):")
                target = input()
            
                run_enum4linux(target)
                print("Enum4linux ha finalitzat.")
            
            elif option == 2:
                f.close()
                print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
                bot.polling()
            
            elif option == 3:
                break

            elif option == 4:
                f.close()
                os._exit(0)
    
    elif option == 6:
        f.close()
        print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
        bot.polling()
    
    elif option == 7:
        f.close()
        os._exit(0)

    