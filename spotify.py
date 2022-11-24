import os
import time
"""spotify={'juanes': {'dfd': ('f', '4'), 'dfew': ('ere', '6')},
         'pedro': {'we': ('df', '4')},
         'vicente': {'diferencia': ('ranchera', '3'),},
         'laura': {'en cambio no': ('pop', '5')},}"""
spotify={}
canciones={}
def añadirArtista (diccionario):
    op=1
    while op==1:
        os.system("cls")
        print("-"*50)
        print ("       1 -> Añadir Cantante: ")
        print("-"*50)
        artista=input(" Ingrese nombre del cantante:  ")
        if artista =="":
            print("-"*50)
            print ("     ¡¡¡No ingreso ningún dato!!! ")
            print("-"*50),time.sleep(3)
            break
        if artista in diccionario.keys():
            canciones=diccionario[artista]
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
        else:
            canciones={}
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
        while True:
            os.system("cls")
            print("-"*50)
            print ("       1 -> Añadir Cantante: ")
            print("-"*50)
            print("Deseas agregar más cantantes si/no",end=":  ")
            sigue=input()
            if sigue.upper()=="SI":
                break
            elif sigue.upper()=="NO":
                op=0
                break
            else:
                print("NOTA: Digitaste un valor erroneo, Escoja SI o NO")
                print("-"*50),time.sleep(3)

def ingresarCanciones (artista,diccionario):
    #print(diccionario)
    op=1
    while op==1:
        os.system("cls")
        print("-"*50)
        print ("       1 -> Añadir Canción para: \"",artista,"\"")
        print("-"*50)
        print("Ingrese nombre de la canción:",end="  ")
        cancion=input()
        if cancion =="":
            break
        print("ingrese el genero de la canción:",end="  ")
        genero=input()
        if genero=="":
            break
        print("ingrese la duración de la canción en min:",end="  ")
        duracion=input()
        if duracion=="":
            break
        if cancion in diccionario:
            print("-"*50),time.sleep(1)
            print("          ¡¡ERROR!! La canción ya fue agregada con anterioridad"),time.sleep(0.3)
            print("          ¡¡ERROR!! no se pudo realizar su solicitud"),time.sleep(2)
            print("-"*50),time.sleep(1)
        else:
            diccionario[cancion]=(genero,duracion,)
            print("-"*50),time.sleep(1)
            print("          ¡¡Canción agregada con exito!!     "),time.sleep(1)
            print("-"*50),time.sleep(1)
        while True:
            os.system("cls")
            print("-"*50)
            print ("       1 -> Añadir Canción para: \"",artista,"\"")
            print("-"*50)
            print("Deseas agregar más canciones para el cantante: ",artista,"si/no",end=":  ")
            sigue=input()
            if sigue.upper()=="SI":
                os.system("cls")
                print("-"*50)
                print ("       1 -> Añadir Canción para: \"",artista,"\"")
                print("-"*50)
                break
            elif sigue.upper()=="NO":
                op=0
                break
            else:
                print("NOTA: Digitaste un valor erroneo, Escoja SI o NO")
                print("-"*50),time.sleep(3)
    return diccionario

def buscarArtista (diccionario):
    os.system("cls")
    print("-"*50)
    print ("       2 -> Buscar Cantante:")
    print("-"*50)
    nombre=input("Ingrese el nombre del cantante a buscar:  ")
    if nombre in diccionario.keys():
        print("Si se encuentra en la librería y estas son sus canciones:"),time.sleep(1)
        print("-"*50)
        musica=diccionario[nombre]
        for cla,valor in musica.items(): 
            print (cla,"genero:",valor[0],"duración:",valor[1],sep=" -> ",end=" minutos \n"),time.sleep(1)
        print("-"*50),time.sleep(5)
    else:
        print("No se encuentra en la librería de reproducción"),time.sleep(3)
    while True:
        os.system("cls")
        print("-"*50)
        print ("       2 -> Buscar Cantante:")
        print("-"*50)
        print("Deseas buscar otro cantante: ","si/no",end=":  ")
        sigue=input()
        if sigue.upper()=="SI":
            return buscarArtista(spotify)
        elif sigue.upper()=="NO":
            break
        else:
            print("NOTA: Digitaste un valor erroneo, Escoja SI o NO")
            print("-"*50),time.sleep(3)

def buscarCancion (diccionario):
    os.system("cls")
    print("-"*50)
    print ("       3 -> Buscar Canción:")
    print("-"*50)
    cancion=input("Ingrese el nombre de la cancion a buscar: ")
    cont=0
    for j in diccionario:
        musica=diccionario[j]
        if cancion in musica.keys():
            cont=1
            print("")
            print ("La canción se encuentra en el Spotify y el cantante es: ",j)
            print("-"*50),time.sleep(6)
    if cont==0:
        print("")
        print("no se encontro la canción en el Spotify")
        print("-"*50),time.sleep(6)
    while True:
        os.system("cls")
        print("-"*50)
        print ("       3 -> Buscar Canción:")
        print("-"*50)
        print("Deseas buscar otra canción: ","si/no",end=":  ")
        sigue=input()
        if sigue.upper()=="SI":
            return buscarCancion(spotify)
        elif sigue.upper()=="NO":
            break
        else:
            print("NOTA: Digitaste un valor erroneo, Escoja SI o NO")
            print("-"*50),time.sleep(3)

def eliminarArtista (artista,diccionario):
    if artista in diccionario.keys():
        del diccionario[artista]
        print("-"*50),time.sleep(1)
        print("          ¡¡Cantante eliminado con éxito!!     "),time.sleep(1)
        print("          ¡¡Nueva librería actualizada!!     "),time.sleep(1)
        print("-"*50),time.sleep(1)
        while True:
            print("Deseas ver la nueva librería: ","si/no",end=":  ")
            sigue=input()
            if sigue.upper()=="SI":
                return mostrarLibreria(spotify)
            elif sigue.upper()=="NO":
                break
            else:
                print("NOTA: Digitaste un valor erroneo, Escoja SI o NO")
                print("-"*50),time.sleep(3)
    else:
        print("-"*50),time.sleep(1)
        print("El cantante no se encuentra en la librería")
        print("-"*50),time.sleep(1)
    return diccionario

def ordenarAlfabeticamente (diccionario):
    os.system("cls")
    print("-"*50)
    print ("       5 -> Ordenar Alfabeticamente:")
    print("-"*50)
    orden=sorted(diccionario.keys())
    print("Librería de Cantantes Ordenada con éxito:")
    print(orden),time.sleep(5)

def masCanciones (diccionario):
    os.system("cls")
    print("-"*50)
    print ("       6 -> El que tiene más canciones:")
    print("-"*50)
    mayor=0
    for x in diccionario:
        cancion=len(diccionario[x])
        if cancion > mayor:
            mayor=cancion
            actor=x
    return (actor, mayor)

def masLarga(diccionario):
    os.system("cls")
    print("-"*50)
    print ("       7 -> El que tiene la canción más larga:")
    print("-"*50)
    lista=[]
    for x in diccionario:
        canciones=diccionario[x]
        larga=0
        for can,j in canciones.items():
            valor=j
            tiempo=int(valor[1])
            if larga<tiempo:
                larga=tiempo
                cancionmay=can
        lista+=[x,cancionmay,larga]
        mayor=0
        artistamayor=[]
        for x in range(2,len(lista),3):
            if lista[x]>mayor:
                artistamayor=lista[x-2],lista[x-1],lista[x]
                mayor=lista[x] 
    return (artistamayor)

def masCorta(diccionario):
    os.system("cls")
    print("-"*50)
    print ("       7 -> El que tiene la canción más larga:")
    print("-"*50)
    lista=[]
    for x in diccionario:
        canciones=diccionario[x]
        larga=99999999999999
        for can,j in canciones.items():
            valor=j
            tiempo=int(valor[1])
            if tiempo<larga:
                larga=tiempo
                cancionmen=can
        lista+=[x,cancionmen,larga]
        menor=99999999999
        artistamenor=[]
        for x in range(2,len(lista),3):
            if menor>lista[x]:
                artistamenor=lista[x-2],lista[x-1],lista[x]
                menor=lista[x]
    return (artistamenor)

def mostrarLibreria (diccionario):
    os.system("cls")
    print("-"*50)
    print ("       9 -> Ver Libreria Spotify: ")
    print("-"*50),time.sleep(1)
    dic= list (diccionario.keys())
    if len(dic)==0:
        print("La libreria aún no tiene Datos")
        print("-"*50),time.sleep(4)
    else:
        for c,v in diccionario.items():
            print(c," sus canciones son: ",v),time.sleep(1.2)
        print("-"*50),time.sleep(4)

def menu ():
    while True:
        os.system("cls")
        print("-"*50)
        print ("       BIENVENIDO A LA LIBRERIA SPOTIFY ")
        print("-"*50),time.sleep(0.7)
        print ("1","Añadir Cantante", sep=" -> "),time.sleep(0.35)
        print ("2","Buscar Cantante", sep=" -> "),time.sleep(0.35)
        print ("3","Buscar Cancion", sep=" -> "),time.sleep(0.35)
        print ("4","Eliminar Cantante", sep=" -> "),time.sleep(0.35)
        print ("5","Ordenar Alfabeticamente", sep=" -> "),time.sleep(0.35)
        print ("6","El que tiene mas canciones", sep=" -> "),time.sleep(0.35)
        print ("7","El que tiene la canción mas larga", sep=" -> "),time.sleep(0.35)
        print ("8","El que tiene la canción mas Corta", sep=" -> "),time.sleep(0.35)
        print ("9","Mostrar la libreria", sep=" -> "),time.sleep(0.35)
        print ("10","Salir", sep=" -> "),time.sleep(0.35)
        seleccion=input("Escoja la opción:  ")
        match seleccion:
            case "1":
                añadirArtista(spotify)
            case "2":
                buscarArtista(spotify)
            case "3":
                buscarCancion(spotify)
            case "4":
                os.system("cls")
                print("-"*50)
                print ("       4 -> Eliminar Cantante: ")
                print("-"*50),time.sleep(1)
                nombre=input("Ingrese el nombre del cantante a eliminar:  ")
                eliminarArtista(nombre,spotify)
            case "5":
                ordenarAlfabeticamente(spotify)
            case "6":
                mayor=masCanciones(spotify)
                print("El cantante con mas canciones es:",mayor[0],"con",mayor[1],"canciones",sep=" ")
                print("-"*50),time.sleep(6)
            case "7":
                larga=masLarga(spotify)
                print ("Es ", larga[0]," con la canción ",larga[1]," y la duración es: ",larga[2]," minutos")
                print("-"*50),time.sleep(6)
            case "8":
                corta=masCorta(spotify)
                print ("Es ",corta[0]," con la canción ",corta[1]," y la duración es: ",corta[2]," minutos")
                print("-"*50),time.sleep(6)
            case "9":
                mostrarLibreria(spotify)                
            case "10":
                os.system("cls")
                print("-"*50)
                print("Hasta pronto, ¡¡FIN!!")
                print("-"*50),time.sleep(3)
                break
            case _:
                print("digitastes un número incorrecto")

menu()