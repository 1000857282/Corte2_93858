#Cree tres clases heredadas de la clase "Ciudadano", basadas en tres profesiones, que incluyan mínimo 2 campos propios cada una.

#Cree por lo menos un método único para cada clase heredada, que tenga relación con cada una de las profesiones seleccionadas.

#En una de las tres clases heredadas, sobrecargue un método.


class Ciudadano():
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre= nombre
        self.__documento=documento
        self.__edad=edad

    # ---------- Getters --------------
    def getNombre(self):
        return self.__nombre

    def getDocumento(self):
        return self.__documento
    
    def getEdad(self):
        return self.__edad

    # ------------ Setters -----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setDocumento(self,documento:int):
        self.__documento=documento

    def setEdad(self,edad:int):
        self.__edad=edad
     # ------ Sobrecarga metodo -----
    def comentario(self):
        return 'Usted puede lograr todo lo que se proponga! '
    
#---------------Clase Mecànico------------------------
class Mecánico(Ciudadano):

    def __init__(self,nombre:str,documento:int,edad:int,nivel:str,ordenesDia:int):
        super().__init__(nombre, documento, edad)
        self.__nivel = nivel
        self.__ordenesDia = ordenesDia

    # ------- Getters --------------
    def getNivel(self):
        return self.__nivel

    def getOrdenesDia(self):
        return self.__ordenesDia
    
    # -------- Setters --------------
    def setNivel(self,nivel:str):
        self.__nivel = nivel
    
    def setOrdenesDia(self,ordenesDia:int):
        self.__ordenesDia = ordenesDia

    # ------ Sobrecarga metodo -----
    def reconocimiento(self):
        return 'Felicitaciones por su buena atención al cliente y por su buena mano de obra'
    
#---------------Clase DJ------------------------
class Dj(Ciudadano):

    def __init__(self,nombre:str,documento:int,edad:int,tipoMusica:str,recomendaciones:int):
        super().__init__(nombre, documento, edad)
        self.__tipoMusica = tipoMusica
        self.__recomendaciones = recomendaciones

    # ------- Getters --------------
    def getTipoMusica(self):
        return self.__tipoMusica

    def getRecomendaciones(self):
        return self.__recomendaciones
    
    # -------- Setters --------------
    def setTipoMusica(self,tipoMusica: str):
        self.__tipoMusica = tipoMusica
    
    def setRecomendaciones(self,recomendaciones:int):
        self.__recomendaciones = recomendaciones

    # ------ Sobrecarga metodo -----
    def Satisfaccion(self):
        return 'Eres uno de los mejores DJ de música electronica'


#---------------Clase Tatuador------------------------------
class Tataudor(Ciudadano):
    
    def __init__(self,nombre:str,documento:int,edad:int,nivel:str,experiencia:str):
        super().__init__(nombre, documento, edad)
        self.__nivel = nivel
        self.__experiencia = experiencia

    # ------- Getters --------------
    def getNivel(self):
        return self.__nivel

    def getExperiencia(self):
        return self.__experiencia
    
    # -------- Setters --------------
    def setNivel(self,nivel:str):
        self.__nivel = nivel
    
    def setExperiencia(self,experiencia:str):
        self.__experiencia = experiencia

    # ------ Sobrecarga metodo -----
    def convocatoria(self):
        return 'Usted hace parte de uno de las mejores convocatoias de tatuadores profesinales'


def main():
    Profesinal1 = Mecánico('Fernando',100089248,30,'Técnico B',8)
    
    print(f'Mecánico: {Profesinal1.getNombre()}\n'+\
    f'Documento:{Profesinal1.getDocumento()}\n'+\
    f'Edad:{Profesinal1.getEdad()}\n'+\
    f'Nivel:{Profesinal1.getNivel()}\n'+\
    f'Ordenes por dia:{Profesinal1.getOrdenesDia()}\n'+\
        f'Reconocimiento:{Profesinal1.reconocimiento()}\n')
    
    Profesional2 = Tataudor('José',1000101956,20,'Profesional', '6 años de expriencia')
    print(f'Tatuador: {Profesional2.getNombre()}\n'+\
    f'Documento:{Profesional2.getDocumento()}\n'+\
    f'Edad:{Profesional2.getEdad()}\n'+\
    f'Nivel:{Profesional2.getNivel()}\n'+\
    f'Experiencia:{Profesional2.getExperiencia()}\n'+\
        f'Comentario:{Profesional2.comentario()}\n' )
    
    Profesional3 = Dj('Sebastián',1000129367,20,'electrónica', 2.378)
    print(f'Dj: {Profesional3.getNombre()}\n'+\
    f'Documento:{Profesional3.getDocumento()}\n'+\
    f'Edad:{Profesional3.getEdad()}\n'+\
    f'Tipo de música:{Profesional3.getTipoMusica()}\n'+\
    f'Recomendaciones:{Profesional3.getRecomendaciones()}\n'+\
        f'Satisfacción:{Profesional3.Satisfaccion()}')



if __name__ == "__main__":
    main()