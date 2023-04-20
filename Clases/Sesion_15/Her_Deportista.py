

#---------------------Clase de Padre-----------------------------
class Deportista: # Clase Papá
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre = nombre  #Metodo privado
        self.__documento= documento
        self.__edad = edad


    # lo siguiente va dentro de la clase, no dentro del constructor
    #------------------Getters---------------#
    def getNombre(self):
        return self.__nombre

    def getDocumento(self):
        return self.__documento

    def getEdad(self):
        return self.__edad

    #------------------Setters----------------#

    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setDocumento(self,documento:int):
        self.__documento = documento

    def setEdad(self,edad:int):
        self.__edad = edad

    #----------------Sobrecarga metodo---------#

    def palmares(self):
        return "Ha ganado una Medalla"


#---------------Clase Hijo Deportista Futbol--------------------------#
class Deportistafutbol(Deportista):
    def __init__(self,nombre:str,documento: int,edad:int, golesAnotados: int,nombreEquipo: str):
        super().____init__(nombre,documento,edad)
        self.__golesAnotados=golesAnotados
        self.__nombreEquipo=nombreEquipo

    #------------------Getters Hijo---------------
    def getGolesAnotados(self):
        return self.__golesAnotados
    
    def getNombreEquipo(self):
        return self.__nombreEquipo
    
    #------------------Setters hijo--------------
    def setGolesAnotados(self,golesAnotados:int):
        self.__golesAnotados=golesAnotados

    def setNombreEquipo(self,nombreEquipo:str):
        self.__nombreEquipo = nombreEquipo
    
    #------------------Sobrecarga metodo----------
    def palmares(self):
        return "Ganado una, la copa Europa"


#----------------Clase Hijo Basket--------------------------------#
#Crear clase de BAstek y tenis


def main():
    Futbolista =  Deportista('Falcao', 1000857282,36,\
                              35,'Selección Colombia') #Datos que le paso a el ocnstructor
    print(f'Deportista: {Futbolista.getNombre ()}\n' +\
          f'Documento:{Futbolista.getDocumento()}\n'+\
          f'Edad:{Futbolista.get}')


if __name__== "__main__":
    main()