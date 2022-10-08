# Completar la siguiente funcion para que imprima cualquier table de multiplicacion hasta el 12



def multiplication_table(number = 1):
    print ("##########################")
    for i in range(1,13):   
        print(number, "x", i, "=", number *i)     
    
multiplication_table(2)
multiplication_table(7)