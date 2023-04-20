'''''
1. Realice un programa donde se cree una matriz de 5x10, después se imprima en pantalla la matriz creada, 
indicando cuál es el número más alto y más bajo dentro de la lista, incluyendo su respectiva posición. 
Finalmente se organice la matriz del número mayor al menor, empezando desde la posición [0,0].
'''''
import random as rand
def matrices(filas, columnas):
    filas=5
    columnas=10
    matriz=[]
    for i in range(1,6):#filas dadas
        matriz.append([])
        for j in range(1,11):
            num = rand.randint(1,20)
            matriz[i].append(num)
    return matriz
            
def escalar(matriz,n):
    for i in matriz:
        for j in range (len(i)):
            i[j]= n*i[j]
    return escalar
print(escalar)

matrices(matriz)
matriz = matrices(filas,columnas)