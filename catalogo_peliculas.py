
class CatalogoPelicula:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')#agrega un nuevo contenido al archivo txt

    def listar_peliculas(self):
        with open(self.ruta_archivo, 'r') as archivo:
           print(archivo.read())  #mostrar lo que hay dentro del archivo txt


    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        print(f'Catálogo eliminado: {self.ruta_archivo}')#elimina el archivo txt
        