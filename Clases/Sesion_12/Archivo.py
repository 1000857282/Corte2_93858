import busqueda

def main():
    dicc = {}
    f = open("matrizAsignacion.txt","rt")
    matriz = f.readlines()
    f.seek(0)
    suma = 0
    for i in range(len(matriz)):
        valor = f.readline().rstrip("\n").split(",")
        for j in range(len(valor)):
            pos = str(f"{i}{j}")
            dicc[pos]= valor[j]

            
       # print(valor)
        #suma +=int(valor[0])
        #print(suma)

    #print(suma)
    print(dicc)
    f.close

    busqueda.busqueda_dicc(dicc)
    #n = ""
    #while n !="salir":
        #n = input("Ingrese un key de busqueda")
        #if n == "salir":
            #break
        #if n not in dicc:
            #print("Error. Fuera de Rango")
        #else:
            #print(dicc[n])
    
    #print("43" in dicc)#Para saber si el dato se encuentra en la lista
    #print(f"la posicion 4.3 es {dicc['43']}") #Tener en cuenta las comillas, imprime la posicion
    #para elimimir cosa dentro del diccionario es --> del NombreDiccinario[llave]
    #f.close()#Cerrar la lectura del archivo
   

#matriz = f.read() --> Lee el archivo completo
#matriz = f.readline() ---> Lee e imprime una sola lista
#matriz = f.readlines() ----> Lee e imprime en forma de lista
#print(matriz)

if __name__=="__main__":
    main()

