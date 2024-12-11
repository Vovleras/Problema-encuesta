from algoritmos import *

class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

    def __repr__(self):
        return f"({self.id}, {self.nombre}, {self.experticia}, {self.opinion})"

    
    def __lt__(self, other):
        if Encuestado.criterio == "opinion":
            if self.opinion != other.opinion:
                return self.opinion > other.opinion
            if self.experticia != other.experticia:
                return self.experticia > other.experticia
            return self.id < other.id

        elif Encuestado.criterio == "experticia":
            if self.experticia != other.experticia:
                return self.experticia > other.experticia
            return self.id > other.id
        
        
  
        
    

class Pregunta:
    def __init__(self, nombre, encuestados):
        self.nombre = nombre
        self.encuestados = encuestados
        self.promedio_opinion = 0
        self.promedio_experticia = 0
    
    def __repr__(self):
        return f"({self.nombre}, {self.encuestados})"

    """ def promedio_opinion(self):
        print(f"Calculando promedio de opinión para la pregunta: {self.nombre}")
        if self.encuestados:
            print(f"Encuestados: {[enc.nombre for enc in self.encuestados]}")
        return sum([enc.opinion for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0

    def promedio_experticia(self):
        return sum([enc.experticia for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0 """
    
    def __lt__(self, other):
        if self.promedio_opinion != other.promedio_opinion:
            return self.promedio_opinion > other.promedio_opinion
        if self.promedio_experticia != other.promedio_experticia:
            return self.promedio_experticia > other.promedio_experticia
        return self.encuestados.size > other.encuestados.size


class Tema:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas
        self.promedio_opinion = 0
        self.promedio_experticia = 0

    
    def __lt__(self, other):
        if self.promedio_opinion != other.promedio_opinion:
            return self.promedio_opinion > other.promedio_opinion
        if self.promedio_experticia != other.promedio_experticia:
            return self.promedio_experticia > other.promedio_experticia
        total_encuestados_self = 0
        for i in range(self.preguntas.top+1):
           total_encuestados_self += accederPosicion(self.preguntas,i).encuestados.size
        
        total_encuestados_other = 0
        for i in range(other.preguntas.top+1):
           total_encuestados_other += accederPosicion(other.preguntas,i).encuestados.size
            
        return total_encuestados_self > total_encuestados_other
