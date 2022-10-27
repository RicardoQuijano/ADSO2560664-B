import random
tam=int(input("ingrese cantidad   "))
vec=[]
for i in range (tam):
    vec.insert(i,round(random.random()*100))
print (vec)

contpar=0
contimpr=0
sum1=0
sum2=0
prom1=0
prom2=0
for i in range (len(vec)):
    if vec[i]%2==0:
        print(vec[i],"  par")
        contpar=contpar+1
        sum1+=vec[i]
        prom1=sum/len(vec)
    else:
        print(vec[i],"  impar")
        contimpr+=1
        sum2+=vec[i]
        prom2=sum/len(vec)
print ("hay ",contpar," pares y suman: ",sum1," y ",contimpr," impares y suman: ",sum2)
print ("el promedio de los pares es:",prom1)
print ("el promedio de los impares es:",prom2)