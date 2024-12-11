from clases import Encuestado

class Lista:

    def __init__(self):
        self.lista = [] 
    
    def agregar(self, item):
        self.lista.append(item)

    def retornar(self):
        return self.lista 
    
    def obtener(self, indice):
        if indice < 0 or indice >= len(self.lista):
            raise IndexError("Índice fuera de rango")
        return self.lista[indice]
    
    def is_empty(self):
        return self.size == 0
    
    def mostrar(self):
        # Mostrar los elementos de la cola en orden FIFO
        elementos = []
        i = self.head
        count = 0
        while count < self.size:
            elementos.append(self.queue[i])
            i = (i + 1) % self.max_length
            count += 1
        #for e in elementos:
            #print(e)
        return elementos

    def ordenar_insertion_sort(self):
        for j in range(1, len(self.lista)):
            key = self.lista[j]
            i = j - 1
            while i >= 0 and self.lista[i] > key:
                self.lista[i + 1] = self.lista[i]
                i -= 1
            self.lista[i + 1] = key

# Datos de ejemplo
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

# Crear la cola y cargar los encuestados
mi_lista = Lista()
for e in encuestados:
    mi_lista.agregar(e)

# Mostrar antes de ordenar
print(f"Lista antes de ordenar: {mi_lista.retornar()}" )

# Ordenar
mi_lista.ordenar_insertion_sort()

# Mostrar después de ordenar
print(f"Lista despues de ordenar: {mi_lista.retornar()}")

#print("Prueba elemento 0:",mi_lista.obtener(0))
