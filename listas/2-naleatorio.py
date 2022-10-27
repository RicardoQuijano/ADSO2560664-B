#tamaño del arreglo que empiece en 10 llenar entre 0 y 100
#sumar, promediar, moda, mediana, desviación estandar
#no usar importaciones solo random

import random
tam=1
while tam<10 or tam>25:
    tam=round(random.random()*100)
print(tam)

lista1=[]
suma=0
prom=0
for i in range (tam):
    lista1.insert(i,round(random.random()*100))
    