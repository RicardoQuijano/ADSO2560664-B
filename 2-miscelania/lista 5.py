import random
tam, pos = 0, 0
vec=[]
pos = []
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
usu = int(input("ingresa tu numero "))
cont=0
for i in range (len(vec)):
    if (usu==vec[i]):
        cont+=1
        pos.append(i)
if cont==0:
    print("El número ingresado no esta en la lista, se procede a añadir")
    vec.append(usu)
    print(vec)
else:
    print("El número ingresado se encontro",cont,"veces y esta en la posición:",pos)