'''
Crear un programa basado en POO con las siguientes características:

- Crear una clase "Ciudadano" que incluya los campos privados Nombre, Cédula y Edad.
- Crear los setters y getters correspondientes a los campos, verificando que el número 
de cedula tenga entre 8 y 10 dígitos y que la edad ingresada sea un número positivo mayor que cero.
- Establecer un método "mostrar" que imprima la información, por ejemplo:

        Nombre: Nicolás - Edad: 28 - CC: 1289384734

- Establecer un método "esMayorDeEdad" que verifique si el ciudadano es o no mayor de edad.

'''
class Ciudadano:
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
def mostrar(self):
    return print(f'Nombre:{self.__nombre} , Edad:{self.__edad} , Cedula:{self.__cedula}')
    

def esMayorDeEdad(self):
    if self.__edad>=18:
        return print(f'Es mayor de edad')
    else:
        return print(f'Es menor de edad')
def getMostrar(self):
    if self.__nombre==None or self.__edad==None or self.__cedula==None:
        return print('Ingrese datos validos')
    else:
        self.__mostrar()
def getEsMayorDeEdad(self):
    if self.__edad==None:
        return print('Ingrese un valor para la edad')
    else:
        self.__EsMayorDeEdad()

def main():
    persona=Ciudadano('Edwin',16,5264654)
    persona.setNombre('Edwuin')
    persona.setEdad(16)
    persona.setCedula(5264654)
    persona.getMostrar()
    persona.getEsMayorDeEdad()
if __name__=='__main__':
    main()