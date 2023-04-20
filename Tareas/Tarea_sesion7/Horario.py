#Realice un programa donde se pueda consultar su horario de clases, de modo que ingresando el nombre de la materia indique el dia de clase,la hora, el salón y el nombre del profesor.

calculo = ["Dia: Martes", "Hora: 7:00", "Salon: 407 DB", "Profesor: Edwin Julian Acuña"]
fisica = ["Dia: Martes", "Hora: 9:00", "Salon: 105 PS", "Profesor: Paula Andrea Mora"]
programacion = ["Dia: Martes", "Hora: 13:00", "Salon: 303 PS", "Profesor: David Nicolas Torres Barrera"]
materiales = ["Dia: Miercoles", "Hora: 9:00", "Salon: 407 DB", "Profesor: Elmer Cepeda Gomez"]
dibujo = ["Dia: Miercoles", "Hora: 11:00", "Salon: 407 DB", "Profesor: Elmer Cepeda Gomez"]
circuitos = ["Dia: Miercoles", "Hora: 13:00", "Salon: 204 PS", "Profesor: Hernan Pineda"]

opc = ""

while  opc != "salir":
    opc = str(input("Ingrese la materia que desea consultar: "))

    if opc == "calculo":
        print(f"La materia que usted eligio tiene el siguiente horario:  {calculo}")

    elif opc == "fisica":
        print(f"La materia que usted eligio tiene el siguiente horario:  {fisica}")

    elif opc == "programacion":
        print(f"La materia que usted eligio tiene el siguiente horario:  {programacion}")

    elif opc == "materiales":
        print(f"La materia que usted eligio tiene el siguiente horario:  {materiales}")

    elif opc == "dibujo":
        print(f"La materia que usted eligio tiene el siguiente horario:  {dibujo}")

    elif opc == "circuitos":
        print(f"La materia que usted eligio tiene el siguiente horario:  {circuitos}")

