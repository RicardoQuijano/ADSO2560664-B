"""Hacer una lista de un tamaño de 10 a 25, con un random de 0 a 100.
    sacar la suma, el promedio, la moda, la mediana y la desviacion estandar.
    No usar importaciones"""

import random
tam=1
sum=0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
print ("el tamaño de la lista es:",tam)
lista=[]
for i in range (tam):
    lista.append(round(random.random()*10))
    sum = sum+ lista[i]
print ("La lista random es: ",lista)
print ("la suma de los números de la lista es:",sum)
prom=sum/(len(lista))
print ("El promedio de la lista es:",prom)
moda=0
mayor=0
for i in range (len(lista)):
    contador=0
    for j in range (len(lista)):
        if lista[i]==lista[j]:
            contador+=1
    if(contador>mayor):
        mayor=contador
        moda=lista[i]

print("la moda es el número \"",moda,"\" se repite",mayor," veces")

for i in range (1,len(lista)):
    for j in range (tam-i):
        if lista[j]>lista[j+1]:
            temp=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=temp
print ("La lista de menor a mayor es:",lista)
if tam%2>0: #es impar
    mediana=lista[tam//2]
else:
    mediana=(lista[tam//2] + lista[tam//2 -1])/2

print("la mediana es:",mediana)

#Desviación estandar = raiz cuadrada de la (sumatoria de los numeros menos el promedio al cuadrado / tamaño - 1)
suma=0
for i in range (len(lista)):
    suma+=(lista[i]-prom)**2
print (suma)
radicando= suma /(tam-1)
desviacion=radicando**(0.5)

print("La desviación estandar es:",desviacion)