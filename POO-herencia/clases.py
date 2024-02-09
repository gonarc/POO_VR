#HERENCIA: es la posibilida de compartir atributos y métodos
# Entre clases. Y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    apellidos
    altura
    edad
    
    """
    #SETS
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad
    
    #GETS
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    #actividades
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    
    def hablar(self):
        return "Estoy hablando"
    
class Informatico(Persona):
    """lenguajes
    experiencia"""
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, JAVASCRIP, PYTHON"
        self.experiencia = 6
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPc(self):
        return "He reparado tu computadora"
    
class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditorRedes = "Experto"
        self.experienciaRedes = 10
        
    def auditoria(self):
        return "Estoy auditando una red"
    
    
    