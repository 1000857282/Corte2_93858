milista = [3,5,7]
while 1: #mientars verdadero, como es cilo sigue agragando numeros, guarda el numero anterior agregado
    opc = input("Ingrese un dato: ")
    
    if opc == "borrar":
        milista.clear()
    else:
        idx = int(input("Ingrese un indice: "))
        milista.insert(idx,opc)
    #milista.append(opc)#insertar
    #milista.insert(2,opc) #lo pone en la posicion despues del 5, osea posicion 2
        print(milista)