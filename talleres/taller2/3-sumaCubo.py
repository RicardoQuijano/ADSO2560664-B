#3.numeros de 3 digitos donde la suma del cubo de cada digito sea igual al numero.

for i in range (100,1000):
    digito=0
    suma=0
    j=i
    while j>0:
        mod = j%10
        nuevo = j//10
        digito=mod**3
        suma+=digito
        j=nuevo
    if suma == i:
        print ("El número:",i,"es igual a la suma de sus dígitos")