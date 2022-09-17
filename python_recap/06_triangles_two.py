# Este programa ayuda a saber si podemos hacer un triángulo
# dadas tres longitudes

print("Hola, te voy a ayudar con eso de los triángulos")
l1 =int(input("ingresa longitud uno\n"))
l2 =int(input("ingresa longitud dos\n"))
l3 =int(input("ingresa longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:") 

print(l1,l2,l3) 


  
if(l1 <=l2+l3) and (l2<=l1+l3) and (l3<=l2+l1):
   print("Si es posible el triángulo")
else:
   print("No es posible el triángulo")
  