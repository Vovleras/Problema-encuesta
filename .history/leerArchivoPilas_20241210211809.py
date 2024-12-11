from clases import *
from algoritmos import *

def obtener_data(nombre):
    with open(nombre, 'r', encoding='utf-8') as file:
        data = file.read()

    segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]

    # Extraemos la información de los encuestados
    encuestados_str = segments[0]
    encuestados = []
    for line in encuestados_str.split('\n'):
        if line.strip():
            # Extraemos la información de cada encuestado
            parts = line.strip().split(", ")
            nombre = parts[0]
            experticia = int(parts[1].split(": ")[1])
            opinion = int(parts[2].split(": ")[1].strip(','))
            encuestado = Encuestado(len(encuestados) + 1, nombre, experticia, opinion)
            encuestados.append(encuestado)

    # Extraemos los temas y preguntas
    cantidad_temas = len(segments) - 1
    lista_tema = []

    for i in range(1, cantidad_temas + 1):
        temas = segments[i]
        temas = [line.strip() for line in temas.split('\n') if line.strip()]
        pregunta_por_tema = []

        for tema in temas:
            numeros = [int(num) for num in tema.strip("{}").split(", ")]
            pregunta_por_tema.append(numeros)

        # Crear una lista de objetos Pregunta para cada tema
        preguntas = []
        for idx, pregunta in enumerate(pregunta_por_tema):
            # En vez de asignar todos los encuestados a la pregunta, solo asignamos sus IDs
            pregunta_obj = Pregunta(f"Pregunta {i}.{idx + 1}", pregunta)  # Asignamos solo los IDs de los encuestados
            preguntas.append(pregunta_obj)

        tema_obj = Tema(f"Tema {i}", preguntas)
        lista_tema.append(tema_obj)

    # Convertir la lista de encuestados en una pila
    encuestados_pila = Pila(len(encuestados))
    for encuestado in encuestados:
        encuestados_pila.push(encuestado)

    # Convertir cada lista de preguntas en pilas, donde cada pila de pregunta contiene los IDs de los encuestados
    lista_tema_pilas = Pila(cantidad_temas)  # Crear una pila para los temas
    for tema in lista_tema:
        pila_tema = Pila(len(tema.preguntas))  # Crear una pila para cada tema
        for pregunta in tema.preguntas:
            pila_pregunta = Pila(len(pregunta.encuestados))  # Crear una pila para cada pregunta
            for encuestado_id in pregunta.encuestados:
                pila_pregunta.push(encuestado_id)  # Llenar la pila con los IDs de los encuestados
            pila_tema.push(pila_pregunta)  # Añadir la pila de la pregunta a la pila del tema
        lista_tema_pilas.push(pila_tema)  # Añadir la pila del tema a la pila de temas

    return [encuestados_pila, lista_tema_pilas]

resultado = obtener_data('datos.txt')
pila_encuestados = resultado[0]
pila_temas = resultado[1]

# Imprimir las Pilas
print("Pila Encuestados:", pila_encuestados)
print("Pila Tema 1:", pila_temas.pila[0])
print("Pila Tema 2:", pila_temas.pila[1])
print("Pila Pregunta 1.1:", pila_temas.pila[0].pila[0])
print("Pila Pregunta 1.2:", pila_temas.pila[0].pila[1])
print("Pila Pregunta 2.1:", pila_temas.pila[1].pila[0])
print("Pila Pregunta 2.2:", pila_temas.pila[1].pila[1])

def promedio(pila):
    acum = 0
    print(pila.top)
    for i in range(pila.size):
        acum +=accederPosicion(pila,i)
    print(acum)
    
    return (acum/(pila.top+1))
        
        
        
print(promedio(pila_temas.pila[0].pila[0]))


QUICKSORT(pila_encuestados, 0, pila_encuestados.top)
print(pila_encuestados)
