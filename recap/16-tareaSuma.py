# Crear una funcion que sume todos los numeros hasta el n

def sum_up_to(n):
    acc = 0

    for number in range(1, n + 1):
        acc += number
    print(acc)    

sum_up_to(10)    

## acc = acumulator, es la variable que irá recibiendo los valores para ejecutar la sumatoria.
##Otra forma de escribir el acumulador es acc = acc + number

