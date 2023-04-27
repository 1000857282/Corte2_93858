class Articulos ():
    pass

class Bebidas(Articulos):
    def __init__(self) :
        super().__init__()
        self.__cantUnidad = None
        self.__proveedor = None 