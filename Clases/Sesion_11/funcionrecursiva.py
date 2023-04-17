def imprimir(x):
    if x > 0:
        imprimir(x-1)
        print(x)

imprimir(5)
   

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('boooooom!')
    print('fin de funcion',num)

cuenta_atras(5)
