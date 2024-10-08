from catalogo_peliculas import CatalogoPelicula
from peliculas import Pelicula




print("********************************************************")
print("******BIENVENIDO A TU CATALOGO DE PELICULAS ONLINE******")
print("********************************************************")

        

opcion = None

nombre_catalogo = input("Ingrese el nombre del catálogo: \n")#terror
catalogo = CatalogoPelicula(nombre_catalogo)  # con este paso creo mi objeto / instancia


while opcion != 4:
    try:
        print("\n*****Opciones:***** ")
        print("1- Agregar película")
        print("2- Listar película")
        print("3- Eliminar catálogo ")
        print("4- SALIR\n")
        
        opcion = int(input("Escriba una opción del menú (1-4): "))

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