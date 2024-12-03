from clases import Encuestado, Pila

def particionar(arr, bajo, alto):
    i = bajo - 1
    pivote = arr[alto]
    
    for j in range(bajo, alto):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[alto] = arr[alto], arr[i+1]
    return i + 1

def quicksort(arr):
    pila = Pila()
    
    # Empujar los valores iniciales de bajo y alto a la pila
    pila.apilar(0)
    pila.apilar(len(arr) - 1)
    
    # Mientras la pila no esté vacía
    while not pila.pila_vacia():
        # Sacar los valores de alto y bajo de la pila
        alto = pila.desapilar()
        bajo = pila.desapilar()
        
        # Obtener el índice de partición
        p = particionar(arr, bajo, alto)
        
        # Si hay elementos a la izquierda del pivote, se empujan a la pila
        if p - 1 > bajo:
            pila.apilar(bajo)
            pila.apilar(p - 1)
        
        # Si hay elementos a la derecha del pivote, se empujan a la pila
        if p + 1 < alto:
            pila.apilar(p + 1)
            pila.apilar(alto)

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
