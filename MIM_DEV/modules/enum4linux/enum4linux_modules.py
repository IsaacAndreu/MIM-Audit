import subprocess

def enum4linux1(ip):
    command = f'enum4linux -a -A -U -S -P {ip}'
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            'message': 'Ejecución exitosa de Enum4linux',
            'output': result.stdout
        }
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar Enum4linux: {e}')
        return {
            'message': f'Error al ejecutar Enum4linux: {e}',
            'output': None
        }