import subprocess

# Funció per realitzar l'auditoria SSH amb una adreça IP
def ssh1(ip):
    # Construïm la comanda ssh-audit amb l'adreça IP proporcionada
    comanda = f"ssh-audit {ip}"

    try:
        # Executem la comanda i capturem la sortida
        result = subprocess.run(comanda, text=True, capture_output=True, shell=True)

        # Retornem la sortida de l'auditoria SSH
        return result.stdout

    except subprocess.CalledProcessError as e:
        # En cas d'error, retornem un missatge d'error
        return f"Error en la auditoría SSH: {e}"

# Funció per realitzar l'auditoria SSH amb un domini
def ssh2(domini):
    # Construïm la comanda ssh-audit amb el domini proporcionat
    comanda = f"ssh-audit {domini}"

    try:
        # Executem la comanda i capturem la sortida
        result = subprocess.run(comanda, text=True, capture_output=True, shell=True)

        # Retornem la sortida de l'auditoria SSH
        return result.stdout

    except subprocess.CalledProcessError as e:
        # En cas d'error, retornem un missatge d'error
        return f"Error en la auditoría SSH: {e}"
