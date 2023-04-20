#Programa con Setters y getters

class Personas:
    def _init_(self):

        #Atributos constructor
        self.__nombre = None  #--- #-- Metodo privado
        self.__altura = None
        self.__peso = None

    #------------Getters---------------------- Get--> toma datos
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura
    
    def getPeso(self):
        return self.__peso


    #------------Setters---------------------- set ->modifica los datos
    def setNombre(self, nombre:str): #Variable nombre sea siempre tipo string
        self.__nombre = nombre #nombre--

    def setAltura(self, altura:int):
        self.__altura = altura
    
    def setPeso(self,peso:int):
        self.__peso = peso



#Clases,campos metodos
    #------------Metodo IMC
    def getIMC(self):
        return self.__Indice()


        #Metodo
    def __Indice(self):
        IMC = self.__peso/((self.__altura/100)**2) #Aqui se hace la conversion de centimetros a metros

        #Condición
        if IMC <= 18.5:
            return str("Por debajo")
        elif IMC <=24.9:
            return str("Saludable")
        elif IMC <=29.9:
            #print(IMC) Imprime IMC
            return str("Sobre peso")
        elif IMC <=34.9:
            return str("Obesidad I")
        elif IMC <=39.9:
            return str("Obesidad II")
        else:
            return str("Obesidad III")
'''''
def main():
    entrada = []
    for i in range(3):
        entrada.append(input('Entrada: '))

    estudiante = Personas()
    estudiante.setNombre(entrada[0]) #Aqui se ingresa el cambio
    estudiante.setPeso(int(entrada[1]))
    estudiante.setAltura(float(entrada[2])) 
    print(f'Su IMC es: {estudiante.getIMC()}')
'''''
'''''
def main():
    estudiante = Personas()
    estudiante.setNombre("Nicol") #Aqui se ingresa el cambio
    estudiante.setPeso(554)
    estudiante.setAltura(155) 
    print(f'Su IMC es: {estudiante.getIMC()}')      
'''''


#instancia es la creacion del objeto
def main():
    estudiante = Personas()
    estudiante.setNombre("Nicol") #Aqui se ingresa el cambio
    estudiante.setPeso(554)
    estudiante.setAltura(155) 
    print(f'Su IMC es: {estudiante.getIMC()}')     
'''''
    estudiante1 = Personas() #Se llma a la clase y se crea los siguientes atributos
    estudiante1.nombre = "Pedro Caceres"
    estudiante1.altura = 188
    estudiante1.peso = 97


    estudiante2 = Personas()
    estudiante2.nombre = "Maria Perez"
    estudiante2.altura = 160
    estudiante2.peso = 47


    estudiante3 = Personas()
    estudiante3.nombre = "Julian Domingues"
    estudiante3.altura = 158
    estudiante3.peso = 58

    estudiante4 = Personas()
    estudiante4.nombre = "Jessica fuentes"
    estudiante4.altura = 170
    estudiante4.peso = 73
'''''
    
'''''
    print(f"Estudiante: {estudiante1.nombre} resultado: {estudiante1.Indice()}")
    print(f"Estudiante: {estudiante2.nombre} resultado: {estudiante2.Indice()}")
    print(f"Estudiante: {estudiante3.nombre} resultado: {estudiante3.Indice()}")
    print(f"Estudiante: {estudiante4.nombre} resultado: {estudiante4.Indice()}")
'''''


if __name__== "__main__":
    main()
