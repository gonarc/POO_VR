import clases

persona = clases.Persona()
persona.setNombre("Javier")
persona.setApellido("Arce")
persona.setAltura("1.70 m")
persona.setEdad("29")

print(f"\nLa persona es {persona.getNombre()} {persona.getApellido()}, mide {persona.getAltura()} y tiene {persona.getEdad()} años de edad.\n")

informatico = clases.Informatico()
informatico.setNombre("Gonzalo")
informatico.setApellido("Arce")
informatico.setAltura("1.93 m")
informatico.setEdad("25")

print(f"\nEl informatico es {informatico.getNombre()} {informatico.getApellido()}, mide {informatico.getAltura()} y tiene {informatico.getEdad()} años de edad. tiene conocimientos en los lenduajes {informatico.getLenguajes()} con una experiencia de {informatico.experiencia} años. \n")


tecnicoRedes = clases.TecnicoRedes()
tecnicoRedes.setNombre("Armando")

print(f"Soy el tecnico en redes {tecnicoRedes.getNombre()} y tengo {tecnicoRedes.experienciaRedes} de experiencia. y sé {tecnicoRedes.getLenguajes()}")

#No puedo acceder a getlenguajes porque la informacion está en el constructor de la clase,
#para poder acceder se utiliza super()__init__() esto va en la clase TecnicoRedes())

#Lo hic y fuciono !
