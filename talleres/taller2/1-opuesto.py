"""1. pedir numeros, imprimirlo con el opuesto 
(ejemplo 5 opuesto -5, -10 opuesto 10), 
finaliza con cero y diga cuantos ingreso
"""

num =2
cont=0

while num!=0:
    num = int(input("Ingrese un número:  "))
    if num!=0:
        print (num,"su opuesto es:",num*-1)
        cont+=1
print ("Ud digito:",cont,"números")