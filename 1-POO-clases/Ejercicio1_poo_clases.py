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

    # Métodos, son acciones que hace el objeto (coche) (funciones)

    # MODIFICAR COLOR DEL COCHE CON SETCOLOR
    def setColor(self, color):
        self.color = color

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

# fin de definicion de clase

# instanciacion de clase

coche = Coche()
coche.setColor("Rojo")
coche.setModelo("Vizon")

print(coche.marca, coche.color)
print(f"Velocidad ACTUAL del coche {coche.marca} {coche.getModelo()}: {coche.getVelocidad()}")


coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(f"Velocidad del coche: {coche.getVelocidad()}")


#Crear mas objetos
coche2 = Coche()

print(" ")
print("######################################")
print(" ")

coche2.setModelo("Murcielago")
coche2.setColor("Amarillo")

print(f"Coche 2 {coche2.marca} {coche2.getModelo()} Color: {coche2.getColor()}")