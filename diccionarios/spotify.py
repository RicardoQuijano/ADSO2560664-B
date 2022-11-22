spotify={}
canciones={}
def añadirArtista (diccionario):
    while True:
        artista=input("Ingrese nombre del artista  ")
        if artista =="":
            break
        if artista in diccionario.keys():
            canciones=diccionario[artista]
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
        else:
            canciones={}
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
    
    return diccionario

def ingresarCanciones (artista,diccionario):
    print(diccionario)
    while True:
        print("Ingrese nombre de la canción", end=":  ")
        cancion=input()
        if cancion =="":
            break
        print("ingrese el genero de la canción ",end=": ")
        genero=input()
        if genero=="":
            break
        print("ingrese la duración de la canción",end=": ")
        duracion=input()
        if duracion=="":
            break
        if cancion in diccionario:
            print("ATENCIÓN::::LA CANCIÓN YA FUE AGREGADA AL SPOTIFY")
        else:
            diccionario[cancion]=(genero,duracion,)
        print("Vas  a seguir agregando canciones para: ",artista,"\n Presione Enter para salir o cualquier tecla para seguir",end=":    ")
        sigue=input()
        if sigue=="":
            break
    return diccionario

def buscarArtista (diccionario):
    nombre=input("Ingrese el nombre del artista a buscar:  ")
    print(diccionario.keys())
    if nombre in diccionario.keys():
        print("El artista se encuentra en nuestra lista de reproducción\n y estas son sus canciones:")
        musica=diccionario[nombre]
        for cla,valor in musica.items(): 
            print (cla,"genero:",valor[0],"duración:",valor[1],sep=" -> ",end="minutos \n")
    else:
        print("El artista no se encuentra en nuestra lista de reproducción")

def eliminarArtista (artista,diccionario):
    if artista in diccionario.keys():
        del diccionario[artista]
    return diccionario

def ordenarAlfabeticamente (diccionario):
    orden=sorted(diccionario.items())
    print("Biblioteca SPOTIFY ordenada alfabeticamente x Artista: \n",orden)
    
def menu ():
    while True:
        print ("BIENVENIDO A LA BIBLIOTECA SPOTIFY")
        print ("Seleccione el número de la lista según lo que desee")
        print (" 1 Añadir Artista \n 2 Buscar Artista \n 3 Buscar Cancion \n 4 Eliminar Artista \n 5 Ordenar Alfabeticamente \n 6 El que tiene mas canciones \n 7 El que tiene la canción mas larga \n 8 El que tiene la canción mas Corta \n  Enter para salir")
        seleccion=input()

        if seleccion=="1":
            print(añadirArtista(spotify))
        elif seleccion=="2":
            buscarArtista(spotify)
        #elif seleccion=="3":
            #buscarCancion(spotify)
        elif seleccion=="4":
            nombre=input("Ingrese el nombre del artista a eliminar:  ")
            print("Nueva Biblioteca Spotify: ",eliminarArtista(nombre,spotify))
        elif seleccion=="5":
            ordenarAlfabeticamente(spotify)

        else:
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
            break

menu()