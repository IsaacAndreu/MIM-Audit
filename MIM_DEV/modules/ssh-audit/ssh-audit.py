import subprocess

def ssh1():
    host = str(input("Sobre quin equip vols fer l'auditoria? (ex. 192.168.X.X) "))
    comanda = f"ssh-audit {host}"
    try:
        subprocess.run(comanda, shell=True, text=True)

        r = subprocess.run(comanda, text=True, capture_output=True, shell=True)
        with open("resultats.json", "w") as f_resultats:
            f_resultats.write(str(r.stdout))
        
    except subprocess.CalledProcessError as e:
        print(f"Error per realitzar l'auditoria: {e}")

def ssh2():
    domini = str(input("Sobre quin domini vols fer l'auditoria? (ex. github.com) "))
    comanda = f"ssh-audit {domini}"
    try:
        subprocess.run(comanda, shell=True)

        r = subprocess.run(comanda, text=True, capture_output=True, shell=True)
        with open("resultats.json", "w") as f_resultats:
            f_resultats.write(str(r.stdout))

    except subprocess.CalledProcessError as e:
        print(f"Error per realitzar l'auditoria: {e}")