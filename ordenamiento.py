from clases import Encuestado, Pila

def quicksort(pila, p, r):
    if p < r:
        piv = particionar(pila, p, r)
        quicksort(pila, p, piv - 1)
        quicksort(pila, piv + 1, r)

#Usa los métodos acceder_posicion e intercambiar_elementos para particionar la pila de manera correcta.
def particionar(pila, p, r):
    pivote = acceder_posicion(pila, r)
    i = p - 1

    for j in range(p, r):
        if acceder_posicion(pila, j) < pivote:
            i += 1
            intercambiar_elementos(pila, i, j)
    
    intercambiar_elementos(pila, i + 1, r)
    return i + 1

#devuelve el elemento en la posición index sin modificar la pila.
def acceder_posicion(pila, index):
    return pila.items[index]

#Intercambia los elementos en las posiciones i y j directamente en la pila items de la pila.
def intercambiar_elementos(pila, i, j):
    pila.items[i], pila.items[j] = pila.items[j], pila.items[i]

# Ejemplo de uso:
encuestados = Pila()
encuestados.apilar(Encuestado(1, "Sofia García", 1, 6))
encuestados.apilar(Encuestado(2, "Alejandro Torres", 7, 10))
encuestados.apilar(Encuestado(3, "Valentina Rodriguez", 9, 0))
encuestados.apilar(Encuestado(4, "Juan Lopéz", 10, 1))
encuestados.apilar(Encuestado(5, "Martina Martinez", 7, 0))
encuestados.apilar(Encuestado(6, "Sebastian Perez", 8, 9))
encuestados.apilar(Encuestado(7, "Camila Fernandez", 2, 7))
encuestados.apilar(Encuestado(8, "Mateo Gonzalez", 4, 7))
encuestados.apilar(Encuestado(9, "Isabella Díaz", 7, 5))
encuestados.apilar(Encuestado(10, "Daniel Ruiz", 2, 9))
encuestados.apilar(Encuestado(11, "Luciana Sanchez", 1, 7))
encuestados.apilar(Encuestado(12, "Lucas Vasquez", 6, 8))
encuestados.apilar(Encuestado(13,"Deiby Muñoz", 3, 7))

quicksort(encuestados, 0, encuestados.size_pila() - 1)

# Desapilar y mostrar los resultados ordenados
resultados_ordenados = []
while not encuestados.pila_vacia():
    resultados_ordenados.append(encuestados.desapilar())
print("Datos ordenados:", resultados_ordenados[::-1])
