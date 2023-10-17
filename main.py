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
from MIM_DEV.modules.shodan import shodan_modules
from MIM_DEV.data.config import TELEGRAM_API_KEY
from MIM_DEV.modules.harvester import harvester_modules
from MIM_DEV.modules.nmap.nmap_modules import nmap1, nmap2, nmap3, nmap4

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
        bot.delete_message(chat_id, message_id - i)

    print(banner.renderText("# MIM #"))
    os._exit(0)

with open("resultats.json", "w") as f:
    f.write(format_data + "\n")

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
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan_modules.shodan1(domini_objectiu)
            
            elif option == 2:
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan_modules.shodan2(domini_objectiu)
            
            elif option == 3:
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan_modules.shodan3(domini_objectiu)
            
            elif option == 4:
                domini_objectiu = input("Insereix un objectiu en format URL (ex: www.google.com\n")
                service_name = input("Insereix el nom del servei que vols escanejar :\n")
                shodan_modules.shodan4(service_name, domini_objectiu)

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
            print("2. Veure resultats a Telegram")
            print("3. Tornar al menú principal")
            print("4. Sortir del programa")

        while True:
            menuharvester()
            option = int(input())
            if option == 1:
                print("Introdueix l'objectiu (domini o adreça IP):")
                target = input()
                harvester_modules.run_the_harvester(target)  # Llama a la función de The Harvester

            elif option == 2:
                print("Pots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")

            elif option == 3:
                break  # Volver al menú principal

            elif option == 4:
                print("Sortint del programa.")
                exit()

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
                print("\nPots trobar els resultats accedint al següent enllaç: https://t.me/projecte2324_bot")
                bot.polling()

            elif option == 7:
                f.close()
                os._exit(0)
        break

    elif option == 4:
        break
