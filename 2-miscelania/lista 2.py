import random
vec=[]
vecprimos=[]
tam = 0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for x in range (len(vec)):
    contar=0
    y=1
    while y <=vec[x]:
        if vec[x] % y == 0:
            contar+=1
        y+=1
    if contar == 2:
        vecprimos.append(vec[x])
print("los números primos son:",len(vecprimos),"y son:",vecprimos)