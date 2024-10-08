

#nombre de la clase
class CatalogoPelicula:
    
    #creamos la clase y el objeto que seran el catalogo como tal derivandonos al archivo txt
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'
        
    #funcion para agregar pelicula
    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')#agrega un nuevo contenido al archivo txt
            
    #funcion para ver la lista de peliculas
    def listar_peliculas(self):
        with open(self.ruta_archivo, 'r') as archivo:
           print(archivo.read())  #mostrar lo que hay dentro del archivo txt

    #funcion para eliminar el catalogo
    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        print(f'Catálogo eliminado: {self.ruta_archivo}')#elimina el archivo txt
        