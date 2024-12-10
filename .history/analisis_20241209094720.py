from algoritmos import *

def orderListByQuick(l):
    p = Pila(len(l))
    resultado = list()
    for indice in l:
        p.push(l[indice])
    
    QUICKSORT(p,0,len(l)-1)
    
    for objeto in p:
        resultado.append(objeto)
        
        
    return p
        
    