"""Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número."""

from math import trunc
n1=100 
cubo=0
while n1 < 1000:
    a=trunc(n1/100)
    b=trunc(n1/10)-(a*10)
    c=n1-(a*100+b*10)
    cubo=(a**3)+(b**3)+(c**3)
    if cubo ==n1:
        print (n1,cubo)
        n1+=1
    else:
        n1+=1