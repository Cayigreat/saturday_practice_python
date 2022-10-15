import math

# Crear una funcion que imprima los numeros divisibles por tres hasta el numero n

def  divisibles_by_three(n):
    print("##############")
    for number in range(1, n + 1):
        if number % 3 == 0:
            print(number)          


divisibles_by_three(50)              
    

# Crear una funcion que sume todos los numeros hasta el n

def sum_up_to(n):
    acc = 0
    
    print("############")
    for number in range(1, n + 1):
        acc = acc + number
    print(acc)

# Otra forma abreviada de usar el acumulador es acc += number
print sum_up_to(20)

# Crear una funcion que calcule el volumen de una esfera de radio r

def ball_volume(r):
    volume = 4/3*math.pi*r**3
    return volume

result = ball_volume(15)
print(result)

# Crear una funcion que entregue el volumen de un cilindro de radio r y altura h

def cylinder_volume(r,h):
    volume = math.pi*r**2*h
    return volume

result = cylinder_volume(10,5)
print(result)    