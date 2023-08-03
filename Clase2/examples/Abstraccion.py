from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def introduccion(self):
        pass


class Estudiante(Persona):
    def __init__(self, nombre, edad, carnet):
        super().__init__(nombre, edad)
        self.carnet = carnet

    def introduccion(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi número de carnet es {self.carnet}")

class Maestro(Persona):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad)
        self.genero = genero
        
    def introduccion(self):
        print(f"Hola mi genero es {self.genero}")


# Crear un objeto de la clase Estudiante
estudiante = Estudiante('Juan', 20, 'A12345678')

# Llamar al método introduccion
estudiante.introduccion()

maestro1 = Maestro('Pedro', 15, 'M')

maestro1.introduccion()