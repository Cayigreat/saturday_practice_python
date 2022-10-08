import random
import time

# El modulo random tiene varias funciones para trabajar con numeros aleatorios
# La funcion choice es una de las mas usadas eligiendo un elemento al azar de una lista

fruits = ['manzana', 'pera', 'frutillas', 'piña']

# Imprimir una fruta al azar
print ('Redoble de tambores...')

for i in range(1,4):
    print(',')
    time.sleep(0.5)

print('Tu fruta es:')
print(random.choices(fruits) )