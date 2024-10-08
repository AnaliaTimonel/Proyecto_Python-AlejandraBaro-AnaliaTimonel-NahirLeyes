#importamos los archivos que utilizaremos
from catalogo_peliculas import CatalogoPelicula
from peliculas import Pelicula



#mensaje de bienvenida inicial
print("********************************************************")
print("******BIENVENIDO A TU CATALOGO DE PELICULAS ONLINE******")
print("********************************************************")

        
#valor inicial de opcion
opcion = None

nombre_catalogo = input("Ingrese el nombre del catálogo: \n")#seleccionamos el catalogo """"terror"""""
catalogo = CatalogoPelicula(nombre_catalogo)  # con este paso creo mi objeto / instancia

#bucle para que el inicio se siga ejecutando hasta seleccionar SALIR
while opcion != 4:
    try:#botonera
        print("\n*****Opciones:***** ")
        print("1- Agregar película")
        print("2- Listar película")
        print("3- Eliminar catálogo ")
        print("4- SALIR\n")
        #ingreso de opcion del usuario
        opcion = int(input("Escriba una opción del menú (1-4): "))
        #condicionales que ejecutaran las funciones especificas segun lo elegido
        if opcion == 1:
            nombre_pelicula = input("Ingrese una nueva pelicula a su catalogo: ")
            nombre_pelicula.upper()
             
            if nombre_pelicula == "":
                print("Error, por favor escribir bien el nombre de la película")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
            
        elif opcion == 2:
            catalogo.listar_peliculas()

        
        elif opcion == 3:
            catalogo.eliminar_catalogo()
    
    except Exception as e:
        print("\n¡Ocurrio un error!\n", e, "\n")
        opcion = None

else: 
    print(F"Hasta la proxima !")    