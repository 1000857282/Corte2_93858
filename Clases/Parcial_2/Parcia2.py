
##Nicol Daniel CAstillo Rios
## Helen Juliana Lopez Castro

#n = open('Catalogo.csv','rt')
#precio es flotante 
'''''
def lectura(): 
    c= open('Catlogo.csv','rt')
    datos = []
    linea = c.readline()
    while linea != '':
        datos.append(linea.rstrip('\n').split(','))
        linea = c.readline()
        c.close()
        return datos
    
    def Orden_Catalogo(datos):
        Catalogo =[]
        for i in datos[1:]:
            country=i[2]
            if country not in Catalogo:
                Catalogo.append(country)
        Catalogo.sort()
        return Catalogo
'''



class Articulos():
    def __init__(self, idArticulo: int, precioBase:float, unidExistencia: int):
        self.__idArticulo= idArticulo
        self.__precioBase= precioBase
        self.__unidExistencia= unidExistencia
    
    # ----- Getters -------
    def getIdArticulo(self):
        return self.__idArticulo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    def getUnidExitencia(self):
        return self.__unidExistencia
    #------- Setters --------
    def setIdArticulo(self,idArticulo:int):
        self.__idArticulo = idArticulo

    def setPrecioBase(self,precioBase:float):
        self.__precioBase = precioBase

    def setUnidExistencia(self, unidExistencia:int):
        self.__unidExistencia = unidExistencia

    # ------- Sobrecarga --------
    #def saludo(self):
       # return "

#-------------------Clase Bebidas-------------------------
class Bebidas(Articulos):
    def __init__(self, idArticulo:int,precioBase:float, unidExistencia: int, cantUnidad:str, proveedor:str):
        super().__init__(idArticulo,precioBase,unidExistencia)
        self.__cantUnidad=cantUnidad
        self.__proveedor  = proveedor

    
    #---------------Getters BEbidas------------
    def getCanUnidad(self):
        return self.__cantUnidad

    def getProveedor(self):
        return self.__proveedor

    # ------------ Setters Bebidas -----------------

    def setCantUnidad(self,cantUnidad:str):
        self.__cantUnidad = cantUnidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    #------------Sobre Carga-------------------
    def Precio_Final(obj):
        return obj.Precio_Final


#-------------------Clase Lacteos-------------------------
class Lacteos(Articulos):
    def __init__(self, idArticulo:int,precioBase:float, unidExistencia: int, cantUnidad:str, proveedor:str):
        super().__init__(idArticulo,precioBase,unidExistencia)
        self.__cantUnidad = cantUnidad
        self.__proveedor  = proveedor

    #---------------Getters Lacteos------------
    def getCanUnidad(self):
        return self.__cantUnidad

    def getProveedor(self):
        return self.__proveedor

    # ------------ Setters Lacteos -----------------
    def setCantUnidad(self,cantUnidad:str):
        self.__cantUnidad = cantUnidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    #------------Sobre carga---------------
    def Precio_Final(obj):
        return obj.Precio_Final

#--------------------Clase Condimentos------------------------

class Condimentos(Articulos):
    def __init__(self, idArticulo:int,precioBase:float, unidExistencia: int, cantUnidad:str, proveedor:str):
        super().__init__(idArticulo,precioBase,unidExistencia)
        self.__cantUnidad=cantUnidad
        self.__proveedor  = proveedor
    
    #---------------Getters Condimentos------------
    def getCanUnidad(self):
        return self.__cantUnidad

    def getProveedor(self):
        return self.__proveedor

    # ------------ Setters Condimentos -----------------

    def setCantUnidad(self,cantUnidad:str):
        self.__cantUnidad = cantUnidad
    
    def setProveedor(self,proveedor:str):
        self.__proveedor=proveedor

    #---------------sobre carga-------------------------
    def Precio_Final(obj):
        return obj.Precio_Final


def lectura():
    n = open('Catalogo.csv', 'rt')
    data = [[],[],[]]
    linea = n.readline().rsplit('\n').split(',')
    print(linea)
    while linea != ['']:
        if  linea[3]=='Bebidas':      
            obj = Bebidas()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBAse(float(linea[5]rstrip('USD')))
            obj.setUnidExistente(int(linea[6]))
            obj.CantUnuidad(linea[4])
            obj.setProveedor(linea[2])
        elif linea[3]=='Lacteos':

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    n.close()
    print(data)
    return data
    


def main():
    Bebidas = Bebidas()
    Bebidas.setCantUnidad('Kevin')
    Bebidas.setproovedor('Español')
    Bebidas.setPrecio_Final(1524348)

    Condimentos = Condimentos()
    Condimentos.setCantunidad('Richard')
    Condimentos.setproovedor('English')
    Condimentos.setPrecio_Final(3937593)

    #----- Aplicantes -----
    print(f'Aplicante: {Bebidas.getidArticulo()}\n'+\
        f'precioBase: {Bebidas.getprecioBase()}\n' + \
            f'unidExistencia: {Bebidas.getunidExistencia()}\n'+
            f'cantunidad:{Bebidas.getcantunidad()}\n'+
            f'proovedor:{Bebidas.getproovedor()}\n'+ 
            Precio_Final(Bebidas)+'\n')
    
    print(f'Aplicante: {Condimentos.getidArticulo()}\n'+\
        f'precioBase: {Condimentos.getprecioBase()}\n' + \
            f'unidExistencia: {Condimentos.getunidExistencia()}\n'+
            f'cantunidad:{Condimentos.getcantunidad()}\n'+
            f'proovedor:{Condimentos.getproovedor()}\n'+\
                  Precio_Final(Condimentos))

if __name__=="__main__":
    main()


