"""4.Generar numero (generarlo random) y adivinarlo diciendo si cada intento es mayor
    o menor que el numero. Decir cuantos numeros ingreso antes de adivinarlo
"""
from random import randint

aleatorio = randint(1,100)
num=0
cont=0
print("ADIVINA EL NÚMERO")
print(aleatorio)
while num!=aleatorio:
    num=int(input("Ingrese un número:   "))
    cont+=1
    if num>aleatorio:
        print("El número a adivinar es menor")
    elif num<aleatorio:
        print("El número a adivinar es mayor")
    else:
        print("Haz adivinado el número")
print("\nUsted lo adivino a los",cont,"intentos")