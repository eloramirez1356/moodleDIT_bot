# -*- coding: utf-8 -*-

# Importamos el módulo de pyTelegramBotAPI
import telebot

# Creamos el bot. Sustituir <TOKEN> con el token de nuestro bot
bot = telebot.TeleBot('291268198:AAEi357SYSvAVOOrUAofCDr5AGxEHrV623I')


# Para almacenar los usuarios dentro de nuestro programa,
# usaremos una lista
usuarios = list()
# Después, abriremos el fichero y por cada linea, iremos
# insertando en nuestra lista el ID
for linea in open('usuarios.txt','r'):
    # El fichero contiene texto, pero nosotros queremos números
    # por lo que transformaremos cada línea a un número entero.
    id = int(linea)
    # Y lo insertaremos en nuestra lista de usuarios
    usuarios.append(id)


# Así le indicamos cómo manejar el comando '/start'
@bot.message_handler(commands=['start'])
def command_start(m):
    # En primer lugar, guardaremos en una variable el id de la
    # conversación a la que debe dirigirse
    cid = m.chat.id
    # Comprobamos que el ID no esté en nuestros usuarios.
    if cid not in usuarios:
        # Con from_user obtenemos información del usuario
        # y con first_name, su nombre.
        nombre = m.from_user.first_name
        # A continuación indicamos qué debe decir el bot.
        bot.send_message(cid, "Bievenido a este bot de pruebas <i>" + nombre + "</i>!", parse_mode="HTML")
        # Y lo guardamos como usuario tan to en la variable
        # como en el fichero
        usuarios.append(cid)
        with open('usuarios.txt','a') as f:
            f.write(str(cid)+'\n')
    # Si ya es usuario, le avisamos
    else:
        bot.send_message(cid, "Ya eras usuario!")




# Declaramos una función que hará de listener. Todos los mensajes
# recibidos por el bot pasarán por esta función.
#def listener(messages):
#    for m in messages:
# Comprobamos que el mensaje recibido sea de texto
#        if m.content_type == 'text':
# Y le respondemos con el texto propio del mensaje recibido.
#            bot.reply_to(m, m.text)

# Una vez creado el listener, debemos asignárselo al bot.
# bot.set_update_listener(listener)

# Por útlimo, hacemos el long-poll, es decir, le decimos al bot que empiece a leer los mensajes que el bot reciba.
bot.polling(True)