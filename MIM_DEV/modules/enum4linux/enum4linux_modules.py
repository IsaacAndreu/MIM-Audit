import subprocess

def run_enum4linux(target):
    command = f'enum4linux -a -A -U -S -P {target}'
    try:
        subprocess.run(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar enum4linux: {e}')