estudiantes={} #Diccionario en donde se guardaran a los estudiantes
def agregar_estudiante():
    try:
        while True:
            carnet = input("Ingrese el carnet del estudiante: ")
            if not carnet:
                print("El carnet no puede estar vacio")
            elif carnet in estudiantes:
                print("El carnet ya ha sido registrado.")
            else:
                break
        while True:
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
        estudiantes[carnet]={
            "nombre":nombre,
            "carrera":carrera,
            "cursos":{}
        }
        print("Estudiante agregado.")
    except Exception as e:
        print("Error al agregar el estudiante:", e)
    finally:
        print("Volviendo al menu principal...")
def agregar_curso():
    try:
        carnet= input("Ingrese el carnet para agregarle un curso: ")
        if carnet in estudiantes:
            while True:
                curso= input("Ingrese el nombre del curso: ")
                if not curso:
                    print("El curso no puede estar vacio")
                else:
                    break
            while True:
                nota= int(input("Ingrese la nota final: "))
                if nota <0 or nota >100:
                    print("Nota invalida")
                else:
                    break
            estudiantes[carnet]["cursos"][curso]=nota
            print("Curso agregado.")
        else:
            print("Carnet no encontrado.")
            return
    except ValueError:
        print("Error: La nota debe ser un numero entero")
    except Exception as e:
        print("Error al agregar el curso:", e)
    finally:
        print("Volviendo al menu principal")
def consultar_estudiante():
    try:
        carnet= input("Ingrese el carnet del estudiante a consultar: ")
        if carnet in estudiantes:
            print(f"Nombre: {estudiantes[carnet]["nombre"]}")
            print(f"Carrera: {estudiantes[carnet]["carrera"]}")
            if estudiantes[carnet]["cursos"]:
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
            print(f"El promedio de notas es: {promedio:.2f}")
        else:
            print("Carnet no encontrado")
            return
    except ZeroDivisionError:
        print("Error: no se puede calcular el promedio sin notas agregadas.")
    except Exception as e:
        print("Error al calcular el promedio: ",e)
def verificar_aprobacion():
    try:
        carnet= input("Ingrese el carnet a verificar: ")
        if carnet in estudiantes:
            if estudiantes[carnet]["cursos"]:
                for curso, nota in estudiantes[carnet]["cursos"].items():
                    if nota < 61:
                        print(f"No aprueba el curso: {curso} (nota: {nota})")
                        return
                    else:
                        print("Aprueba todos los cursos")
            else:
                print("El estudiante no tiene cursos registrados.")
        else:
            print("Carnet no encontrado")
    except Exception as e:
        print("Error al verificar aprobacion: ",e)
def mostrar_estudiantes():
    try:
        if estudiantes:
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
        else:
            print("No hay estudiantes registrados")
    except Exception as e:
        print("Error al mostrar todos los estudiantes: ",e)
while True:
    print("MENU")
    print("1. Agregar un estudiante")
    print("2. Agregar un curso a un estudiante")
    print("3. Consultar un estudiante")
    print("4. Calcular promedio de un estudiante")
    print("5. Verificar si un estudiante aprueba")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
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
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida, ingrese una opcion valida.")