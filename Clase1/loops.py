### Loops ###

# While

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2

else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)


print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

for i in range(len(my_list)):
    print(my_list[i])
