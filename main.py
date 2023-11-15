from Persona import *
from Lista import *

import random

#Método para obtener un mensaje aleatorio
def obtenerMensaje():
  mensajes = ["Hola", "¿Cómo estás?", "Buenas", "¿Qué tal?", "Adiós", "Hasta luego", "Gracias", "Lo siento", "¿En qué puedo ayudarte?", "Ya voy para allá", "Gracias por la salida hoy!", "Te quiero!"]
  return random.choice(mensajes)

#Método para obtener una hora aleatoria
def obtenerHora():
  horas = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM","7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM","1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM","7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]
  return random.choice(horas)

#Método que genera los mensajes en la red y el historial de mensajes
def generarMensajes(personas, historialMensajes, limiteMensajes, numMensajes = 0):
  while numMensajes < limiteMensajes:
    remitente = random.choice(personas)
    destinatario = random.choice(personas)
    mensaje = obtenerMensaje()
    hora = obtenerHora()
    Datos = Data(remitente.id, destinatario.id, hora, mensaje)

    if remitente != destinatario:
      # Asegurarse que un remitente envie varios mensajes a un mismo destinatario
      for _  in range(random.randint(1, 5)):
        print(f"{remitente.nombre} ({remitente.id}) envía a {destinatario.nombre} ({destinatario.id}):")
        print(f"  Mensaje: {mensaje}")
        print(f"  Hora: {hora}")
        print("-" * 30)
        historialMensajes.insertar(Datos)
        numMensajes += 1
        
#Método que analiza el historial de mensajes
def analizarHistorial(listaPersonas, historialMensajes):

  actual = historialMensajes.first
  while actual:
    remitente = actual.data.remitente
    destinatario = actual.data.destinatario
    listaPersonas[remitente-1].mensajesEnviados.append(actual.data.destinatario)
    listaPersonas[destinatario-1].mensajesRecibidos.append(actual.data.remitente)
    actual = actual.siguiente
  
  definirAmigos(listaPersonas)
    
#Método que define los amigos de cada persona 
def definirAmigos(personas):
  for persona in personas:
    for amigo in set(persona.mensajesRecibidos):
      if persona.mensajesRecibidos.count(amigo) >= 3:
        personas[amigo - 1].amigos.append(persona.id)
        personas[persona.id - 1].amigos.append(amigo)
       
#Método que muestra los amigos de cada persona 
def mostrarAmigos(personas):
  for persona in personas:
    if persona.amigos:
      amigosConNombre = [f"{amigoId} ({personas[amigoId - 1].nombre})" for amigoId in persona.amigos]
      print(f"{persona.nombre} es amigo de Id: {', '.join(amigosConNombre)}")
    else:
      print(f"{persona.nombre} no tiene amigos :(")

#Método que muestra la persona con más amigos 
def personasConMasAmigos(personas):
  personaConMasAmigos = personas[0]
  for persona in personas:
    if len(persona.amigos) > len(personaConMasAmigos.amigos):
      personaConMasAmigos = persona
      
  print(f"\n{personaConMasAmigos.nombre} tiene más amigos ({len(personaConMasAmigos.amigos)})")
      
#Método que muestra la relación más fuerte
def relacionMasFuerte(personas):
  parejaMasFuerte = None
  cantidadMensajes = 0

  for persona in personas:
    for amigoId in persona.amigos:
      cantidadEnviados = persona.mensajesEnviados.count(amigoId)
      cantidadRecibidos = persona.mensajesRecibidos.count(amigoId)
      mensajesTotales = cantidadEnviados + cantidadRecibidos

      if mensajesTotales > cantidadMensajes:
        cantidadMensajes = mensajesTotales
        parejaMasFuerte = [persona.id, amigoId]

  if parejaMasFuerte:
    persona1 = personas[parejaMasFuerte[0] - 1].nombre
    persona2 = personas[parejaMasFuerte[1] - 1].nombre
    print(f"La relación más fuerte es entre {persona1} ({parejaMasFuerte[0]}) y {persona2} ({parejaMasFuerte[1]}).")
    print(f"Tienen un total de {cantidadMensajes} mensajes intercambiados.")
        
if __name__ == '__main__':

  #Variables Globales
  limitePersonas = 20
  numMensajes = 0
  historialMensajes = Lista()

  #Crear personas
  personas = []
  for i in range(limitePersonas):
    personas.append(Persona(i+1))

  # Simular que cada persona envía un mensaje a otra persona en la red (exactamente 50 mensajes)
  generarMensajes(personas, historialMensajes, 50)

  #Analizar el historial de mensajes
  analizarHistorial(personas, historialMensajes)

  #Mostrar el historial de mensajes
  print("HISTORIAL DE MENSAJES:")
  print("=" * 100)
  historialMensajes.mostrar()
  
  #Imprimir los datos de las personas después de hacer el análisis
  print("\n")
  print("DATOS DE LAS PERSONAS")
  print("=" * 100)
  for persona in personas:
    print(persona)
  
  #Imprimir quien es amigo de quien
  print("\n")
  print("AMIGOS:")
  print("=" * 100)
  mostrarAmigos(personas)

  #Imprimir la persona con más amigos
  print("\n")
  print("PERSONA CON MÁS AMIGOS:")
  print("=" * 100)
  personasConMasAmigos(personas)
  
  #Imprimir la relacion mas fuerte
  print("\n")
  print("RELACIÓN MÁS FUERTE:")
  print("=" * 100)
  relacionMasFuerte(personas)


    
        