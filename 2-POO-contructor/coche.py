# Programacion Orientada a Objetos
# Definir clase (molde para crear más objetos de ese tipo)

# (Coche) con caracteristicas similares
class Coche:
    # ATRIBUTOS O PROPIEDADES  (VARIABLES)
    # CARACTERISTICAS DEL COCHE
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    #propiedades publicas y privadas
    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #metodo para acceder a __soy_privado
    def getSoyPrivado(self):
        return self.__soy_privado
    # Métodos, son acciones que hace el objeto (coche) (funciones)

    # MODIFICAR COLOR DEL COCHE CON SETCOLOR
    def setColor(self, color):
        self.color = color

    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def setPlazas(self, plazas):
        self.plazas = plazas
        
    def getPlazas(self):
        return self.plazas

    # MOSTRAR MODELO DEL COCHE CON GETMODELO
    def getModelo(self):
        return self.modelo
    # MOSTRAR COLOR DEL COCHE CON GETCOLOR
    def getColor(self):
        return self.color

    # MODIFICAR MODELO DEL COCHE CON SETMODELO
    def setModelo(self, modelo):
        self.modelo = modelo

    # MOSTRAR MODELO DEL COCHE CON GETMODELO
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    
    def getInfo(self):
        informacion = "\n----------INFORMACION DEL COCHE-----------\n"
        informacion += "\nMARCA = " + self.getMarca()
        informacion += "\nMODELO = " + self.getModelo()
        informacion += "\nCOLOR = " + self.getColor()
        informacion += "\nVELOCIDAD = " + str(self.getVelocidad()) + "Km/h"
        informacion += "\nPLAZAS = " + str(self.getPlazas())
        
        return informacion

# fin de definicion de clase

# instanciacion de clase