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
    except Exception as e:
        print("Error al agregar el estudiante:", e)
    finally:
        print("Volviendo al menu principal...")
