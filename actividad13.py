estudiantes={} #Diccionario en donde se guardaran a los estudiantes
def agregar_estudiante(): #Funcion para agregar un estudiante
    try:
        while True:
            carnet = input("Ingrese el carnet del estudiante: ") #Va a pedir los datos y si el usuario lo deja vacio entonces le dira que no se puede y le pedira que ingresa nuevamente el dato
            if not carnet:
                print("El carnet no puede estar vacio")
            elif carnet in estudiantes:
                print("El carnet ya ha sido registrado.")
            else:
                break   #Si el usuario ingresa todo bien entonces pasara con el siguiente dato
        while True: #Se inicia con otro bucle para el campo de nombre con la misma logica para que no se deje el campo vacio
            nombre= input("Ingrese el nombre del estudiante: ")
            if not nombre:
                print("El nombre no puede estar vacio")
            else:
                break
        while True:
            carrera= input("Ingrese la carrera o programa academico: ")
            if not carrera:
                print("La carrera no puede estar vacia.")
            else:
                break
        estudiantes[carnet]={    #Se agrega los datos en el diccionario de estudiantes dejando como campo unico al carnet
            "nombre":nombre,
            "carrera":carrera,
            "cursos":{} #Cursos seria el subdiccionario en donde se van a guardar los cursos del estudiante
        }
        print("Estudiante agregado.")
    except Exception as e:
        print("Error al agregar el estudiante:", e)
    finally:
        print("Volviendo al menu principal...")
def agregar_curso(): #Funcion para agregar cursos
    try:
        carnet= input("Ingrese el carnet para agregarle un curso: ")
        if carnet in estudiantes: #Se le pide un carnet al usuario para agregar el curso al estudiante con ese carnet
            while True:
                curso= input("Ingrese el nombre del curso: ")
                if not curso:
                    print("El curso no puede estar vacio")
                else:
                    break
            while True:
                nota= int(input("Ingrese la nota final: "))
                if nota <0 or nota >100: #Se hace una condicion para que la nota sea entre 0 y 100
                    print("Nota invalida")
                else:
                    break
            estudiantes[carnet]["cursos"][curso]=nota #Aqui se agregarian los datos del curso y nota en el subdiccionario de cursos que esta en el diccionario de estudiantes
            print("Curso agregado.")
        else:
            print("Carnet no encontrado.")
            return
    except ValueError:
        print("Error: La nota debe ser un numero entero") #Se deja el error de que dentro de las notas solo pueden ser numeros enteros
    except Exception as e:
        print("Error al agregar el curso:", e)
    finally:
        print("Volviendo al menu principal")
def consultar_estudiante():
    try:
        carnet= input("Ingrese el carnet del estudiante a consultar: ")
        #Se pide el carnet y si esta en el diccionario va a mostrar toda la informacion segun ese carnet
        if carnet in estudiantes:
            print(f"Nombre: {estudiantes[carnet]["nombre"]}")
            print(f"Carrera: {estudiantes[carnet]["carrera"]}")
            if estudiantes[carnet]["cursos"]: #Si tiene cursos registrados los mostrara de lo contrario no
                print("Cursos y notas: ")
                for curso, nota in estudiantes[carnet]["cursos"].items():
                    print(f"-Curso: {curso} | Nota: {nota}")
            else:
                print("No tiene cursos registrados")
        else:
            print("Carnet no encontrado")
            return
    except Exception as e:
        print("Error al consultar estudiante: ",e)
def calcular_promedio():
    try:
        carnet= input("Ingrese el carnet del estudiante a calcular su promedio: ")
        if carnet in estudiantes:
            promedio = sum(estudiantes[carnet]["cursos"].values())/len(estudiantes[carnet]["cursos"])
        #Si esta el carnet en el diccionario se hara el promedio sumando todas las notas del estudiante dividiendolas con la cantidad de cursos que tiene registrados
            print(f"El promedio de notas es: {promedio:.2f}")
        else:
            print("Carnet no encontrado")
            return
    except ZeroDivisionError: #Se lanzara un error por si no hay notas registradas por lo que no se podra realizar el promedio
        print("Error: no se puede calcular el promedio sin notas agregadas.")
    except Exception as e:
        print("Error al calcular el promedio: ",e)
def verificar_aprobacion():
    try:
        carnet= input("Ingrese el carnet a verificar: ")
        if carnet in estudiantes:
            if estudiantes[carnet]["cursos"]:
                for curso, nota in estudiantes[carnet]["cursos"].items(): #Se ira validando cada nota del carnet
                    if nota < 61:
                        print(f"No aprueba el curso: {curso} (nota: {nota})") #Si alguna nota es menor a 61 le indicara que curso no aprobo y la nota que obtuvo
                        return
                print("Aprueba todos los cursos") #Si todas las notas son mayores o iguales a 61 imprimira esto
            else:
                print("El estudiante no tiene cursos registrados.")
        else:
            print("Carnet no encontrado")
    except Exception as e:
        print("Error al verificar aprobacion: ",e)
def mostrar_estudiantes():
    try:
        if estudiantes: #Si hay estudiantes en el diccionario se imprimira la informacion de cada uno y si tienen cursos igualmente
            for carnet, datos in estudiantes.items():
                print(f"\nCarnet: {carnet}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Carrera: {datos["carrera"]}")
                if datos["cursos"]:
                    print("Cursos:")
                    for curso, nota in datos["cursos"].items():
                        print(f"-Curso: {curso} | Nota: {nota}")
                else:
                    print("No tiene cursos registrados")
        else: #Si no hay nada en el diccionario mostrara este mensaje
            print("No hay estudiantes registrados")
    except Exception as e:
        print("Error al mostrar todos los estudiantes: ",e)
while True: #Se mostrara el menu y se le pedira una opcion al usuario hasta que salga del programa
    print("MENU")
    print("1. Agregar un estudiante")
    print("2. Agregar un curso a un estudiante")
    print("3. Consultar un estudiante")
    print("4. Calcular promedio de un estudiante")
    print("5. Verificar si un estudiante aprueba")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion: #En cada opcion se llamara a la funcion correspondiente
        case "1":
            agregar_estudiante()
        case "2":
            agregar_curso()
        case "3":
            consultar_estudiante()
        case "4":
            calcular_promedio()
        case "5":
            verificar_aprobacion()
        case "6":
            mostrar_estudiantes()
        case "7":
            print("Saliendo del programa...") #Se termina el programa
            break
        case _:
            print("Opcion invalida, ingrese una opcion valida.") #Por si el usuario no ingresa una de las opciones