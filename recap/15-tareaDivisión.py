# Crear una funcion que imprima los numeros divisibles por tres hasta el numero n

def  divisibles_by_three(n):  
    for number in range(1, n + 1):
        if number % 3 == 0:
            print(number)          


divisibles_by_three(50)              
    


