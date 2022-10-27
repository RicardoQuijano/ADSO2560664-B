""" pedir un numero al usuario, y de los numeros del 1 al 1000, cuantos son multiplos de n, ademas
sumelos y promedielos. """
cont=0
suma=0
num = int(input("ingresse un numero     "))
for i in range (1 , 1001, 1):
    if num % i == 0:
        cont= cont+1
        suma= suma+i
print ("son multiplos :",cont,"la suma de los multiplos",suma," el promedio es",suma/cont)
