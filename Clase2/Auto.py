class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estado = 'parado'
        self.velocidad = 0

    def arrancar(self):
        self.estado = 'arrancado'
        print(f"El auto {self.marca} {self.modelo} de color {self.color} está arrancando")

    def acelerar(self):
        if self.estado == 'arrancado':
            self.velocidad += 10
            print(f"El auto {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h")
        else:
            print("Primero debes arrancar el auto")

    def frenar(self):
        if self.estado == 'arrancado':
            self.velocidad = 0  # Al frenar la velocidad se reduce a 0
            self.estado = 'parado'  # Al frenar el auto pasa a estado 'parado'
            print(f"El auto {self.marca} {self.modelo} está frenando y su velocidad ahora es {self.velocidad} km/h")
        else:
            print("El auto ya está parado")