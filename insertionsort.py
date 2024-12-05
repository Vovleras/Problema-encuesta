from clases import Encuestado

class ColaInsertionSort:
    def __init__(self, max_length):
        self.max_length = max_length
        self.queue = [None] * max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_length:
            raise Exception("Overflow: La cola está llena")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_length
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Underflow: La cola está vacía")
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.max_length
        self.size -= 1
        return item

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
        for e in elementos:
            print(e)

    def ordenar_insertion_sort(self):
        # Convertir la cola a una lista para aplicar Insertion Sort
        elementos = []
        while not self.is_empty():
            elementos.append(self.dequeue())

        # Aplicar Insertion Sort en la lista
        for j in range(1, len(elementos)):
            key = elementos[j]
            i = j - 1
            while i >= 0 and elementos[i] > key:
                elementos[i + 1] = elementos[i]
                i -= 1
            elementos[i + 1] = key

        # Cargar los elementos ordenados nuevamente en la cola
        for item in elementos:
            self.enqueue(item)

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
cola_encuestados = ColaInsertionSort(max_length=len(encuestados) + 1)
for e in encuestados:
    cola_encuestados.enqueue(e)

# Mostrar antes de ordenar
print("Cola antes de ordenar:")
cola_encuestados.mostrar()

# Ordenar
cola_encuestados.ordenar_insertion_sort()

# Mostrar después de ordenar
print("\nCola después de ordenar:")
cola_encuestados.mostrar()
