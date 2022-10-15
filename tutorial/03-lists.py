import math

squares = [1,4,9,16,25]

#Desafío: a partir del arreglo anterior crear uno que tenga sus raíces
# roots == 'raiz' 

roots = []

##Otra forma sin math 
#for number in squares:
    #roots.append(int(number**(1/2))##

for number in squares:
    roots.append(int(math.sqrt(number)))

print(roots)   

##sqrt = sqrt o raiz cuadrada 
## square: sq
## root: rt

## append: agrega al final , porque en este caso es mas de un resultado el que debe mostrarse

## Reemplazar algun elemento del arreglo segun el indice
roots[4] = 6

print(roots)