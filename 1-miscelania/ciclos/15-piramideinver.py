"""Diseñar e implementar un programa que solicite a su
usuario un valor no negativo n y visualice la siguiente salida:
1 2 3 ........ n-1 n
1 2 3 ........ n-1
.........
1 2 3
1 2
1
"""

num= int (input ("Digite un numero entero positivo: "))
nu=num+1
if num > 0:
    while nu > 0:
        for i in range(1, nu):
            print (i , end=" ")
        nu-=1
        print()
else:
    print ("El número debe ser positivo")