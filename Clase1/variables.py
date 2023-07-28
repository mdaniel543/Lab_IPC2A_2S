### Variables ###

my_string = "Bienvenidos a IPC2"
print(my_string)

my_int = 5
print(my_int)

my_int_to_str = str(my_int)
print(my_int_to_str)

print(type(my_int_to_str))

my_bool = False
print(my_bool)

# Concatenación de variables en un print
print(my_string, my_int_to_str, my_bool)
print("Este es el valor de:", my_bool)

# Algunas funciones del sistema
print(len(my_string))

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print("Me llamo:", name, ". Mi edad es:", age )

# Cambiamos su tipo
name = 15
age = "Mi edad"
print(name)
print(age)

address = "Mi dirección"
print(type(address))
address = True
address = 5
address = 1.2
print(type(address))