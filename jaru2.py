#---------------------------------------------------------------
#                 Herramienta creada por:                      |
#               (RullerTheOne y JaggedMule14)                  |
#                                                              |
#        El fin de esta herramienta es para uso etico          |
#     cualquier accion ilicita quedará en manos del usuario.   |
#                                                              |
#---------------------------------------------------------------

###-Pregunta Y respuesta Nmap - wfuzz - dirbuster - etc-###

import sys
import os
from colorama import init,Fore,Style
import time
import signal

def def_handler(sig, frame):
    print(f'{Fore.RED}\n[-]Exit')
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

print(f'{Fore.GREEN}     _            _   _ ')
time.sleep(0.1)
print(f'{Fore.YELLOW}    | | __ _ _ __| | | |')
time.sleep(0.1)
print(f'''{Fore.RED} _  | |/ _` | '__| | | |''')
time.sleep(0.1)
print(f'{Fore.CYAN}| |_| | (_| | |  | |_| |')
time.sleep(0.1)
print(f'{Fore.BLUE} \___/ \__,_|_|   \___/ \n')
time.sleep(0.1)
print(f'{Fore.RED}[!]EJECUTAR COMO ROOT')
VictimIP = input(f"{Fore.CYAN}\n[+]Introduce la IP victima: ")
print(f'\n{Fore.MAGENTA}[+]Modos de escaneo (1 al 5)')
time.sleep(0.1)
print(f'{Fore.RED}1.- Muy Agresivo || Velocidad:Rapido')
time.sleep(0.1)
print(f'{Fore.RED}2.- Agresivo || Velocidad:Media Alta')
time.sleep(0.1)
print(f'{Fore.YELLOW}3.- Moderado || Velocidad:Media')
time.sleep(0.1)
print(f'{Fore.GREEN}4.- Leve || Velocidad:Media Baja')
time.sleep(0.1)
print(f'{Fore.GREEN}5.- Muy Leve || Velocidad:Baja')
ScanMode = int(input(f'{Fore.CYAN}\n[+]Elige tu modo de escaneo: '))
print(f'{Fore.MAGENTA}\n[+]Formatos')
time.sleep(0.1)
print(f'{Fore.RED}1.- Formato Grepeable || extractPorts para copiar puertos')
time.sleep(0.1)
print(f'{Fore.YELLOW}2.- Formato Normal || cat de toda la vida para leer')
time.sleep(0.1)
print(f'{Fore.GREEN}3.- Formato XML || Interpretación en http')
time.sleep(0.1)
print(f'{Fore.BLUE}4.- s4L1d4 sCRiPt KiDDi3 || No me la conteiner que sos Script Kiddie')
time.sleep(0.1)
print(f'{Fore.YELLOW}5.- No quiero exportar una pija || No exportar')
Formato = input(f'{Fore.CYAN}\n[+]¿En qué formato deseas exportar?: ')

###-Funciones-###

def conect():
    ping = os.system(f'ping -c 1 {VictimIP} >/dev/null 2>&1')
    if ping == 0:
        return True
    else:
        return False

def muyagresivo():
    os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {VictimIP} -oG allports')

def agresivo():
    os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn {VictimIP} -oG allports') 

def tranquilomedio():
    os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {VictimIP} -oG allports')

def muytranquilo():
    os.system(f'nmap -T1 -sS --open -sV -n -Pn {VictimIP} -oG allports')

def sigiloso():
    os.system(f'nmap -p- -sS --open -T0 -n -Pn {VictimIP} -oG allports')

if conect() == True:
    print(f'{Fore.GREEN}[+]Conexión con {VictimIP} exitosa')
    if ScanMode == 1:
        print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias")
        muyagresivo()
    elif ScanMode == 2:
        print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?")
        agresivo()
    elif ScanMode == 3:
        print(f"{Fore.YELLOW}\nIniciando escaneo medio..., no te gusta tanto el ruido eh, ¿tienes miedo?")
        tranquilomedio()
    elif ScanMode == 4:
        print(f"{Fore.GREEN}\nIniciando escaneo tranquilo..., chicos.. vengan encontramos a un pusilánime")
        muytranquilo()
    elif ScanMode == 5:
        print(f"{Fore.GREEN}\nIniciando escaneo muy tranquilo..., ¿si eres tan cagón para que me usas? ;(")
        sigiloso()
    else:
        print(f'{Fore.RED}[-]Elige un número del 1 al 5')
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')
