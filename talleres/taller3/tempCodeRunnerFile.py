suma=0
lista=[4,7,7,9,10]
prom=(4+7+7+9+10)/5
for i in range (len(lista)):
    suma+=(lista[i]-prom)**2
print (suma)
radicando= suma /4
desviacion=radicando**(0.5)

print("La desviación estandar es:",desviacion)