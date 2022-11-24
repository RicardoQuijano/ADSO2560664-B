# calculadora: suma resta multiplica y divide


def suma (n1,n2):
    resultado=n1+n2
    return resultado

def resta (n1,n2):
    resultado=n1-n2
    return resultado

def multiplica (n1,n2):
    resultado=n1*n2
    return resultado

def division (n1,n2):
    resultado=n1/n2
    return resultado

def modulo (n1,n2):
    resultado=n1%n2
    return resultado

def menu ():
    while True:
        print ("1. Suma")
        print ("2. Resta")
        print ("3. Multiplicacion")
        print ("4. Division")
        print ("5. Modulo")
        opcion=int(input("Escoja la opcion")) #3
        match opcion:
            case 1:
                nu1=int(input("Ingrese numero 1"))
                nu2=int(input("ingrese numero 2"))
                print (suma(nu1,nu2))
            case 2:
                nu1=int(input("Ingrese numero 1"))
                nu2=int(input("ingrese numero 2"))
                print (resta(nu1,nu2))
            case 3:
                nu1=int(input("Ingrese numero"))
                nu2=int(input("ingrese numero"))
                print (multiplica(nu1,nu2))
            case 4:
                nu1=int(input("Ingrese numero 1"))
                nu2=int(input("ingrese numero 2"))
                print (division(nu1,nu2))
            case 5:
                nu1=int(input("Ingrese numero 1"))
                nu2=int(input("ingrese numero 2"))
                print (modulo(nu1,nu2))
            case _:
                print ("Oiga ud digito otro numero")
                print ("finaliza el programa")
                break
##################################################################

menu()

