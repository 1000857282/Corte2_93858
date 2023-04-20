 #clase
class Persona: #Crear clase

    #Constructor
    def __init__(self): #Self es el objeto
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.frase = None
    
    #Metodo
    def hablar(self):
        return self.frase #De estudiante retorne la frase
    
    #Instanciación

def main():
    estudiante = Persona()
    estudiante.nombre = "Nicol"
    estudiante.apellido = "Castillo"
    estudiante.edad = 19
    estudiante.frase = "Oh, debo estudiar"

    futbolista = Persona()
    futbolista.nombre = "Radamel"
    futbolista.apellido = "Garcia"
    futbolista.edad = 36
    futbolista.frase = "Goooolllll!"

    #Apuntador


    #Ejemplo 1.
    #print(id(Estudiante),Estudiante.nombre)
    #print(id(futbolista),futbolista.nombre)
    #futbolista = Estudiante #El futbolista es igual al nimbre por lo tanto, el dato de Radamel queda anonimo

    #print(id(Estudiante),Estudiante.nombre)
    #print(id(futbolista),futbolista.nombre)

    print(f"el estudiante dice:  {estudiante.hablar()}")
    print(f"el señor futbolista dice: {futbolista.hablar()}") #Vaya a la clase perosna del metodo hablar y busque futbolista hablar


if __name__== "__main__":
    main()


#vriable = minuscula  --> Ejmplico: is_digit
#Clases = las primeras letras son mayuscula y todo pegado ---> Ej: ClasePrincipal
#funciones = minusculas ---> Ej: funcion1
#campos = igual que las variables
#metodos= la segundo es mayuscula ---> metodoInicial