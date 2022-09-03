# Las variables son nombres que apuntan a un valor
# Y el valor es de cierto tipo

name = "stranger"

# No pueden comenzar con números ni palabras reservadas
# Es muy aconsejable no utilizar ni mayúsculas ni acentos
# Para separar nombres largos utilizar "_" (underscore)

long_name_variable = "Something"
longaniza = "Chillán"

print (name, long_name_variable, longaniza)

# Podemos saber el tipo(class) de la variable con la función type

print (type(longaniza),type(name), type (long_name_variable))

# Otros tipos frecuentes

# int
number = 42

# bool
is_real = True 
not_real = False
print (type (is_real),type(not_real))

# float
decimal = 1.0
print (type (decimal))