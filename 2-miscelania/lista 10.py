import math
import random
tam=0
vec=[]
vecmayor=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
#Desviación estandar = raiz cuadrada de la (sumatoria de los numeros menos el promedio al cuadrado / tamaño - 1)
suma=0
for i in range (len(vec)):
    suma+=vec[i]
prom=suma/tam
suma=0
for i in range (len(vec)):
    suma+=(vec[i]-prom)**2
radicando= suma /(tam-1)
desviacion=math.sqrt(radicando)

print("La desviación estandar es:",desviacion)