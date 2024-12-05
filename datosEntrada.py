def ordenarPersonas(listaDesordenada):
    #LLamar aqui al algoritmo de ordenamiento
    return 0

def ordenarPregunta(pregunta, personas):
    orden = pregunta.strip("{}").split(", ")
    ids = [int(num) for num in orden]
    listaPersonas = personas.split("\n")
    encuestadosDesorden = []

    for i in ids:
        encuestadosDesorden.append(str(i) +", "+ listaPersonas[i-1])

    encuestadosOrden = ordenarPersonas(encuestadosDesorden)

    return encuestadosDesorden

def ordenarTema(cadaTema, encuestados):
    preguntasOrden = [] #Lista que contiene las preguntas ordenadas    
    for i in cadaTema:
        preguntasOrden.append(ordenarPregunta(i, encuestados))
    return preguntasOrden

def temas(info):
    temas = []
    for i in range(1, len(info)):
        temas.append(ordenarTema(info[i].split("\n"), info[0]))

    
    
    print("Temas", temas, "Fin temas")

def cargarArchivo():
    nombre = input("Ingresa el nombre del archivo que deseas cargar: ")
    with open(nombre, "r") as archivo:
        contenido = archivo.read()

    vectorInformacion = [elemento.strip() for elemento in contenido.split("\n\n")]
    encuestados = vectorInformacion[0]
    k = len(vectorInformacion) - 2
    temas(vectorInformacion)
    

cargarArchivo()