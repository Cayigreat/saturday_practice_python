import math

#Crear una función que calcule el volumen de una esfera de radio r

 

def ball_volume(r):
    volume =4/3*math.pi*r**3
    return volume

result = ball_volume(15)
print(result)