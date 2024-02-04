from coche import Coche

# Crear instancias con diferentes valores
carro_verde = Coche("verde", "Toyota", "Corolla", 150, 180, 4)
carro_rojo = Coche("rojo", "Ford", "Focus", 140, 160, 4)
carro_azul = Coche("azul", "Honda", "Civic", 160, 200, 4)
carro_negro = Coche("negro", "Chevrolet", "Malibu", 155, 190, 4)
carro_rosado = Coche("rosado", "Nissan", "Sentra", 145, 170, 4)

# print(f"{carro.marca} {carro.getModelo()} {carro.getColor()} {carro.getVelocidad()}km/h")

print(carro_verde.getInfo())
print(carro_rojo.getInfo())
print(carro_rosado.getInfo())
print(carro_negro.getInfo())
print(carro_azul.getInfo())