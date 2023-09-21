import datetime
import logging
from pyfiglet import Figlet
import shodan
import requests
import json
from modules.shodan import main as shodan_module


banner = Figlet(font='isometric4')

data = datetime.datetime.today()
datastring = data.strftime("%d-%m-%Y")
format_data = "Auditoria realitzada a data de " + datastring

telegram_api_key = '6676090876:AAH3bmZEhE7buvGz-isGVJf4KmXnhO5FF5c'

shodan_api_key = 'n423QbNhqvvDQR5KAtYxtnh1vDwDd3Dn'


f = open("resultats.json", "w")
f.write(format_data + "\n")


print(banner.renderText("# M I M #"))
print("## Benvingut al menu del projecte ##")
print("## Versio 1.0 ##")
print("## Programat per Marc Queral, Max Segura, Isaac Andreu ##")
print("## Programa defensiu dissenyat per neutralitzar possibles amenaces," "\n" " reforçar la seguretat del sistema i garantir l'integirtat dels"
      "\n" " dispositius i serveis de la xarxa. \n")

print("Escull una de les següents opcions: \n")

def menuprincipal():
    print("1. Shodan Api")
    print("2. Escaneig")
    print("3. Auditoria SSH")
    print("4. Enumeració")
    print("5. Rebre resultats i sortir")
    print("6. Sortir sense resultats")

while True:
    menuprincipal()
    option = int(input())
    if option == 1:
        print("Has escollit el menu de Shodan Api. Ara, escull una de les següents opcions:\n")

        def menushodan():
            print("1. Cerca d'informació de l'api de Shodan")
            print("2. Noms de domini i ports oberts")
            print("3. Servei relacionat a cada port")
            print("4. A quines IP i quins ports puc trovar aquest servei?")
            print("5. Tornar al menu principal")
            print("6. Rebre resultats i sortir")
            print("7. Sortir sense resultats")

        while True:
            menushodan()
            option = int(input())
            if option == 1:
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan1(domini_objectiu)
            
            elif option == 2:
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan2()
            
            elif option == 3:
                domini_objectiu = str(input("Insereix un objectiu en format URL (ex: www.google.com)\n"))
                shodan3()
            
            elif option == 4:
                sys.argv = (input("Insereix el servei que vols escanejar.\n"))
                shodan4()
            elif option == 5:
                break

            elif option == 6:
                f.close()
                print("Pots trobar els resultats accedint al següent enllaç:")
                bot.polling()

            elif option == 0:
                f.close()
                os._exit(0)
        
    elif option == 2:
        break
    
    
          