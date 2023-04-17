'''''
2. Realice un programa donde permita crear una lista de 10 números aleatorios entre 1 y 50 (todos números enteros), 
después cree dos funciones donde se reciba la lista como parámetro para:

mayor() - Función que imprima el número mayor de la lista (no puede usar el método max())

primos() - función que imprima los números de la lista que son primos.
'''''
import random as rand
lista = []
for i in range (0,10):
    numero = rand.randint(1,50)
    lista.append(numero)
print(lista)

def minimo_maximo(lista): #en vez de lista puedo poner numb
    menor = lista[0]#Suponemos que el menor y el mayor estan en la primera ubicación. #numb
    mayor = lista[0]#Quien es mayor al numero de la posición 0, pasa a estar en la posición 0 ej: [15,18]--> [18] igual con el menor #numb

    for n in lista: #numb
        if n < menor:
            menor = n
            #print(f"El menor de la lista es: {menor}") , me imprime 2 veces eñ resultado
        if n > mayor:
            mayor = n
            #print(f"El mayor de la lista es: {mayor}")

    print(f"el menor de la lista es: {menor}") 
    print(f"El mayor de la lista es: {mayor}")
minimo_maximo(lista) #se pone el dato a utilizar lista, se llama la función, si le pongo print al inicio no retorna nada None

def primos(n): #Primero se describe la condicion en la funcion y luego se llama
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lista = lista
lista_primos = []

for numero in lista:
    if primos(numero): #Aqui se llama a la funcion
        lista_primos.append(numero)

print(f"Números primos en la lista:  {lista_primos}" )



#Errores

'''
def numero_primo(inicial,final):

    lista1= lista
    for n in range(inicial,final+1):
        contador= 0

        for i in range(1,n+1):
            if n%i == 0:
                contador +=1
        if contador==2:
            lista1.append(n)
    return lista1
lista1=lista
print(numero_primo())



def numero_primo(numb):
    for n in lista:
        for m in range(1):
        
            if n%m == 0:
                pass
                     
            else:

    print(f"El {n} es un numero primo")
    
numero_primo(lista)
'''

    

        
