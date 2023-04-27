def Producto(dicc):
    n=''
    while n!= 'salir':
        n=input('Ingrese el alimento para saber el valor base y su iva, de lo contrario, escriba "salir" para terminar:')
        if n=='salir':
            break
        else: 
            precio=float(input('Ingrese el valor neto del producto del mercado actual: '))
            iva=dicc[n]*precio
            print(f'\nEl valor base del producto "{n}" es: {precio-iva}\nEl valor del IVA es: {iva}')