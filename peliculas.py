import os   # es el modulon que se importa para poder eliminar el archivo de la computadora

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre #atributo privado

   
    def __str__(self):
        return f"nombre:{self.nombre}"

   #Métodos de acceso para el atributo privado: mostrar el atributo "nombre" y modificarlo
   # recordar que hay dos metodos (decoradores o funciones)

    @property       #decorador que permite que un método sea accedido como un atributo 
    def nombre(self): 
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 