class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero")
        self.__edad = edad

# Crear un objeto de la clase Persona
persona = Persona('Ana', 35)

# Modificar los atributos a través de los métodos setter
persona.nombre = 'Juan'
persona.edad = 36

# Acceder a los atributos a través de los métodos getter
print(persona.nombre)
print(persona.edad)
