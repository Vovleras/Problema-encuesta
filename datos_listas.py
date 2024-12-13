import re
import time
from clases import *
from lista import *

"""
Calcula el tiempo total de ejecución del programa, desde la carga del archivo
hasta la escritura de los resultados en "resultados.txt".
"""
def calcular_tiempo_ejecucion(nombre_archivo):
    # Capturar el tiempo de inicio
    tiempo_inicio = time.time()
    # Ejecutar el programa
    cargar_archivo(nombre_archivo)
    # Capturar el tiempo de finalización
    tiempo_fin = time.time()
    # Calcular el tiempo total en milisegundos
    tiempo_total_ms = (tiempo_fin - tiempo_inicio) * 1000

    with open("resultados.txt", "a") as archivo_resultados:
        archivo_resultados.write(f"\nTiempo total de ejecución del programa: {tiempo_total_ms:.2f} milisegundos\n")

#Funcion para prdenar encuestados por experticia y luego por id
def orden_experticia(self, other):
    if self.experticia != other.experticia:
            return self.experticia > other.experticia
    return self.id > other.id

"""
Función que ordena los encuestados 
de acuerdo a la experticia
"""
def enc_orden_experticia(encuestados):

    lista_encuestados = encuestados
    #Modificar metodo de ordenamiento, para ordenar por experticia
    Encuestado.set_lt_method(orden_experticia)

    lista_encuestados.ordenar_insertion_sort()
    return lista_encuestados

"""
Función que obtiene las preguntas con mayor y menor promedio de opinion y experticia
"""
def resultados_preguntas(temas):
    total_preguntas = Lista()
    for t in temas:
        for p in range(t.preguntas.tamaño()):
            pregunta = t.preguntas.obtener(p)
            total_preguntas.agregar(pregunta)

    total_preguntas.ordenar_insertion_sort()
    preg_mayor = total_preguntas.obtener(0)
    preg_menor = total_preguntas.obtener(total_preguntas.tamaño() - 1)

    #Modificar metodo de ordenamiento para ordenar por experticia
    Pregunta.set_lt_method(lambda self, other: self.promedio_experticia() > other.promedio_experticia())
    
    total_preguntas.ordenar_insertion_sort()
    preg_mayor_exp = total_preguntas.obtener(0)
    preg_menor_exp = total_preguntas.obtener(total_preguntas.tamaño() - 1)

    return preg_mayor, preg_menor, preg_mayor_exp, preg_menor_exp


def promedio_encuestados(encuestados, num):
    promedio = 0
    suma = 0
    for e in range(encuestados.tamaño()):
        if num == 1:
            suma += encuestados.obtener(e).opinion
        else:
            suma += encuestados.obtener(e).experticia
    
    promedio = suma / encuestados.tamaño()
    return round(promedio, 2)
        

def escribir_resultado(listaTemas, encuestados):
    #Promedio de opinion y experticia de los encuestados
    prom_encuestados_op = promedio_encuestados(encuestados, 1)
    prom_encuestados_ex = promedio_encuestados(encuestados, 2)
    #Encuestados con mayor y menor opinion
    enc_ordenados_op = encuestados.retornar()
    print(enc_ordenados_op)
    enc_mayor = encuestados.obtener(0)
    enc_menor = encuestados.obtener(encuestados.tamaño()-1)

    #Encuestados con mayor y menor experticia
    ordenados_experticia = enc_orden_experticia(encuestados) #Encuestados ordenados por experticia
    enc_mayor_ex = ordenados_experticia.obtener(0)
    enc_menor_ex = ordenados_experticia.obtener(ordenados_experticia.tamaño() -1)
    
    #Preguntas con mayor y menor promedio de opinion y experticia
    preg_mayor, preg_menor, preg_mayor_ex, preg_menor_ex = resultados_preguntas(listaTemas)
    #Escribir en el archivo de resultados toda la infomación obtenida
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados de la encuesta")
        for i in listaTemas:
            promedio = round(i.promedio_opinion(), 2)
            nombre = i.nombre
            archivo.write(f"\n[ {promedio} ] Tema {nombre}\n")

            for j in range(i.preguntas.tamaño()):
                pregunta = i.preguntas.obtener(j)
                promedio_pregunta = round(pregunta.promedio_opinion(), 2)
                nombre_pregunta = pregunta.nombre
                id_encuestados = pregunta.id_encuestados().retornar()
                archivo.write(f"  [ {promedio_pregunta} ] Pregunta {nombre_pregunta} : {id_encuestados}\n")

        archivo.write("\nLista de encuestados\n")
        [archivo.write(f" {enc_str}\n") for enc_str in enc_ordenados_op]
        print(enc_ordenados_op)
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
    pregunta_lista = Pregunta(nom_preg, encuestados_orden) #Aqui esta solo una pregunta
    
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

    tema_ordenado = Tema(nombre_tema, preguntas_orden)
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
    escribir_resultado(resultado_temas.retornar(), totalEOrdenados)
    
# nombreArchivo = input("Ingrese el nombre del archivo: ")
# cargar_archivo(nombreArchivo)
