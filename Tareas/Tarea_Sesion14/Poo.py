'''
Crear un programa basado en POO con las siguientes características:

- Crear una clase "Ciudadano" que incluya los campos privados Nombre, Cédula y Edad.
- Crear los setters y getters correspondientes a los campos, verificando que el número 
de cedula tenga entre 8 y 10 dígitos y que la edad ingresada sea un número positivo mayor que cero.
- Establecer un método "mostrar" que imprima la información, por ejemplo:

        Nombre: Nicolás - Edad: 28 - CC: 1289384734

- Establecer un método "esMayorDeEdad" que verifique si el ciudadano es o no mayor de edad.

'''
class ciudadano:
    def __init__(self):

        self.__nombre = None
        self.__cedula = None
        self.__edad = None
        
#--------------Getters--------------------

    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getEdad(self):
        return self.__edad

#--------------Setters--------------------

    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setCedula(self,cedula:int):
        if 8<=len(cedula)<=10:
            pass
        else:
            print("Cedula invalida, ingrese su cedula de nuevo")
        self.__cedula = cedula

    def setEdad(self,edad:int):
        if 0 < edad >=100:
            pass#edad positiva y mayor a cero
        else:
            print("Edad errónea")
        self.__edad = edad

#----------------Metodo---------------------
def datos():
    persona= ciudadano()
    
def main():
    persona = 