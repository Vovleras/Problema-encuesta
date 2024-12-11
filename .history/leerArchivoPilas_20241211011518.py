from clases import *
from algoritmos import *

#Funcion que recbie el nombre de un archivo de texto y extrae la información del archivo en listas
#Retorna una lista que en su primera posicion tiene una lista de objetos de encuestados
#y en la segunda posicion tiene una lista de temas que a su vez tiene una lista de preguntas. 
# Cada pregunta contiene el indice de los encuestados que la respondieron.
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
        lista_tema.append(pregunta_por_tema)
    
    
    return [encuestados,lista_tema]


#funcion que recibe una lista de encuestados y una lista de temas
# retorna una pila de temas que contiene una pila de objetos preguntas por cada tema

def obtener_objetos_por_preguntas(encuestados, temas):
    pila_temas = Pila(len(temas))
    
    for i, tema in enumerate(temas, start=1):  
        pila_tema_pregunta = Pila(len(tema))
        
        for idx, pregunta in enumerate(tema, start=1):  
            pila_encuestado_preg = Pila(len(pregunta))
            
            for encuestado in pregunta:  
                pila_encuestado_preg.push(encuestados[encuestado - 1])
        
            pila_tema_pregunta.push(
                Pregunta(f"Pregunta {i}.{idx}", pila_encuestado_preg)
            )
        
        pila_temas.push(pila_tema_pregunta)
    
    return pila_temas

        
    
#funcion que obtiene los datos: encuestados, temas y preguntas en pilas  
#retorna una pila de encuestados y una pila de temas que contiene una pila de objetos pregunta por cada tema

def obtener_pilas(nombre):
    pila = Pila(2)
    lista_datos=obtener_data(nombre)
    encuestados = lista_datos[0]
    temas_obj = obtener_objetos_por_preguntas(encuestados,lista_datos[1])
    encuestados_pila = Pila(len(encuestados))
    for encuestado in encuestados:
        encuestados_pila.push(encuestado)
    
    pila.push(encuestados_pila)
    pila.push(temas_obj)
    return pila
    
        

#Funcion que recibe una pila de preguntas y un string tipo
# Calcula el promedio segun el tipo (experticia u opinion) de cada pregunta de la pila
def promedio(preguntas,tipo):
    acum = 0
    for pregunta in range(preguntas.top+1) :
        for id in range ((accederPosicion(preguntas,pregunta).encuestados.top)+1):
            if tipo == 'opinion':
                acum += accederPosicion(accederPosicion(preguntas,pregunta).encuestados,id).opinion
            else:
                acum += accederPosicion(accederPosicion(preguntas,pregunta).encuestados,id).experticia 
        if tipo == 'opinion':  
            accederPosicion(preguntas,pregunta).promedio_opinion = acum/((accederPosicion(preguntas,pregunta).encuestados.top)+1)
        else:
            accederPosicion(preguntas,pregunta).promedio_experticia = acum/((accederPosicion(preguntas,pregunta).encuestados.top)+1)
            
        acum=0
        print("prom opinion")
        print(accederPosicion(preguntas,pregunta).promedio_opinion)
        print("prom experticia")
        print(accederPosicion(preguntas,pregunta).promedio_experticia)
        
           
#Funcion que calcula el promedio segun el tipo (experticia u opinion) de  una pila de temas
def calcular_promedio(temas, tipo): 
    print("llamndo a promedio")
    for i in range(temas.top+1):
        promedio((accederPosicion(temas,i)), tipo)


#funcion que recibe una pila de tema y organiza las preguntas de cada tema
def ordenar_preguntas_prom(temas):
    
    print("esto es ordenar preguntas:")
    for i in range(temas.top+1):
        QUICKSORT(accederPosicion(temas,i),0,accederPosicion(temas,i).top)
        print(accederPosicion(temas,i))

#funcion que recibe una pila de tema y organiza los encuestados de las preguntas de cada tema
def ordenar_encuestados_preg(tema):
    print("ESTO ES ORDENAR ENCUESTADOS")
    for i in range(tema.top+1):
        for j in range ( (accederPosicion(tema,i).top)+1):
            QUICKSORT(accederPosicion(accederPosicion(tema,i),j).encuestados, 0, accederPosicion(accederPosicion(tema,i),j).encuestados.top)
            print(accederPosicion(accederPosicion(tema,i),j).encuestados)
        
     

def obtener_resultado(nombre):
    resultado=obtener_pilas(nombre) 
    pila_encuestados = accederPosicion(resultado,0)
    pila_temas = accederPosicion(resultado,1)
    
    calcular_promedio(pila_temas, 'opinion')
    calcular_promedio(pila_temas, 'experticia')
    
    ordenar_encuestados_preg(pila_temas)
    ordenar_preguntas_prom(pila_temas)
    
    QUICKSORT(pila_encuestados, 0, pila_encuestados.top)
    print(pila_encuestados)

 
resultado=obtener_pilas('datos.txt')
pila_encuestados = accederPosicion(resultado,0)
pila_temas = accederPosicion(resultado,1)

        
    

#obtener_resultado('datos.txt')




