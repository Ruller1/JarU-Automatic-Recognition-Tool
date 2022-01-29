#---------------------------------------------------------------
#                 Herramienta creada por:                      |
#               (RullerTheOne y JaggedMule14)                  |
#                                                              |
#        El fin de esta herramienta es para uso etico          |
#     cualquier accion ilicita quedará en manos del usuario.   |
#                                                              |
#---------------------------------------------------------------

###-Pregunta Y respuesta Nmap - wfuzz - dirbuster - etc-###

from sqlite3 import adapt
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
print(f'''{Fore.RED} _  | |/ _` | '__| | | | {Fore.LIGHTBLUE_EX}(Creado por RullerTheOne - JaggedMule14)''')
time.sleep(0.1)
print(f'{Fore.CYAN}| |_| | (_| | |  | |_| |')
time.sleep(0.1)
print(f'{Fore.BLUE} \___/ \__,_|_|   \___/ \n')
time.sleep(0.1)
print(f'{Fore.RED}\n[!]\nEJECUTAR COMO ROOT')
victimIP = input(f"{Fore.CYAN}\n[+]Introduce la IP victima: ")
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

scanMode = int(input(f'{Fore.CYAN}\n[+]Elige tu modo de escaneo: '))
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

formato = int(input(f'{Fore.CYAN}\n[+]¿En qué formato deseas exportar?: '))

###-Funciones-###

def conect():
    ping = os.system(f'ping -c 1 {victimIP} >/dev/null 2>&1')
    if ping == 0:
        return True
    else:
        return False


###-Muy Agresivo-###
def muyagresivogrep():
        os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def muyagresivonormal():
        os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {victimIP} -oN allports')
        sys.exit(0)
def muyagresivoxml():
        os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {victimIP} -oX allports')
        sys.exit(0)
def muyagresivosk():
        os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {victimIP} -noob allports') ##No me se la salida de noobs ; )
        sys.exit(0)
def muyagresivo():
    os.system(f'nmap -p- --open -sS --min-rate 5000 -sCV -n -Pn {victimIP}')
    sys.exit(0)




###-Agresivo-###
def agresivogrep():
        os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def agresivonormal():
        os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn {victimIP}  -oN allports')
        sys.exit(0)
def agresivoxml():
        os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn  {victimIP} -oX allports')
        sys.exit(0)
def agresivosk():
        os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn  {victimIP} -noob allports') ##No me se la salida de noobs ; )
        sys.exit(0)
def agresivo():
    os.system(f'nmap -p- -sS --open -T5 -sCV -n -Pn  {victimIP}')
    sys.exit(0)

    
###-Tranquilo Medio-###
def tranquilomediogrep():
        os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def tranquilomediogrep():
        os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def tranquilomedionormal():
        os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP}  -oN allports')
        sys.exit(0)
def tranquilomedioxml():
        os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP} -oX allports')
        sys.exit(0)
def tranquilomediosk():
        os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP} -noob allports') ##No me se la salida de noobs ; )
        sys.exit(0)
def tranquilomedio():
    os.system(f'nmap -p- -sS --open -sV -T3 -n -Pn {victimIP}')
    sys.exit(0)

   
###-Muy Tranquilo-###
def muytranquilogrep():
        os.system(f'nmap -T1 -sS --open -sV -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def muytranquilonormal():
        os.system(f'nmap -T1 -sS --open -sV -n -Pn {victimIP}  -oN allports')
        sys.exit(0)
def muytranquiloxml():
        os.system(f'nmap -T1 -sS --open -sV -n -Pn {victimIP} -oX allports')
        sys.exit(0)
def muytranquilosk():
        os.system(f'nmap -T1 -sS --open -sV -n -Pn {victimIP} -noob allports') ##No me se la salida de noobs ; )
        sys.exit(0)
def muytranquilo():
    os.system(f'nmap -T1 -sS --open -sV -n -Pn {victimIP}')
    sys.exit(0)
  
###-Sigiloso-###
def sigilosogrep():
        os.system(f'nmap -p- -sS --open -T0 -n -Pn {victimIP} -oG allports')
        sys.exit(0)
def sigilosonormal():
        os.system(f'nmap -p- -sS --open -T0 -n -Pn {victimIP}  -oN allports')
        sys.exit(0)
def sigilosoxml():
        os.system(f'nmap -p- -sS --open -T0 -n -Pn {victimIP} -oX allports')
        sys.exit(0)
def sigilososk():
        os.system(f'nmap -p- -sS --open -T0 -n -Pn {victimIP} -noob allports') ##No me se la salida de noobs ; )
        sys.exit(0)
def sigiloso():
    os.system(f'nmap -p- -sS --open -T0 -n -Pn {victimIP}')
    sys.exit(0)

###-Grep Recon-###
if conect() == True and scanMode == 1 and formato == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Formato grepeable seleccionado")
    muyagresivogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 2 and formato == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?\n[!]Formato grepeable seleccionado")
    agresivogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 3 and formato == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo medio..., no te gusta tanto el ruido eh, ¿tienes miedo?\n[!]Formato grepeable seleccionado")
    tranquilomediogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 4 and formato == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo tranquilo..., ¿un niñito jugando con fuego?, ten cuidado, te puedes quemar..\n[!]Formato grepeable seleccionado")
    muytranquilogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')


if conect() == True and scanMode == 5 and formato == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo sigiloso..., ¿si eres tan cagón para que me usas?\n[!]Formato grepeable seleccionado")
    sigilosogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

###-Formato Normal recon-###
if conect() == True and scanMode == 1 and formato == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Formato grepeable seleccionado")
    muyagresivonormal()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 2 and formato == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?\n[!]Formato grepeable seleccionado")
    agresivonormal()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')
if conect() == True and scanMode == 3 and formato == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo medio..., no te gusta tanto el ruido eh, ¿tienes miedo?\n[!]Formato grepeable seleccionado")
    tranquilomediogrep()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 4 and formato == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo tranquilo..., ¿un niñito jugando con fuego?, ten cuidado, te puedes quemar..\n[!]Formato grepeable seleccionado")
    muytranquilonormal()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 5 and formato == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy tranquilo..., ¿si eres tan cagón para que me usas? \n[!]Formato grepeable seleccionado")
    sigilosonormal()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

###-Formato XML recon-###
if conect() == True and scanMode == 1 and formato == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Formato grepeable seleccionado")
    muyagresivoxml()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 2 and formato == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?\n[!]Formato grepeable seleccionado")
    agresivoxml()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 3 and formato == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo tranquilo..., ¿un niñito jugando con fuego?, ten cuidado, te puedes quemar..\n[!]Formato grepeable seleccionado")
    tranquilomedioxml()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')


if conect() == True and scanMode == 4 and formato == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Formato grepeable seleccionado")
    muytranquiloxml()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 5 and formato == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo sigiloso..., ¿si eres tan cagón para que me usas?\n[!]Formato grepeable seleccionado")
    sigilosoxml()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

###- Formato Noob - ###
if conect() == True and scanMode == 1 and formato == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Formato grepeable seleccionado")
    muyagresivosk()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')


if conect() == True and scanMode == 2 and formato == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?\n[!]Formato grepeable seleccionado")
    agresivosk()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 3 and formato == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo medio..., no te gusta tanto el ruido eh, ¿tienes miedo?\n[!]Formato grepeable seleccionado")
    tranquilomediosk()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 4 and formato == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo tranquilo..., ¿un niñito jugando con fuego?, ten cuidado, te puedes quemar..\n[!]Formato grepeable seleccionado")
    muytranquilosk()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 5 and formato == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo sigiloso..., ¿si eres tan cagón para que me usas?\n[!]Formato grepeable seleccionado")
    sigilososk()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 1:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo muy agresivo..., abstente a las consecuencias\n[!]Ningún Formato Seleccionado")
    muyagresivo()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 2:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?\n[!]Ningún Formato Seleccionado")
    agresivo()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 3:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo medio..., no te gusta tanto el ruido eh, ¿tienes miedo?\n[!]Ningún Formato Seleccionado")
    tranquilomedio()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 4:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo tranquilo..., ¿un niñito jugando con fuego?, ten cuidado, te puedes quemar..\n[!]Ningún Formato Seleccionado")
    muytranquilo()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')

if conect() == True and scanMode == 5:
    print(f'{Fore.GREEN}\n[+]Conexión con {victimIP} exitosa')
    print(f"{Fore.RED}\nIniciando escaneo sigiloso..., ¿si eres tan cagón para que me usas? \n[!]Ningún Formato Seleccionado")
    sigiloso()
else:
    print(f'{Fore.RED}[-]Conectividad con la máquina fallida')




