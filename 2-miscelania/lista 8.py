import random
tam= 0
vec=[]
moda= []
veces=[]
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
mayor=0
for i in range(len(vec) - 1):
    for y in range(i+1,len(vec)):
        if vec[i] > vec[y]:
            vec[i], vec[y] = vec[y], vec[i]
print("Arreglo de menor a mayor:",vec)
for i in range (len(vec)):
    contador=0
    for j in range (len(vec)):
        if vec[i]==vec[j]:
            contador+=1
    if contador>1:
        moda.append(vec[i])
        veces.append(contador)
for i in range (len(moda)):
    for j in range (i+1,len(moda)):
        if (veces[i]>veces[j]):
            mayor=i
print("la moda es el número \"",moda[mayor],"\" se repite",veces[mayor]," veces")
