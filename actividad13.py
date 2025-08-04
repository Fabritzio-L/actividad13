estudiantes={} #Diccionario en donde se guardaran a los estudiantes
def agregar_estudiante():
    try:
        carnet = input("Ingrese el carnet del estudiante")
        if not carnet:
            print("El carnet no puede estar vacio")
            return
        if carnet in estudiantes:
            print("El carnet ya ha sido registrado.")
            return
        nombre= input("Ingrese el nombre del estudiante: ")
        if not nombre:
            print("El nombre no puede estar vacio")
            return
        carrera= input("Ingrese la carrera o programa academico: ")
        if not carrera:
            print("La carrera no puede estar vacia.")
            return
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
            curso= input("Ingrese el nombre del curso: ")
            if not curso:
                print("El curso no puede estaer vacio")
                return
            nota= int(input("Ingrese la final: "))
            if nota <0 or nota >100:
                print("Nota invalida")
                return
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
                for curso, datos in estudiantes[carnet]["cursos"].items():
                    print(f"-Curso: {curso} | Nota: {datos["notas"]}")
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