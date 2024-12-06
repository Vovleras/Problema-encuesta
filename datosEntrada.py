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

    preguntaLista = Pregunta(nomPreg, encuestadosOrden)
    print(preguntaLista.promedio_opinion()) #Solo es de prueba
    #return encuestadosOrden
    return preguntaLista

def ordenarTema(cadaTema, encuestados):
    nombrePregunta = 1 #Es el nombre de la pregunta, se debe modificar segun corresponda
    preguntasOrden = [] #Lista que contiene las preguntas ordenadas    
    for i in cadaTema:
        preguntasOrden.append(ordenarPregunta(i, encuestados, nombrePregunta))
        nombrePregunta += 1
    return preguntasOrden

def temas(info, totalEncuestados):
    temas = []
    for i in range(1, len(info)):
        temas.append(ordenarTema(info[i].split("\n"), totalEncuestados))

    print("Temas", temas, "Fin temas")

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