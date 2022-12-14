""" Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod."""

n1=int(input("Ingresa un número: "))
n2=int (input("Ingresa un número: "))
contador=0
if n1 > n2:
    coc, res= divmod(n1,n2)
else:
    coc, res=divmod(n2,n1)
print ("El cociente es: {}, y el residuo es: {}".format(coc,res))