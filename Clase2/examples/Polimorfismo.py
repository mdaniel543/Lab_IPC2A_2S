class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def introduccion(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carnet):
        super().__init__(nombre, edad)
        self.carnet = carnet

    def introduccion(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi número de carnet es {self.carnet}."


# Crear objetos de las clases Persona y Estudiante
persona = Persona('Ana', 35)
estudiante = Estudiante('Juan', 20, 'A12345678')

# Llamar al método introduccion en ambos objetos
print(persona.introduccion())
print(estudiante.introduccion())