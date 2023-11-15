import random

class Persona():
    def __init__(self, id):

        #Parámetros para crear la persona
        listaNombres = ["Juan", "Jose", "Daniel", "Alejandro", "Tomas", "Roberto", "Carlos", "Miguel", "David", "Ricardo", "Wilmer", "Agustin", "Mateo", "Pablo", "Andres", "German", "Mario", "Luis"]
        listaApellidos = ["Char", "Diaz", "Carmona", "Cardona", "Duque", "Rodriguez", "Lopez", "Restrepo", "Salinas", "Ospina", "Acevedo", "Roldan", "Cadavid", "Perez", "Sanchez", "Cifuentes", "Gutierrez" ]

        #Atributos de una persona
        self.nombre = f'{random.choice(listaNombres)} {random.choice(listaApellidos)}'
        self.id = id
        self.mensajesRecibidos = []
        self.mensajesEnviados = []
        self.amigos = []

    def __str__(self):
        return f'Nombre: {self.nombre}, ID: {self.id}, Mensajes Recibidos: {self.mensajesRecibidos}, Mensajes Enviados: {self.mensajesEnviados}, Amigos: {len(self.amigos)}'