from algoritmos import *

def orderListByQuick(l):
    p = Pila(len(l))
    for indice in l:
        p.push(l[indice])
    
    QUICKSORT(p,0,len(l)-1)
    return p
        
    