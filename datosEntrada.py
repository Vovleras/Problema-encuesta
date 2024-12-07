import re
from clases import *
from insertionsort import *

def escribir_resultado(listaTemas, encuestados):

    enc_mayor = encuestados[0]
    enc_menor = encuestados[len(encuestados)-1]

    with open("resultados.txt", "w") as archivo:

        archivo.write("Resultados de la encuesta")

        for i in listaTemas:
            promedio = round(i.promedio_opinion(), 2)
            nombre = i.nombre
            archivo.write(f"\n[ {promedio} ] Tema {nombre}\n")

            for j in i.preguntas:
                promedio_pregunta = round(j.promedio_opinion(), 2)
                nombre_pregunta = j.nombre
                id_encuestados = [enc.id for enc in j.encuestados]
                archivo.write(f"  [ {promedio_pregunta} ] Pregunta {nombre_pregunta} : {id_encuestados}\n")

        archivo.write("\nLista de encuestados\n")
        [archivo.write(f" {enc_str}\n") for enc_str in encuestados]
        archivo.write("\nResultado:\n")
        archivo.write(f"Encuestado con mayor opinion: {enc_mayor}\n")
        archivo.write(f"Encuestado con menor opinion: {enc_menor}\n")
    print(1)

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

def ordenarTema(cadaTema, encuestados, nombre):
    nombre_tema = nombre
    nombrePregunta = 1 #Es el nombre de la pregunta, se debe modificar segun corresponda
    preguntasOrden = [] #Lista que contiene las preguntas ordenadas    
    for i in cadaTema:
        nombre_texto = str(nombre_tema) + "." + str(nombrePregunta)
        preguntasOrden.append(ordenarPregunta(i, encuestados, nombre_texto))
        nombrePregunta += 1

    # Crear la cola y cargar las preguntas
    cola_preguntas = ColaInsertionSort(max_length=len(preguntasOrden) + 1)
    for e in preguntasOrden:
        cola_preguntas.enqueue(e)

    # Ordenar
    cola_preguntas.ordenar_insertion_sort()
    pregOrdenadas = cola_preguntas.mostrar() #Aqui estan las preguntas ordenadas en el tema

    temaOrdenado = Tema(nombre_tema, pregOrdenadas)
    #print(pregOrdenadas)
    return temaOrdenado

def temas(info, totalEncuestados):
    temas = []
    for i in range(1, len(info)):
        temas.append(ordenarTema(info[i].split("\n"), totalEncuestados, i))

    # Crear la cola y cargar los encuestados
    cola_temas = ColaInsertionSort(max_length=len(temas) + 1)
    for t in temas:
        cola_temas.enqueue(t)

    # Ordenar
    cola_temas.ordenar_insertion_sort()
    temasOrdenados = cola_temas.mostrar()

    print("Temas", temasOrdenados, "Fin temas")
    return temasOrdenados

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
    resultado_temas = temas(vectorInformacion, encuestados)
    escribir_resultado(resultado_temas, totalEOrdenados)
    #escribir_promedios_op(totalEOrdenados, resultado_temas)
    

cargarArchivo()