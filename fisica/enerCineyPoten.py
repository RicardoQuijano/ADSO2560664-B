"""
    Sobre una mesa que tieen 110 centimetros de altura, con relación al piso, se encuentra a un libro
    de 3200gramos. Encuentre la energía potencial del piso con relación al piso.
    Ecuación = ep = mgh

"""
import os, time, math

def enerPotencial (masa, altura, grav=9.8):
    aMet=altura/100
    mKg=masa/1000
    return round((mKg*grav*aMet),1)

def titulo ():
    print ("-"*80)
    print ("|                           EJEMPLO DE ENERGÍA POTENCIAL                        |")
    print ("-"*80)

def datos ():
    while True:
        try:
            titulo()
            print ("Sobre una mesa que tiene ____ centimetros de altura (ingrese en cm): ", end="")
            altu=int(input())
            print("con relación al piso, se encuentra a un libro de _____ gramos (ingrese los gramos): ", end="")
            mas=int(input())
            print ("Encuentre la energía potencial del piso con relación al piso."), time.sleep(2)
            break
        except ValueError:        
            print ("Upss !! no fue un número valido, intente de nuevo"),time.sleep(3)
            os.system("cls")
        except:
            print ("Upss !! tipo de error desconocido, vuelva a intentar"),time.sleep(3)
            os.system("cls")
    return (enerPotencial(altu, mas))

dat=datos()
print(""),time.sleep(0.5)
print ("-"*80),time.sleep(0.5)
print ("     La energía potencial es de:  ",dat," J"),time.sleep(0.5)
print ("-"*80),time.sleep(0.5)
