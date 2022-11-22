"""import random
tam = 0
vec=[]
x,y,z=0,1,0
while tam<5 or tam>20:
    tam = int(input("Ingresa un numero mayor a 5 y menor a 20   "))
vec.append(1)
for i in range(tam):
    z=x+y
    vec.append(z)
    x=y
    y=z
print(vec)"""

x=input()
y=input()
print(x + y)

a=1
b=0
c=a & b
print (c)
d = a|b
print (d)
e=a^b
print (e)
print (c + d+ e)

e=[3,1,-2]
print(e[e[-1]])

e=[1,2,3,4]
print(e[-3:-2])