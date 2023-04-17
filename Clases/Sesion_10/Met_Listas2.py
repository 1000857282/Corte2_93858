milista = [3,5,7,5]
opc = " " 
while  opc != "salir":#1: #mientars verdadero, como es cilo sigue agragando numeros, guarda el numero anterior agregado
    
    opc = input("¿Que metodo desea utilizar?: ")
    
    if opc == "borrar":
        dato = int(input("¿Cual dato quiere borrar?"))
        milista.remove(dato)
        print(milista)

    elif opc == "limpiar":
        milista.clear()
        print(milista)

    elif opc == "agregar":
        dato = int(input("¿Cual dato quiere agregar?"))
        milista.append(dato)
        print(milista)


    elif opc == "buscar":
        dato = int(input("¿Cual dato quiere buscar?"))
        pos = milista.index(dato)
        print(f"el indice es {pos} ")


    elif opc == "insertar":
        dato = int(input("¿Cual dato quiere insertar?"))
        idx = int(input("Ingrese un indice: "))
        milista.insert(idx,dato)
        print(milista)

    elif opc == "sacar": #Sacar de la lista
        idx = int(input("Indice del numero a sacar: "))
        milista.pop(idx)
        print(milista)

    elif opc == "comparar": #Sacar maximos y minimos
        print(f"El valor maximo de la lista es: {max(milista)} ")
        print(f"El valor minimo de la lista es: {min(milista)} ")

    elif opc == "contar":
        dato= int(input("¿Qué numero desea revisar"))
        con = milista.count(dato)
        print(f"El numero {dato} esta {con} veces en la lista")

    elif opc== "sumar":
        print(f"Los elementos de la lista suman{sum(milista)}")

    elif opc == "comprobar":
        dato= int(input("¿Qué numero desea comprobar"))
        valor = dato in milista 
        print(valor)
        #print(dato in milista): otra manera de expresarlo

    elif opc == "extender":
        dato= int(input("¿Qué datos desea unir"))
        OtraLista = [ 1,2,3,4]
        milista.extend(OtraLista)
        print(milista)

    elif opc == "ascender":
        milista.sort()
        print(milista)
     

    elif opc == "invertir":
        #milista.reverse() depronto codigo de otro programa
        milista.sort(reverse=True)
        print(milista) 
    #milista.append(opc)#insertar
    #milista.insert(2,opc) #lo pone en la posicion despues del 5, osea posicion 2
        print(milista)