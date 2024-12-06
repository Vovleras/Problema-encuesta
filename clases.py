# clases.py

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

    def __repr__(self):
        return f"({self.nombre}, {self.encuestados})"

    def promedio_opinion(self):
        return sum([enc.opinion for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0

    def promedio_experticia(self):
        return sum([enc.experticia for enc in self.encuestados]) / len(self.encuestados) if self.encuestados else 0


class Tema:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas

    def promedio_opinion(self):
        return sum([pregunta.promedio_opinion() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0

    def promedio_experticia(self):
        return sum([pregunta.promedio_experticia() for pregunta in self.preguntas]) / len(self.preguntas) if self.preguntas else 0


class Pila:
    def __init__(self):
        self.items = []

    def pila_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.pila_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila esta vacia")

    def tope(self):
        if not self.pila_vacia():
            return self.items[-1]
        else:
            raise InterruptedError("La pila esta vacia")
