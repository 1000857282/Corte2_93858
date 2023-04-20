import random as rand

for i in range(0,5): #(0,5,2)--> el 2 es un salto , va de dos en dos 
    numero = rand.randint(10,20) #Randint:simular una situación de sorteo #ramdon.randrange(10,20,2)---> saca un numero dentro de este rango, el ultimo 2 es para que lo saque par
    real = round(rand.uniform(10,20),2) #uniform son los numeros decimales y round es redondear en 2
    letra = rand.choice("murcielago") #Elegir alguna de las letras aleatoriamente
    print(numero, end=" ")#El valor predeterminado de end es \n, lo que significa que después de la instrucción print imprimirá una nueva línea
    print(real,end=" " )#end= " " crea un espacion vacio y permite imprimir al lado
    print(letra,  " \n ")#\n da espacio en linea