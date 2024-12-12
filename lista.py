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
    
    def tamaño(self):
        return len(self.lista)
    
    def es_vacia(self):
        return len(self.lista) == 0
    
    def asignar(self, pos, valor):
        if 0 <= pos < self.tamaño():
            self.lista[pos] = valor
        else:
            raise IndexError("Índice fuera de rango")


    def ordenar_insertion_sort(self):
        n = self.tamaño() 
        for j in range(1, n):
            key = self.obtener(j)
            i = j - 1
            while i >= 0 and self.obtener(i) > key:
                self.asignar(i + 1, self.obtener(i)) 
                i -= 1
            self.asignar(i + 1, key)

