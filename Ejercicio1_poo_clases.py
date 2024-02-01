#Programacion Orientada a Objetos
#Definir clase (molde para crear más objetos de ese tipo)

#(Coche) con caracteristicas similares
class Coche:
     #ATRIBUTOS O PROPIEDADES  (VARIABLES)
     #CARACTERISTICAS DEL COCHE
    color = "Rojo"
    marca="Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    #Métodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):
        self.velocidad += 1
        
    def frenar (self):
        self.velocidad -= 1
        
    def getVelocidad (self):
        return self.velocidad
    
#fin de definicion de clase

#instanciacion de clase

coche = Coche()
print(coche.marca, coche.color)
print(f"Velocidad ACTUAL del coche: {coche.velocidad}")


coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(f"Velocidad del coche: {coche.velocidad}")

        