### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4) # División flotante
print(10 % 3) # Módulo
print(10 // 3) # División entera
print(2 ** 3)  # Potencia
print(2 ** 3 + 3 - 7 / 1 // 4) # Precedencia de operadores

# Operaciones con cadenas de texto
print("Hola " + "Amigos " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5) # Repetición de cadenas
print("Hola " * (2 ** 3)) # Repetición de cadenas con potencia

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)


print("-------------------")

# Operaciones con cadenas de texto
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII

print(len("aaaa") >= len("abaa"))  # Cuenta caracteres

print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and 5 > 4)
print(3 < 4 or (5 != 6 and 4 == 4))
print(not (3 > 4))