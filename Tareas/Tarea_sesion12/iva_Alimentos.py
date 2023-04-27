import Productos
def valor():
    dicc = {}
    f = open('Alimentos.txt','rt')
    alimentos = f.readlines()
    f.seek(0)
    for i in range(len(alimentos)):
        val=f.readline().rstrip('\n').split(',')
        dicc[val[1]]=float(val[2])
    Productos.Producto(dicc)


if __name__=='__main__':
    valor()







    