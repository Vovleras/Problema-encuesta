from clases import Encuestado, Pila

def particionar(array, p, r):
    i= p - 1
    pivote = array[r]
    
    for j in range(p, r):
        if array[j] < pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1

def quicksort(array):
    pila = Pila()
    
    # Empujar los valores iniciales de p y r a la pila
    pila.apilar(0)
    pila.apilar(len(array) - 1)
    
    # Mientras la pila no esté vacía
    while not pila.pila_vacia():
        # Sacar los valores de r y p de la pila
        r = pila.desapilar()
        p = pila.desapilar()
        
        # Obtener el índice de partición
        piv = particionar(array, p, r)
        
        # Si hay elementos a la izquierda del pivote, se empujan a la pila
        if piv - 1 > p:
            pila.apilar(p)
            pila.apilar(piv - 1)
        
        # Si hay elementos a la derecha del pivote, se empujan a la pila
        if piv + 1 < r:
            pila.apilar(piv + 1)
            pila.apilar(r)

# Ejemplo de uso:
encuestados = [
    Encuestado(1, "Sofia García", 1, 6), 
    Encuestado(2, "Alejandro Torres", 7, 10), 
    Encuestado(3, "Valentina Rodriguez", 9, 0), 
    Encuestado(4, "Juan Lopéz", 10, 1), 
    Encuestado(5, "Martina Martinez", 7, 0), 
    Encuestado(6, "Sebastian Perez", 8, 9), 
    Encuestado(7, "Camila Fernandez", 2, 7), 
    Encuestado(8, "Mateo Gonzalez", 4, 7), 
    Encuestado(9, "Isabella Díaz", 7, 5), 
    Encuestado(10, "Daniel Ruiz", 2, 9), 
    Encuestado(11, "Luciana Sanchez", 1, 7), 
    Encuestado(12, "Lucas Vasquez", 6, 8),
]

quicksort(encuestados)
print("Datos ordenados:", encuestados)
