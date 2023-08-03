from Auto import Auto

class AutoDeportivo(Auto):
    def __init__(self, marca, modelo, color, max_velocidad):
        super().__init__(marca, modelo, color)
        self._max_velocidad = max_velocidad

    def arrancar(self):
        print(f"El auto no arranca")

    def turbo(self):
        if self.estado == 'arrancado':
            self.velocidad = self._max_velocidad
            print(f"El auto deportivo {self.marca} {self.modelo} está usando turbo y su velocidad ahora es {self.velocidad} km/h")
        else:
            print("Primero debes arrancar el auto")