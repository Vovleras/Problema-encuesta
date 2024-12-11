import re
from clases import *
from listas import *

"""
Función que ordena los encuestados 
de acuerdo a la experticia
"""
def enc_orden_experticia(encuestados):

    lista_encuestados = Lista()
    for e in encuestados:
        lista_encuestados.agregar(e)

    #Modificar metodo de ordenamiento, para ordenar por experticia
    Encuestado.set_lt_method(lambda self, other: self.experticia > other.experticia)

    lista_encuestados.ordenar_insertion_sort()
    return lista_encuestados

"""
Función que obtiene las preguntas con mayor y menor promedio de opinion y experticia
"""
def resultados_preguntas(temas):
    total_preguntas = []
    for t in temas:
        for p in t.preguntas:
            total_preguntas.append(p)

    lista_preguntas = Lista()
    for e in total_preguntas:
        lista_preguntas.agregar(e)

    lista_preguntas.ordenar_insertion_sort()
    preg_mayor = lista_preguntas.obtener(0)
    preg_menor = lista_preguntas.obtener(lista_preguntas.tamaño() - 1)

    #Modificar metodo de ordenamiento para ordenar por experticia
    Pregunta.set_lt_method(lambda self, other: self.promedio_experticia() > other.promedio_experticia())
    
    lista_preguntas.ordenar_insertion_sort()
    preg_mayor_exp = lista_preguntas.obtener(0)
    preg_menor_exp = lista_preguntas.obtener(lista_preguntas.tamaño() - 1)

    return preg_mayor, preg_menor, preg_mayor_exp, preg_menor_exp

def escribir_resultado(listaTemas, encuestados):
    #Encuestados con mayor y menor opinion
    enc_mayor = encuestados[0]
    enc_menor = encuestados[len(encuestados)-1]
    #Encuestados con mayor y menor experticia
    ordenados_experticia = enc_orden_experticia(encuestados) #Encuestados ordenados por experticia
    enc_mayor_ex = ordenados_experticia.obtener(0)
    enc_menor_ex = ordenados_experticia.obtener(ordenados_experticia.tamaño() -1)
    #Preguntas con mayor y menor promedio de opinion y experticia
    preg_mayor, preg_menor, preg_mayor_ex, preg_menor_ex = resultados_preguntas(listaTemas)
    #Promedio de opinion y experticia de los encuestados
    prom_encuestados_op = round(sum([e.opinion for e in encuestados]) / len(encuestados), 2)
    prom_encuestados_ex = round(sum([e.experticia for e in encuestados]) / len(encuestados), 2)
    #Escribir en el archivo de resultados toda la infomación obtenida
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

"""
Función que permite crear encuestados y ordenarlos
"""
def ordenar_personas(lista_desordenada):
    encuestados = Lista()
    for i in lista_desordenada:
        datos = re.findall(r'\d+', i) #Se obtiene el id, la experticia y la opinion
        datos_numericos = [int(num) for num in datos]
        
        id = datos_numericos[0]
        nombre = i.split(",")[1]
        experticia = datos_numericos[1]
        opinion = datos_numericos[2]

        personaE = Encuestado(id, nombre, experticia, opinion)
        encuestados.agregar(personaE)
    
    encuestados.ordenar_insertion_sort()
    return encuestados

def ordenar_pregunta(pregunta, personas, nom_preg):
    orden = pregunta.strip("{}").split(", ")
    ids = [int(num) for num in orden]
    encuestados_desorden = Lista()

    for i in ids:
        encuestados_desorden.agregar(personas.obtener(i-1))
    
    encuestados_orden = ordenar_personas(encuestados_desorden.retornar())
    pregunta_lista = Pregunta(nom_preg, encuestados_orden.retornar()) #Aqui esta solo una pregunta
    
    return pregunta_lista

def ordenar_tema(cada_tema, encuestados, nombre):
    nombre_tema = nombre
    nombre_pregunta = 1 
    preguntas_orden = Lista()

    for i in cada_tema:
        nombre_texto = str(nombre_tema) + "." + str(nombre_pregunta)
        preguntas_orden.agregar(ordenar_pregunta(i, encuestados, nombre_texto))
        nombre_pregunta += 1

    preguntas_orden.ordenar_insertion_sort()

    tema_ordenado = Tema(nombre_tema, preguntas_orden.retornar())
    return tema_ordenado

def temas(info, total_encuestados):
    lista_temas = Lista()
    for i in range(1, len(info)):
        lista_temas.agregar(ordenar_tema(info[i].split("\n"), total_encuestados, i))

    lista_temas.ordenar_insertion_sort()

    print("Temas ordenados")
    return lista_temas

def asignar_id(encuestados_sin):
    lista_personas = encuestados_sin.split("\n")
    encuestados_desorden = Lista()

    for i in range(len(lista_personas)):
        encuestados_desorden.agregar(str(i+1) +", "+ lista_personas[i])
    
    return encuestados_desorden

""""""
def cargar_archivo(nombre):
    with open(nombre, "r", errors="ignore") as archivo:
        contenido = archivo.read()

    vector_informacion = [elemento.strip() for elemento in contenido.split("\n\n")]
    vector_informacion.pop()
    encuestados = asignar_id(vector_informacion[0])
    totalEOrdenados = ordenar_personas(encuestados.retornar())
    
    k = len(vector_informacion) - 2
    resultado_temas = temas(vector_informacion, encuestados)
    escribir_resultado(resultado_temas.retornar(), totalEOrdenados.retornar())
    
nombreArchivo = input("Ingrese el nombre del archivo: ")
cargar_archivo(nombreArchivo)