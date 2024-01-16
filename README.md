

*Esta herramienta digital forma parte del catálogo de herramientas del **Banco Interamericano de Desarrollo**. Puedes conocer más sobre la iniciativa del BID en [code.iadb.org](https://code.iadb.org)*

<h1 align="center">MIM Audit</h1>
<p align="center"><img src="images/logo.png"/></p> 

## Tabla de contenidos:
---

- [Descripció i context](#descripción-y-contexto)
- [Fet amb](#fet-amb)
- [Prerequeriments](#prerequeriments)
- [Guía de instalació](#guía-de-instalación)
- [Guía de usuari](#guía-de-usuario)
- [Código de conducta](#código-de-conducta)
- [Autor/es](#autores)
- [Licencia](#licencia)
- [Limitación de responsabilidades - Solo BID](#limitación-de-responsabilidades)


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

    '''sh
    pip install -r requirements.txt
    '''
 	
## Guía de instalación
---
1. Clona aquest repositori a la teva màquina local:
    '''sh
    git clone https://github.com/IsaacAndreu/MIM-Audit
    '''
2. Entra al directori del projecte:
    '''sh
    cd MIM-Audit
    '''
3. Instal·la les dependencies necessaries:
    '''sh
    pip install -r requeriments.txt
    '''

## Guia d'usuari
---
Benvinguts a la secció d'ús de la nostra eina de auditoria. Aquí us guiarem a través dels passos bàsics per utilitzar les diferents eines disponibles a la nostra aplicació.

### Menú principal
En aquesta pantalla hi trobareu un menú amb les diverses eines de auditoria com Shodan API, The Harvester, Escaneo(Nmap), Auditoria SSH i Escaneo (Enum4Linux)
<p align="left"><img src="images/MenuPrincipal.png></p> 

### Instruccions generals

Cada eina té una secció on podeu introduir la IP o URL que volveu analitzar. Algunes eines tenen una barra de selecció perquè pugueu triar entre diferents funcions. Assegureu-vos de proporcionar la informació correcta abans de procedir.

### Shodan API
Comencem amb Shodan API. Introduïu la IP o URL a la barra corresponent. Podeu triar diferents opcions de cerca mitjançant la barra de selecció. Un cop fet, feu clic a "Enviar" i espereu els resultats a la part inferior. 
<p align="left"><img src="images/ShodanAPI.png></p> 

### The Harvester
Amb The Harvester, introduïu la IP o URL desitjada i seleccioneu les opcions necessàries. Cliqueu "Executar The Harvester" per iniciar l'eina. Els resultats hi tarden uns 3 o 5 mins en mostrarse a la part inferior de la pàgina.
<p align="left"><img src="images/TheHarvester.png></p> 

### Escaneig (Nmap)
Amb Nmap primer elegiu una de les opcions, una vegada fet aixo introduïu la IP o nom del host que voleu escanejar i trieu les opcions de l'escaneig. Cliqueu a "Enviar" per iniciar el procés. Els resultats es mostraran sota la barra d'opcions
<p align="left"><img src="images/Nmap.png></p> 

### Auditoria SSH
En aquesta secció, primer elegiu una de les opcions, una vegada fet aixo introduïu la IP o host corresponen a la màquina amb la qual voleu realitzar l'auditoria SSH. Cliqueu a "Iniciar Auditoria". Els resultats apareixeran a sota.
<p align="left"><img src="images/MenuSSH.png></p> 

### Escaneo (Enum4Linux)
Per a l'escaneig amb Enum4Linux, introduïu la IP i cliqueu a "Iniciar Escaneig". Els resultats estaran disponibles a la part inferior.
<p align="left"><img src="images/Enum4Linux.png></p> 

### Resultats
Després de completar cada anàlisi, veureu els resultats a la part inferior de la pàgina. Teniu un botó per esborrar els resultats si cal, i també un botó per enviar-los via Telegram.

### Suport tècnic
No dubteu a explorar les diferents eines i funcions per millorar la vostra auditoria. Si teniu algun dubte, consulteu la nostra secció de preguntes freqüents o poseu-vos en contacte amb el nostre suport tècnic. Gràcies per confiar en la nostra plataforma.


## Código de conducta 
---
El código de conducta establece las normas sociales, reglas y responsabilidades que los individuos y organizaciones deben seguir al interactuar de alguna manera con la herramienta digital o su comunidad. Es una buena práctica para crear un ambiente de respeto e inclusión en las contribuciones al proyecto. 

La plataforma Github premia y ayuda a los repositorios dispongan de este archivo. Al crear CODE_OF_CONDUCT.md puedes empezar desde una plantilla sugerida por ellos. Puedes leer más sobre cómo crear un archivo de Código de Conducta (aquí)[https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/]

## Autor/es
---
Nombra a el/los autor/es original/es. Consulta con ellos antes de publicar un email o un nombre personal. Una manera muy común es dirigirlos a sus cuentas de redes sociales.

## Información adicional
---
Esta es la sección que permite agregar más información de contexto al proyecto como alguna web de relevancia, proyectos similares o que hayan usado la misma tecnología.

## Licencia 
---

La licencia especifica los permisos y las condiciones de uso que el desarrollador otorga a otros desarrolladores que usen y/o modifiquen la herramienta digital.

Incluye en esta sección una nota con el tipo de licencia otorgado a esta herramienta digital. El texto de la licencia debe estar incluído en un archivo *LICENSE.md* o *LICENSE.txt* en la raíz del repositorio.

Si desconoces qué tipos de licencias existen y cuál es la mejor para cada caso, te recomendamos visitar la página https://choosealicense.com/.

Si la herramienta que estás publicando con la iniciativa Código para el Desarrollo ha sido financiada por el BID, te invitamos a revisar la [licencia oficial del banco para publicar software](https://github.com/EL-BID/Plantilla-de-repositorio/blob/master/LICENSE.md)

## Limitación de responsabilidades
Disclaimer: Esta sección es solo para herramientas financiadas por el BID.

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.