def busqueda_dicc():
    while n !="salir":
        n = input("Ingrese un key de busqueda")
        if n == "salir":
            break
        if n not in dicc:
            print("Error. Fuera de Rango")
        else:
            print(dicc[n])