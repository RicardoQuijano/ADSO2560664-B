import random
tam=0
vec=[]
vecmayor=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range(len(vec) - 1):
    for y in range(i+1,len(vec)):
        if vec[i] > vec[y]:
            vec[i], vec[y] = vec[y], vec[i]
print("Arreglo de menor a mayor:",vec)
for i in range(len(vec)-1,-1,-1):
    vecmayor.append(vec[i])
print("Arreglo de mayor a menor:",vecmayor)
