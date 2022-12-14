"""
trabajo y potencia en un elevador de carga:

En una obra de construcción requieren implementar una grúa que les permita elevar materiales
de construcción a la parte más alta de la obra, como ingeniero, se te ha encargado de
determinar la potencia para el motor de la grua.
Sabiendo que la carga máxima es: dada por el usuario entre 2 y 8 kg
una altura: (random entre 1 y 10m)
y un tiempo de: (random 5 y 20 s)

"""
import os, time, random
def fuerza (masa, grav=9.8):
    fuer=masa*grav
    return fuer

def trabajo (fuer, desplaza):
    traba=fuer*desplaza
    return traba

def potencia (trabajo, tiemp):
    poten=trabajo/tiemp
    return poten

def titulo ():
    print ("-"*80)
    print ("|                 TRABAJO Y POTENCIA EN UN ELEVADOR DE CARGA                    |")
    print ("-"*80)

def datos ():
    while True:
        try:
            print ("por favor ingrese la carga máxima (entre 2 y 8 kg) ", end=" ")
            carga=int(input())
            if carga >=2 and carga <=8:
                altua=random.randint(1,10)
                tiempo=random.randint(5,20)
                break
        except ValueError:        
            print ("Upss !! no fue un número valido, intente de nuevo"),time.sleep(3)
            os.system("cls")
            titulo()
        except:
            print ("Upss !! tipo de error desconocido, vuelva a intentar"),time.sleep(3)
            os.system("cls")
            titulo()
            
    return (carga, altua, tiempo)

titulo()
print ("En una obra de construcción requieren implementar una grúa que les permita")
print ("elevar materiales de construcción a la parte más alta de la obra, como ingeniero,")
print ("se te ha encargado de determinar la potencia para el motor de la grua."),time.sleep(6)
os.system("cls")
titulo()

dat=datos()
fu=fuerza(dat[0])
tra=trabajo(fu,dat[1])
po=potencia(tra,dat[2])
print ("la pontencia según los datos ingresados ( carga:",dat[0],"kg, altura",dat[1],"m, tiempo",dat[2],"s) es:",po,"J",end=" ")
