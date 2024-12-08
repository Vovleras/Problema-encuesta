import re
from clases import *
from insertionsort import *

def enc_orden_experticia(encuestados):
    # Crear la cola y cargar los encuestados
    cola_encuestados = ColaInsertionSort(max_length=len(encuestados) + 1)
    for e in encuestados:
        cola_encuestados.enqueue(e)

    #Modificar metodo de ordenamiento
    Encuestado.set_lt_method(lambda self, other: self.experticia > other.experticia)

    # Ordenar
    cola_encuestados.ordenar_insertion_sort()
    encuestadosOrdenados = cola_encuestados.mostrar()
    return encuestadosOrdenados

def resultados_preguntas(temas):
    total_preguntas = []

    for t in temas:
        for p in t.preguntas:
            total_preguntas.append(p)

    print(total_preguntas)
    # Crear la cola y cargar las preguntas
    cola_preguntas = ColaInsertionSort(max_length=len(total_preguntas) + 1)
    for e in total_preguntas:
        cola_preguntas.enqueue(e)

    # Ordenar
    cola_preguntas.ordenar_insertion_sort()
    preg_ordenadas = cola_preguntas.mostrar() #Aqui estan las preguntas ordenadas en el tema

    print(preg_ordenadas)
    preg_mayor = preg_ordenadas[0]
    preg_menor = preg_ordenadas[len(preg_ordenadas)-1]

    #Modificar metodo de ordenamiento
    Pregunta.set_lt_method(lambda self, other: self.promedio_experticia() > other.promedio_experticia())
    # Ordenar
    cola_preguntas.ordenar_insertion_sort()
    preg_ordenadas_exp = cola_preguntas.mostrar()
    print(preg_ordenadas_exp)
    preg_mayor_exp = preg_ordenadas_exp[0]
    preg_menor_exp = preg_ordenadas_exp[len(preg_ordenadas)-1]

    return preg_mayor, preg_menor, preg_mayor_exp, preg_menor_exp

def escribir_resultado(listaTemas, encuestados):

    enc_mayor = encuestados[0]
    enc_menor = encuestados[len(encuestados)-1]

    ordenados_experticia = enc_orden_experticia(encuestados) #Encuestados ordenados por experticia
    enc_mayor_ex = ordenados_experticia[0]
    enc_menor_ex = ordenados_experticia[len(ordenados_experticia)-1]

    preg_mayor, preg_menor, preg_mayor_ex, preg_menor_ex = resultados_preguntas(listaTemas)

    prom_encuestados_op = round(sum([e.opinion for e in encuestados]) / len(encuestados), 2)
    prom_encuestados_ex = round(sum([e.experticia for e in encuestados]) / len(encuestados), 2)



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
        archivo.write("\nResultados:\n")
        archivo.write(f"Pregunta con mayor promedio de opinion: [{round(preg_mayor.promedio_opinion(), 2)}] {preg_mayor.nombre}\n")
        archivo.write(f"Pregunta con menor promedio de opinion: [{round(preg_menor.promedio_opinion(), 2)}] {preg_menor.nombre}\n")
        archivo.write(f"Pregunta con mayor promedio de experticia: [{round(preg_mayor_ex.promedio_experticia(), 2)}] {preg_mayor_ex.nombre}\n")
        archivo.write(f"Pregunta con menor promedio de experticia: [{round(preg_menor_ex.promedio_experticia(), 2)}] {preg_menor_ex.nombre}\n")
        archivo.write(f"Encuestado con mayor opinion: {enc_mayor}\n")
        archivo.write(f"Encuestado con menor opinion: {enc_menor}\n")
        archivo.write(f"Encuestado con mayor experticia: {enc_mayor_ex}\n")
        archivo.write(f"Encuestado con menor experticia: {enc_menor_ex}\n")
        archivo.write(f"Promedio de experticia de los encuestados: {prom_encuestados_ex}\n")
        archivo.write(f"Promedio del valor de opinion de los encuestados: {prom_encuestados_op}\n")
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