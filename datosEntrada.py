import re
from clases import *
from insertionsort import *

def ordenarPersonas(listaDesordenada):
    #LLamar aqui al algoritmo de ordenamiento
    encuestados = []

    for i in listaDesordenada:
        datos = re.findall(r'\d+', i) #Se obtiene el id, la experticia y la opinion
        datosNumericos = [int(num) for num in datos] #Convertir a enteros 
        
        id = datosNumericos[0]
        nombre = i.split(",")[1]
        experticia = datosNumericos[1]
        opinion = datosNumericos[2]

        personaE = Encuestado(id, nombre, experticia, opinion)
        encuestados.append(personaE)
    
    # Crear la cola y cargar los encuestados
    cola_encuestados = ColaInsertionSort(max_length=len(encuestados) + 1)
    for e in encuestados:
        cola_encuestados.enqueue(e)

    # Ordenar
    cola_encuestados.ordenar_insertion_sort()
    encuestadosOrdenados = cola_encuestados.mostrar()
    return encuestadosOrdenados

def ordenarPregunta(pregunta, personas, nomPreg):
    orden = pregunta.strip("{}").split(", ")
    ids = [int(num) for num in orden]
    #listaPersonas = personas.split("\n")
    encuestadosDesorden = []

    for i in ids:
        encuestadosDesorden.append(personas[i-1])
    
    encuestadosOrden = ordenarPersonas(encuestadosDesorden)

    preguntaLista = Pregunta(nomPreg, encuestadosOrden) #Aqui esta solo una pregunta
    #print(preguntaLista.promedio_opinion()) #Solo es de prueba
    #return encuestadosOrden
    return preguntaLista

def ordenarTema(cadaTema, encuestados):
    nombrePregunta = 1 #Es el nombre de la pregunta, se debe modificar segun corresponda
    preguntasOrden = [] #Lista que contiene las preguntas ordenadas    
    for i in cadaTema:
        preguntasOrden.append(ordenarPregunta(i, encuestados, nombrePregunta))
        nombrePregunta += 1

    # Crear la cola y cargar las preguntas
    cola_preguntas = ColaInsertionSort(max_length=len(preguntasOrden) + 1)
    for e in preguntasOrden:
        cola_preguntas.enqueue(e)

    # Ordenar
    cola_preguntas.ordenar_insertion_sort()
    pregOrdenadas = cola_preguntas.mostrar() #Aqui estan las preguntas ordenadas en el tema

    #print(pregOrdenadas)
    return pregOrdenadas

def temas(info, totalEncuestados):
    temas = []
    for i in range(1, len(info)):
        temas.append(ordenarTema(info[i].split("\n"), totalEncuestados))

    # Crear la cola y cargar los encuestados
    cola_temas = ColaInsertionSort(max_length=len(temas) + 1)
    for t in temas:
        cola_temas.enqueue(t)

    # Ordenar
    cola_temas.ordenar_insertion_sort()
    temasOrdenados = cola_temas.mostrar()

    print("Temas", temasOrdenados, "Fin temas")

def asignarID(encuestadosSin):
    listaPersonas = encuestadosSin.split("\n")
    encuestadosDesorden = []

    for i in range(len(listaPersonas)):
        encuestadosDesorden.append(str(i+1) +", "+ listaPersonas[i])
    
    return encuestadosDesorden


def cargarArchivo():
    nombre = input("Ingresa el nombre del archivo que deseas cargar: ")
    with open(nombre, "r") as archivo:
        contenido = archivo.read()

    vectorInformacion = [elemento.strip() for elemento in contenido.split("\n\n")]
    encuestados = asignarID(vectorInformacion[0])
    totalEOrdenados = ordenarPersonas(encuestados)
    print(totalEOrdenados)
    k = len(vectorInformacion) - 2
    temas(vectorInformacion, encuestados)
    

cargarArchivo()