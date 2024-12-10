from algoritmos import *
from clases import *

def orderListByQuick(l):
    p = Pila(len(l))
    resultado = list()
    for indice in l:
        p.push(indice)
    
    QUICKSORT(p,0,len(l)-1)
      
    return p

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

if(isinstance(orderListByQuick(encuestados),list)):
    print("Hola")

