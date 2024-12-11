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

    def ordenar_insertion_sort(self):
        for j in range(1, len(self.lista)):
            key = self.lista[j]
            i = j - 1
            while i >= 0 and self.lista[i] > key:
                self.lista[i + 1] = self.lista[i]
                i -= 1
            self.lista[i + 1] = key
