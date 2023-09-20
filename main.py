
print(banner.renderText("# Menu projecte #"))
print("##Benvingut al menu del projecte##")
print("## Versio 1.0 ##")
print("## Programat per Marc Queralt, Max Segura, Isaac Andreu ##")
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
                shodan1()
            
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

        print("Has escollit el menu d'escaneig. Ara, escull una de les següents opcions:\n")

        def menumap():
            print("1. Descobrir hosts de xarxa")
            print("2. Escaneig de ports oberts")
            print("3. Llistat de serveis i versions d'un, un rang o tots els ports")
            print("4. Llistat de vulnerabilitats d'un, un rang o tots els serveis.")
            print("5. Tornar al menu principal")
            print("6. Rebre resultats i sortir")
            print("7. Sortir sense resultats")

        while True:
            menumap()
            option = int(input())
            if option == 1:
                nmap1()
            
            elif option == 2:
                nmap2()
            
            elif option == 3:
            