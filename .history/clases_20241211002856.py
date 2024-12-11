class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

    def __repr__(self):
        return f"({self.id}, {self.nombre}, {self.experticia}, {self.opinion})"

    
    def __lt__(self, other):
        if self.opinion != other.opinion:
            return self.opinion > other.opinion
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

    """ def promedio_opinion(self):
        return sum([pregunta.promedio_opinion() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0

    def promedio_experticia(self):
        return sum([pregunta.promedio_experticia() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0 """
    
    def __lt__(self, other):
        if self.promedio_opinion != other.promedio_opinion:
            return self.promedio_opinion > other.promedio_opinion
        if self.promedio_experticia != other.promedio_experticia:
            return self.promedio_experticia > other.promedio_experticia
        return sum( pregunta.encuestados.size for pregunta in self.preguntas) > sum( pregunta.encuestados.size for pregunta in other.preguntas)
