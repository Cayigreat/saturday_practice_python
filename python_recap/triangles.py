import time

# Este programa ayuda a saber si podemos hacer un triángulo
# dadas tres longitudes

print("Hola, te voy a ayudar con eso de los triángulos")
l1 =int(input("ingresa longitud uno\n"))
l2 =int(input("ingresa longitud dos\n"))
l3 =int(input("ingresa longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:") 

print(l1,l2,l3) 

if(l1 <=l2+l3):
  print("Vamos bien, revisemos los otros casos")
  time.sleep(0.5)  
  if(l2<=l1+l3):
    print ("Seguimos bien, revisemos los otros casos")  
    time.sleep(0.5)  
    if(l3<=l2+l1): 
      print("Si es posible el triángulo")
    else:
      print("No es posible el triángulo")
  else:
    print("no es posible el triángulo")
else: 
  print("No es posible el triángulo:", l1, "No es menor que", l2 , "+", l3)


