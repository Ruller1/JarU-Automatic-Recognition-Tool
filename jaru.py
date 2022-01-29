
#---------------------------------------------------------------
#                 Herramienta creada por:                      |
#               (RullerTheOne y JaggedMule14)                  |
#                                                              |
#        El fin de esta herramienta es para uso etico          |
#     cualquier accion ilicita quedará en manos del usuario.   |
#                                                              |
#---------------------------------------------------------------


# Pregunta Y respuesta Nmap - wfuzz - dirbuster - etc

import sys,os

ipvictima = input("Introduce la Ip victima")
mododeescaneo = int(input("Introduce el modo de escaneo: 1-Muy Agresivo Velocidad:rapido, \n2-Agresivo Velocidad:Medio \n3-Tranquilo pero no tanto Velocidad:medio \n4-Tranquilo-Velocidad:Lento \n5-Muy tranquilo Velocidad:Muy Lento"))

def muyagresivo():
    os.system('nmap -p- --open --min-rate 7000 -sCV -Pn $ipvictima -oG allports')

def agresivo():
    os.system('nmap -p- --open -T5 -sCV $ipvictima -oG allports') 

def tranquilomedio():
    os.system('nmap -p- --open -sV -T3 $ipvictima -oG allports')

def muytranquilo():
    os.system('nmap -T1 --open -sV $ipvictima -oG allports')

def sigiloso():
    os.system('nmap -p- --open -T0 -v $ipvictima -oG allports')


if mododeescaneo == 1:
    print("Iniciando escaneo muy agresivo..., abstente a las consecuencias")
    muyagresivo()
elif mododeescaneo == 2:
    print("Iniciando escaneo agresivo..., ¿te gusta el ruido?, ¿eres un espartano?")
    agresivo()
elif mododeescaneo == 3:
    print("Iniciando escaneo medio.., no te gusta tanto el ruido eh, ¿tienes miedo?")
    tranquilomedio()
elif mododeescaneo == 4:
    print("Iniciando escaneo tranquilo..., chicos.. vengan encontramos a un pusilánime")
elif mododeescaneo == 5:
    print("Iniciando escaneo muy tranquilo..., ¿si eres tan cagón para que me usas? ;(")
