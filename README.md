<h1 align="center">MIM Audit</h1>
<p align="center"><img src="images/logo.png"/></p> 

## Tabla de contenidos:
---

- [Descripció i context](#descripció-i-context)
- [Fet amb](#fet-amb)
- [Prerequeriments](#prerequeriments)
- [Guía de instalació](#guía-de-instalació)
- [Guía de usuari](#guía-de-usuari)
- [Codi de conducta](#codi-de-conducta)
- [Autor/es](#autores)
- [Licencia](#licencia)


## Descripció i context
---

Som un grup d'estudiants del IES Ebre. El nostre projecte (MIM Audit) es una eina que pot realitzar una auditoría a un host o xarxa. 

Funcionalitats principals
* Shodan API
* The Harvester
* Escaneo (Nmap)
* Auditoria SSH
* Enum4linux
* Enviar els resultats a Telegram
* Imatge del contenedor docker

## Fet amb

<p align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" width="200">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" width="200">
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequeriments
---
* Instal·lació de python i altres requeriments.

    ```
    pip install -r requirements.txt
    ```
 	
## Guía de instalació
---
1. Clona aquest repositori a la teva màquina local:
    ```
    git clone https://github.com/IsaacAndreu/MIM-Audit
    ```
2. Entra al directori del projecte:
    ```
    cd MIM-Audit
    ```
3. Instal·la les dependencies necessaries:
    ```
    pip install -r requeriments.txt
    ```

## Guía de usuari
---
Benvinguts a la secció d'ús de la nostra eina de auditoria. Aquí us guiarem a través dels passos bàsics per utilitzar les diferents eines disponibles a la nostra aplicació.

### Menú principal
En aquesta pantalla hi trobareu un menú amb les diverses eines de auditoria com Shodan API, The Harvester, Escaneo(Nmap), Auditoria SSH i Escaneo (Enum4Linux)

<p align="center">
  <img src="images/MenuPrincipal.png" alt="menuprincipal" width="40%">
</p>

### Instruccions generals
Cada eina té una secció on podeu introduir la IP o URL que volveu analitzar. Algunes eines tenen una barra de selecció perquè pugueu triar entre diferents funcions. Assegureu-vos de proporcionar la informació correcta abans de procedir.

### Shodan API
Comencem amb Shodan API. Introduïu la IP o URL a la barra corresponent. Podeu triar diferents opcions de cerca mitjançant la barra de selecció. Un cop fet, feu clic a "Enviar" i espereu els resultats a la part inferior. 

<p align="center">
  <img src="images/ShodanAPI.png" alt="shodanapi" width="40%">
</p>

### The Harvester
Amb The Harvester, introduïu la IP o URL desitjada i seleccioneu les opcions necessàries. Cliqueu "Executar The Harvester" per iniciar l'eina. Els resultats hi tarden uns 3 o 5 mins en mostrarse a la part inferior de la pàgina.

<p align="center">
  <img src="images/TheHarvester.png" alt="TheHarvester" width="40%">
</p>

### Escaneig (Nmap)
Amb Nmap primer elegiu una de les opcions, una vegada fet aixo introduïu la IP o nom del host que voleu escanejar i trieu les opcions de l'escaneig. Cliqueu a "Enviar" per iniciar el procés. Els resultats es mostraran sota la barra d'opcions

<p align="center">
  <img src="images/Nmap.png" alt="nmap" width="40%">
</p>

### Auditoria SSH
En aquesta secció, primer elegiu una de les opcions, una vegada fet aixo introduïu la IP o host corresponen a la màquina amb la qual voleu realitzar l'auditoria SSH. Cliqueu a "Iniciar Auditoria". Els resultats apareixeran a sota.

<p align="center">
  <img src="images/MenuSSH.png" alt="menussh" width="40%">
</p>

### Escaneig (Enum4Linux)
Per a l'escaneig amb Enum4Linux, introduïu la IP i cliqueu a "Iniciar Escaneig". Els resultats estaran disponibles a la part inferior.

<p align="center">
  <img src="images/Enum4Linux.png" alt="enum4linux" width="40%">
</p>

### Resultats
Després de completar cada anàlisi, veureu els resultats a la part inferior de la pàgina. Teniu un botó per esborrar els resultats si cal, i també un botó per enviar-los via Telegram.

### Suport tècnic
No dubteu a explorar les diferents eines i funcions per millorar la vostra auditoria. Si teniu algun dubte, consulteu la nostra secció de preguntes freqüents o poseu-vos en contacte amb el nostre suport tècnic. Gràcies per confiar en la nostra plataforma.


## Codi de conducta
---
Podeu trobar el codi de conducta al següent link: https://github.com/IsaacAndreu/MIM-Audit?tab=coc-ov-file

## Autor/es
---
Marc Queral - (https://github.com/MarcQueral)

Isaac Andreu - (https://github.com/IsaacAndreu)

Max Segura - (https://github.com/MaxSegura)

Link del projecte: [https://github.com/IsaacAndreu/MIM-Audit]

## Licencia 
---

La licencia especifica los permisos y las condiciones de uso que el desarrollador otorga a otros desarrolladores que usen y/o modifiquen la herramienta digital.

Incluye en esta sección una nota con el tipo de licencia otorgado a esta herramienta digital. El texto de la licencia debe estar incluído en un archivo *LICENSE.md* o *LICENSE.txt* en la raíz del repositorio.

Si desconoces qué tipos de licencias existen y cuál es la mejor para cada caso, te recomendamos visitar la página https://choosealicense.com/.

Si la herramienta que estás publicando con la iniciativa Código para el Desarrollo ha sido financiada por el BID, te invitamos a revisar la [licencia oficial del banco para publicar software](https://github.com/EL-BID/Plantilla-de-repositorio/blob/master/LICENSE.md)

