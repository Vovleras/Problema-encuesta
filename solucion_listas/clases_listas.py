# clases.py
from solucion_listas.lista import Lista

class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion
        self.criterio = 1

    def __repr__(self):
        return f"({self.id}, Nombre: {self.nombre}, Experticia: {self.experticia}, Opinion: {self.opinion})"

    def __lt__(self, other):
        if self.opinion != other.opinion:
            return self.opinion > other.opinion
        if self.experticia != other.experticia:
            return self.experticia > other.experticia
        return self.id > other.id
    
    @classmethod
    def set_lt_method(cls, compare_fn):
        cls.__lt__ = compare_fn

class Pregunta:
    def __init__(self, nombre, encuestados):
        self.nombre = nombre
        self.encuestados = encuestados

    def __repr__(self):
        return f"({self.nombre}, {self.encuestados})"

    def promedio_opinion(self):
        
        promedio = 0
        suma = 0
        for enc in range(self.encuestados.tamaño()):
            encuestado = self.encuestados.obtener(enc)
            suma += encuestado.opinion
        
        if self.encuestados.es_vacia():
            return 0
        else:
            promedio = suma / self.encuestados.tamaño()
            return promedio

        #return sum([enc.opinion for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0

    def promedio_experticia(self):

        promedio = 0
        suma = 0
        for enc in range(self.encuestados.tamaño()):
            encuestado = self.encuestados.obtener(enc)
            suma += encuestado.experticia
        
        if self.encuestados.es_vacia():
            return 0
        else:
            promedio = suma / self.encuestados.tamaño()
            return promedio

        #return sum([enc.experticia for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0
    
    def id_encuestados(self):
        ids = Lista()
        for enc in range(self.encuestados.tamaño()):
            encuestado = self.encuestados.obtener(enc)
            ids.agregar(encuestado.id)
        
        return ids

    def __lt__(self, other):
        if self.promedio_opinion() != other.promedio_opinion():
            return self.promedio_opinion() > other.promedio_opinion()
        if self.promedio_experticia() != other.promedio_experticia():
            return self.promedio_experticia() > other.promedio_experticia()
        return self.encuestados.tamaño() > other.encuestados.tamaño()

    @classmethod
    def set_lt_method(cls, compare_fn):
        cls.__lt__ = compare_fn

class Tema:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas

    def __repr__(self):
        return f"({self.nombre}, {self.preguntas})"

    def promedio_opinion(self):
        promedio = 0
        suma = 0
        for preg in range(self.preguntas.tamaño()):
            pregunta = self.preguntas.obtener(preg)
            suma += pregunta.promedio_opinion()
        
        if self.preguntas.es_vacia():
            return 0
        else:
            promedio = suma / self.preguntas.tamaño()
            return promedio
        #return sum([pregunta.promedio_opinion() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0

    def promedio_experticia(self):
        promedio = 0
        suma = 0
        for preg in range(self.preguntas.tamaño()):
            pregunta = self.preguntas.obtener(preg)
            suma += pregunta.promedio_experticia()
        
        if self.preguntas.es_vacia():
            return 0
        else:
            promedio = suma / self.preguntas.tamaño()
            return promedio
        #return sum([pregunta.promedio_experticia() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0

    def __lt__(self, other):
        if self.promedio_opinion() != other.promedio_opinion():
            return self.promedio_opinion() > other.promedio_opinion()
        if self.promedio_experticia() != other.promedio_experticia():
            return self.promedio_experticia() > other.promedio_experticia()
        return sum(len([pregunta.encuestados for pregunta in self.preguntas])) > sum(len([pregunta.encuestados for pregunta in other.preguntas])) #Corregir

