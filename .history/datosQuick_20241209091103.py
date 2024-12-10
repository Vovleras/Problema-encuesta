from clases import *
from algoritmos import *

# Abre el archivo 'datos.txt' en modo de lectura
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()

lines = data.split('\n')
print(length(lines))

# Inicializa una lista para almacenar los encuestados
A = Pila(12)

contador_id = 1

# Inicializa una pila para almacenar las preguntas
pregunta_1_1 = Pila(10)
pregunta_1_2 = Pila(10)
pregunta_2_1 = Pila(10)
pregunta_2_2 = Pila(10)

# Variable para llevar la cuenta de las preguntas
pregunta_actual = 1

# Recorre cada línea del archivo
for line in lines:
    # Verifica si la línea contiene información de encuestado
    if 'Experticia' in line and 'Opinión' in line:
        parts = line.split(',')
        nombre = parts[0].strip()
        experticia = int(parts[1].split(':')[1].strip())
        opinion = int(parts[2].split(':')[1].strip())

        encuestado = Encuestado(contador_id, nombre, experticia, opinion)

        contador_id += 1

        A.push(encuestado)

    # Verifica si la línea contiene un conjunto de encuestados para una pregunta
    elif '{' in line and '}' in line:
        # Extrae los IDs de encuestados de la línea
        ids_str = line.replace('{', '').replace('}', '').strip()
        ids = [int(id_str) for id_str in ids_str.split(',')]
        
        # Dependiendo de la pregunta actual, añade los IDs a la pila correspondiente
        if pregunta_actual == 1:
            for id in ids:
                pregunta_1_1.push(id)
        elif pregunta_actual == 2:
            for id in ids:
                pregunta_1_2.push(id)
        elif pregunta_actual == 3:
            for id in ids:
                pregunta_2_1.push(id)
        elif pregunta_actual == 4:
            for id in ids:
                pregunta_2_2.push(id)
        
        # Incrementa el contador de preguntas
        pregunta_actual += 1

def calcular_promedio(pila_pregunta, A, tipo='opinion'):
    suma = 0
    cantidad_encuestados = 0

    # Suponiendo que size es un atributo
    pila_temp = Pila(pila_pregunta.size)

    while not pila_pregunta.stackEmpty():
        # Obtenemos el ID de los encuestados de la pila de la pregunta
        id_encuestado = pila_pregunta.pop()

        # Accedemos al encuestado en la pila A usando el ID
        encuestado = accederPosicion(A, id_encuestado - 1)  # Ajustamos el índice porque las pilas son 0-indexadas

        # Dependiendo del tipo de promedio, sumamos la opinión o la experticia
        if tipo == 'opinion':
            suma += encuestado.opinion
        elif tipo == 'experticia':
            suma += encuestado.experticia
        cantidad_encuestados += 1

        # Poner el ID en la pila temporal
        pila_temp.push(id_encuestado)

    # Devolvemos la pila de vuelta a su estado original
    while not pila_temp.stackEmpty():
        pila_pregunta.push(pila_temp.pop())

    if cantidad_encuestados > 0:
        return suma / cantidad_encuestados
    else:
        return 0

 # Calcular el promedio para las opiniones de cada pregunta
promedio_opinion_1_1 = calcular_promedio(pregunta_1_1, A, tipo='opinion')
promedio_opinion_1_2 = calcular_promedio(pregunta_1_2, A, tipo='opinion')
promedio_opinion_2_1 = calcular_promedio(pregunta_2_1, A, tipo='opinion')
promedio_opinion_2_2 = calcular_promedio(pregunta_2_2, A, tipo='opinion')

# Calcular el promedio para las experticias de cada pregunta
promedio_experticia_1_1 = calcular_promedio(pregunta_1_1, A, tipo='experticia')
promedio_experticia_1_2 = calcular_promedio(pregunta_1_2, A, tipo='experticia')
promedio_experticia_2_1 = calcular_promedio(pregunta_2_1, A, tipo='experticia')
promedio_experticia_2_2 = calcular_promedio(pregunta_2_2, A, tipo='experticia')

# Promedio de los promedios de opinión para el Tema 1 y Tema 2
promedio_opinion_tema_1 = (promedio_opinion_1_1 + promedio_opinion_1_2) / 2
promedio_opinion_tema_2 = (promedio_opinion_2_1 + promedio_opinion_2_2) / 2

# Promedio de los promedios de experticia para el Tema 1 y Tema 2
promedio_experticia_tema_1 = (promedio_experticia_1_1 + promedio_experticia_1_2) / 2
promedio_experticia_tema_2 = (promedio_experticia_2_1 + promedio_experticia_2_2) / 2

# Promedio de los promedios de opinión y experticia
promedio_opinion_total = (promedio_opinion_tema_1 + promedio_opinion_tema_2) / 2
promedio_experticia_total = (promedio_experticia_tema_1 + promedio_experticia_tema_2) / 2


