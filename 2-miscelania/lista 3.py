import random
tam=0
vec=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)  
cp, ci, sp, si = 0, 0, 0, 0
for i in range (len(vec)):
    if vec [i]%2==0:
        cp += 1
        sp +=vec[i]
    else:
        ci += 1
        si +=vec[i]
print("Total de # pares",cp, "Total de # impares",ci)
print ("total de suma de pares", sp)
print("Promedio de impares es", si // ci)