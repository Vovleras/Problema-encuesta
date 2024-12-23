from solucion_pilas.clases import *
from solucion_pilas.algoritmos import *
import time
import os

#Funcion que recbie el nombre de un archivo de texto y extrae la información del archivo en listas
#Retorna una lista que en su primera posicion tiene una lista de objetos de encuestados
#y en la segunda posicion tiene una lista de temas que a su vez tiene una lista de preguntas. 
# Cada pregunta contiene el indice de los encuestados que la respondieron.
def obtener_data(nombre):
     
    with open(nombre, 'r', encoding='utf-8') as file:
        data = file.read()

    segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]
 
    encuestados_str = segments[0]
    encuestados = []
    for line in encuestados_str.split('\n'):
        if line.strip():
            
            parts = line.strip().split(", ")
            nombre = parts[0]
            experticia = int(parts[1].split(": ")[1])
            opinion = int(parts[2].split(": ")[1].strip(','))
            encuestado = Encuestado(len(encuestados) + 1, nombre, experticia, opinion)
            encuestados.append(encuestado)


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
# retorna una pila de objetos temas que contiene una pila de objetos preguntas por cada tema

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
        tema = Tema(f"Tema {i}",pila_tema_pregunta)
        pila_temas.push(tema)
    
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
            accederPosicion(preguntas,pregunta).promedio_opinion = round( acum/((accederPosicion(preguntas,pregunta).encuestados.top)+1) ,2)
        else:
            accederPosicion(preguntas,pregunta).promedio_experticia = round( acum/((accederPosicion(preguntas,pregunta).encuestados.top)+1) ,2)
            
        acum=0
    
        
           
#Funcion que calcula el promedio de cada pregunta de una pila de objetos tema segun el tipo (experticia u opinion)
def calcular_promedio(temas, tipo): 
   
    for i in range(temas.top+1):
       
        promedio((accederPosicion(temas,i)).preguntas, tipo)

#Funcion que calcula el promedio de cada tema segun el tipo (experticia u opinion) 
def calcular_prom_temas(temas,tipo):
    acum =0
    for i in range(temas.top+1):
        for j in range(accederPosicion(temas,i).preguntas.top+1):
            if tipo == 'opinion':
                acum += accederPosicion(accederPosicion(temas,i).preguntas,j).promedio_opinion
            else:
                acum += accederPosicion(accederPosicion(temas,i).preguntas,j).promedio_experticia
        if tipo == 'opinion':
            accederPosicion(temas,i).promedio_opinion= round( (acum/((accederPosicion(temas,i).preguntas.top)+1)) ,2)
        else:
            accederPosicion(temas,i).promedio_experticia= round( (acum/((accederPosicion(temas,i).preguntas.top)+1)) ,2)
        acum = 0




#funcion que recibe una pila de tema y organiza las preguntas de cada tema
def ordenar_preguntas_prom(temas):
    
    
    for i in range(temas.top+1):
        QUICKSORT(accederPosicion(temas,i).preguntas,0,accederPosicion(temas,i).preguntas.top)
        

#funcion que recibe una pila de tema y organiza los encuestados de las preguntas de cada tema
def ordenar_encuestados_preg(tema):
    Encuestado.criterio = "opinion"
   
    for i in range(tema.top+1):
        for j in range ( (accederPosicion(tema,i).preguntas.top)+1):
            
            QUICKSORT(accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados, 0, accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados.top)
           

        
        
#funcion que recibe una pila de tema y retorna la pregunta con maximo y minimo promedio de opinion y experticia
def mayor_menor_pregunta(tema,tipo):
    

    max =  accederPosicion(accederPosicion(tema,0).preguntas,0)
    min =  accederPosicion(accederPosicion(tema,0).preguntas,0)

    p = Pila(2)
    
    for i in range(tema.top+1):
        for j in range ( (accederPosicion(tema,i).preguntas.top)+1):
            if 'opinion' == tipo:
                if max.promedio_opinion < accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_opinion:
                    max = accederPosicion(accederPosicion(tema,i).preguntas,j)
                if accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_opinion < min.promedio_opinion:
                    min = accederPosicion(accederPosicion(tema,i).preguntas,j)
                    
                if accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_opinion == min.promedio_opinion:
                    if  accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados.size > min.encuestados.size:
                        min = accederPosicion(accederPosicion(tema,i).preguntas,j)
                
                if accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_opinion == max.promedio_opinion:
                    if  accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados.size > max.encuestados.size:
                        max = accederPosicion(accederPosicion(tema,i).preguntas,j)
                        
                        
                
            else:
                if max.promedio_experticia < accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_experticia:
                    max = accederPosicion(accederPosicion(tema,i).preguntas,j)
                    
                if accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_experticia < min.promedio_experticia:
                    min = accederPosicion(accederPosicion(tema,i).preguntas,j)
                    
                if accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_experticia == min.promedio_experticia:
                    if  accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados.size > min.encuestados.size:
                        min = accederPosicion(accederPosicion(tema,i).preguntas,j)
                
                if max.promedio_experticia < accederPosicion(accederPosicion(tema,i).preguntas,j).promedio_experticia:
                    if  accederPosicion(accederPosicion(tema,i).preguntas,j).encuestados.size > max.encuestados.size:
                        max = accederPosicion(accederPosicion(tema,i).preguntas,j)
                    
                
                
                
    p.push(max)
    p.push(min)
    return p

#funcin que recibe una pila de temas y retorna el encuesta maximo y minimo segun el tipo
def mayor_menor_encuestados(encuestados,tipo):
    min = accederPosicion(encuestados,0)
    max = accederPosicion(encuestados,0)
    p = Pila(2)
    for i in range(encuestados.top+1):
        if tipo == 'opinion':
            if accederPosicion(encuestados,i).opinion < min.opinion:
                min = accederPosicion(encuestados,i)
            if accederPosicion(encuestados,i).opinion > max.opinion:
                max = accederPosicion(encuestados,i)
            if (accederPosicion(encuestados,i).opinion == min.opinion):
                if accederPosicion(encuestados,i).id >  min.id  :
                    min = accederPosicion(encuestados,i)
            if (accederPosicion(encuestados,i).opinion == max.opinion):
                if accederPosicion(encuestados,i).id > max.id :
                    max = accederPosicion(encuestados,i)
                    
                
        else:
            if accederPosicion(encuestados,i).experticia < min.experticia:
                min = accederPosicion(encuestados,i)
            if accederPosicion(encuestados,i).experticia > max.experticia:
                max = accederPosicion(encuestados,i)
            if (accederPosicion(encuestados,i).experticia == min.experticia):
                if accederPosicion(encuestados,i).id > min.id  :
                    min = accederPosicion(encuestados,i)
            if (accederPosicion(encuestados,i).experticia == max.experticia):
                if accederPosicion(encuestados,i).id > max.id :
                    max = accederPosicion(encuestados,i)
            
    p.push(max)
    p.push(min)
    return p
    

#Funcion que recibe una pila de encuestados y retorna el promedio segun el tipo
def promedio_encuestados(encuestados,tipo):
    prom = 0
    acum = 0
    for i in range(encuestados.top+1):
        if tipo == 'opinion':
            acum+=accederPosicion(encuestados,i).opinion
        else:
            acum+=accederPosicion(encuestados,i).experticia
        prom = round((acum/encuestados.size),2)
    return prom

        
            
        
#Funcion que recibe una pila de tema, pila de encuestados, el mayor y menor encuestado segun opinion y experticia, promeido de experticia de los encuestados y promedio de  opinion de los encuestados
# Retorna un archivo txt con toda la informacion de los parametros de entrada
def mostra_info(pila_encuestados, pila_temas, m_n_e_e, m_n_e_o, m_n_o, m_n_e, prom_experticia_encuestados, prom_opinion_encuestados):
    
    
    archivo_nombre = f"resultados.txt"

    
    with open(archivo_nombre, "w", encoding="utf-8") as archivo:
       
        def escribir_en_archivo(*args, **kwargs):
            print(*args, **kwargs, file=archivo)
    
        escribir_en_archivo("Resultados de la encuesta:")
        escribir_en_archivo("")
        for i in range(pila_temas.top + 1):
            
            tema = accederPosicion(pila_temas, i)
            escribir_en_archivo(f"[{tema.promedio_opinion}] {tema.nombre}:")
            
            for j in range(tema.preguntas.top + 1):
                
                pregunta = accederPosicion(tema.preguntas, j)
                encuestados_ids = Pila(pregunta.encuestados.size)
                
                for k in range(pregunta.encuestados.top + 1):
                    encuestado_id = accederPosicion(pregunta.encuestados, k).id
                    encuestados_ids.push(str(encuestado_id))
                
                p = ""
                
                for k in range(encuestados_ids.top + 1):
                    if p:
                        p += ", " 
                    p += accederPosicion(encuestados_ids, k)
                
                escribir_en_archivo(f" [{pregunta.promedio_opinion}] {pregunta.nombre} ({p})") 
            escribir_en_archivo("")
            
        escribir_en_archivo("Lista de encuestados:")
        for i in range(pila_encuestados.top+1):
            escribir_en_archivo(f" ({accederPosicion(pila_encuestados,i).id}, Nombre:'{accederPosicion(pila_encuestados,i).nombre}', Experticia:{accederPosicion(pila_encuestados,i).experticia}, Opinion:{accederPosicion(pila_encuestados,i).opinion})")
        
        escribir_en_archivo("")
        escribir_en_archivo("Resultados:")
        escribir_en_archivo(f"Pregunta con mayor promedio de opinion: [{accederPosicion(m_n_o, 0).promedio_opinion}] {accederPosicion(m_n_o, 0).nombre}")
        escribir_en_archivo(f"Pregunta con menor promedio de opinion: [{accederPosicion(m_n_o, 1).promedio_opinion}] {accederPosicion(m_n_o, 1).nombre}")
        escribir_en_archivo(f"Pregunta con mayor promedio de experticia: [{accederPosicion(m_n_e, 0).promedio_experticia}] {accederPosicion(m_n_e, 0).nombre}")
        escribir_en_archivo(f"Pregunta con menor promedio de experticia: [{accederPosicion(m_n_e, 1).promedio_experticia}] {accederPosicion(m_n_e, 1).nombre}")
        escribir_en_archivo(f"Encuestado con mayor opinion: ({accederPosicion(m_n_e_o, 0).id}, Nombre: ' {accederPosicion(m_n_e_o, 0).nombre} ', Experticia: {accederPosicion(m_n_e_o, 0).experticia}, Opinion: {accederPosicion(m_n_e_o, 0).opinion})")
        escribir_en_archivo(f"Encuestado con menor opinion: ({accederPosicion(m_n_e_o, 1).id}, Nombre: '{accederPosicion(m_n_e_o, 1).nombre}', Experticia:  {accederPosicion(m_n_e_o, 1).experticia}, Opinion: {accederPosicion(m_n_e_o, 1).opinion})")
        escribir_en_archivo(f"Encuestado con mayor experticia: ({accederPosicion(m_n_e_e, 0).id}, Nombre: ' {accederPosicion(m_n_e_e, 0).nombre} ', Experticia: {accederPosicion(m_n_e_e, 0).experticia}, Opinion: {accederPosicion(m_n_e_e, 0).opinion})")
        escribir_en_archivo(f"Encuestado con menor experticia: ({accederPosicion(m_n_e_e, 1).id}, Nombre: '{accederPosicion(m_n_e_e, 1).nombre}', Experticia:  {accederPosicion(m_n_e_e, 1).experticia}, Opinion: {accederPosicion(m_n_e_e, 1).opinion})")
        escribir_en_archivo(f"Promedio de experticia de los encuestados: {prom_experticia_encuestados}")
        escribir_en_archivo(f"Promedio de opinion de los encuestados: {prom_opinion_encuestados}")
        
         
         

    
            

def obtener_resultado(nombre):
    resultado=obtener_pilas(nombre) 
    pila_encuestados = accederPosicion(resultado,0)
    pila_temas = accederPosicion(resultado,1)
   
    calcular_promedio(pila_temas, 'opinion')
    calcular_promedio(pila_temas, 'experticia')
    calcular_prom_temas(pila_temas,'opinion')
    calcular_prom_temas(pila_temas,'experticia')
    
    m_n_o=mayor_menor_pregunta(pila_temas,'opinion')
    m_n_e=mayor_menor_pregunta(pila_temas,'experticia')
    m_n_e_o=mayor_menor_encuestados(pila_encuestados,'opinion')
    m_n_e_e=mayor_menor_encuestados(pila_encuestados,'experticia')
    
    prom_opinion_encuestados = promedio_encuestados(pila_encuestados,'opinion')
    prom_experticia_encuestados = promedio_encuestados(pila_encuestados,'experticia')

    ordenar_encuestados_preg(pila_temas)
    ordenar_preguntas_prom(pila_temas)
    QUICKSORT(pila_temas,0,pila_temas.top)
    Encuestado.criterio = 'experticia'
    QUICKSORT(pila_encuestados, 0, pila_encuestados.top)
    mostra_info(pila_encuestados, pila_temas, m_n_e_e, m_n_e_o, m_n_o, m_n_e, prom_experticia_encuestados, prom_opinion_encuestados)
    


"""
Calcula el tiempo total de ejecución del programa, desde la carga del archivo
hasta la escritura de los resultados en "resultados.txt".
"""
def calcular_tiempo_ejecucion_quick(nombre_archivo):
    tiempo_inicio = time.time()
    obtener_resultado(nombre_archivo)
    tiempo_fin = time.time()
    tiempo_total_ms = (tiempo_fin - tiempo_inicio) * 1000

    print("Se escribieron los resultados")

    with open("resultados.txt", "a", encoding="utf-8") as archivo_resultados:
        archivo_resultados.write(f"\nTiempo total de ejecución del programa: {tiempo_total_ms:.2f} milisegundos\n")

    ruta_archivo_salida = os.path.join(os.getcwd(), "resultados.txt")
    print(ruta_archivo_salida)
    return ruta_archivo_salida
    

 
#obtener_resultado('entrada_prueba_1.txt')  
#obtener_resultado('entrada_prueba_2.txt')
#obtener_resultado('entrada_prueba_3.txt') 
 





