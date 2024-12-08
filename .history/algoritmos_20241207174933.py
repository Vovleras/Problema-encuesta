""" import copy

class Pila:
    def __init__(self, size):
        self.pila= [None]*size
        self.top = -1
        self.size = size
        
    def stackEmpty(self):
        return self.top<0
          
        
    def push(self,x):
        if self.top == self.size-1:
            raise Exception("Overflow")
        else:
            
            self.top += 1
            self.pila[self.top] = x 
            

    def pop(self):
        if self.stackEmpty():
            raise Exception("Underflow")
        else:
            self.top -=1
            return self.pila[self.top+1]
    def peek(self):
        if self.stackEmpty():
            raise Exception("Underflow")
        return self.pila[self.top]

    def __repr__(self):
        return f"Pila({self.pila})"


def accederPosicion(p, i):
    
    elementos = Pila(p.size)

    while p.top >i:
        elementos.push(p.pop())

    valor = p.peek()
    while not elementos.stackEmpty():
        p.push(elementos.pop())
    
    return valor
       
    
        

    
def cambiar(i, j, A):
    p = Pila(A.size)
    
    valor_i = accederPosicion(A,i)
    valor_j = accederPosicion(A,j)
    while A.top > i - 1:
        p.push(A.pop())
        
    A.push(valor_j)
    p.pop()
    while A.top < j-1:
        A.push(p.pop())
    A.push(valor_i)
    p.pop()
    while not p.stackEmpty():
        A.push(p.pop())
    return A

        
p = Pila(5)
p.push(10)
p.push(20)
p.push(30)
p.push(40)

print("Elemento en la posicion 2:", accederPosicion(p, 2))
print("Pila despues de acceder:", p)
print("Pila despues de cambias: 2", cambiar(0,3,p))

def PARTITION(A,p,r):
    x = accederPosicion(A,p)
    i = p-1
    j = r+1
    while True:
        while accederPosicion(A,j) <= x:
            j -= 1
        while accederPosicion(A,i) >= x:
            i += 1
        if i< j:
            cambiar(i,j,A)
        else:
            return j
        
        


def QUICKSORT(A, p , r):
    if p < r:
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q)
        QUICKSORT(A,q+1,r)
        
        
        
A = Pila(9)
A.push(1)
A.push(10)
A.push(9)
A.push(3)
A.push(2)
A.push(8)
A.push(3)
A.push(9)
        
PARTITION(A,0,A.top) """

import copy

class Pila:
    def __init__(self, size):
        self.pila = [None] * size
        self.top = -1
        self.size = size
        
    def stackEmpty(self):
        return self.top < 0
          
    def push(self, x):
        if self.top == self.size - 1:
            raise Exception("Overflow")
        else:
            self.top += 1
            self.pila[self.top] = x 

    def pop(self):
        if self.stackEmpty():
            raise Exception("Underflow")
        else:
            valor = self.pila[self.top]
            self.top -= 1
            return valor

    def peek(self):
        if self.stackEmpty():
            raise Exception("Underflow")
        return self.pila[self.top]

    def __repr__(self):
        return f"Pila({self.pila[:self.top+1]})"

def accederPosicion(p, i):
    # Crear una pila temporal para no modificar la original
    pila_temp = Pila(p.size)
    
    # Desapilar hasta llegar al elemento deseado
    while p.top > i:
        pila_temp.push(p.pop())
    
    # Obtener el valor en la posición i
    valor = p.peek()
    
    # Restaurar la pila original
    while not pila_temp.stackEmpty():
        p.push(pila_temp.pop())
    
    return valor

def cambiar(i, j, A):
    # Crear pilas temporales para no modificar directamente A
    pila_temp1 = Pila(A.size)
    pila_temp2 = Pila(A.size)
    
    # Desapilar hasta la posición i
    while A.top > i:
        pila_temp1.push(A.pop())
    
    # Guardar el elemento en la posición i
    valor_i = A.peek()
    
    # Remover el elemento en la posición i
    A.pop()
    
    # Apilar el nuevo valor en la posición j
    A.push(accederPosicion(pila_temp1, j-i-1))
    
    # Restaurar elementos de pila_temp1
    while not pila_temp1.stackEmpty():
        pila_temp2.push(pila_temp1.pop())
    
    # Restaurar elementos de pila_temp2 a A
    while not pila_temp2.stackEmpty():
        A.push(pila_temp2.pop())
    
    return A

def PARTITION(A, p, r):
    # Obtener el pivote
    x = accederPosicion(A, p)
    i = p - 1
    j = r + 1
    
    while True:
        # Decrementar j mientras los elementos sean mayores que el pivote
        j -= 1
        while j > p and accederPosicion(A, j) > x:
            j -= 1
        
        # Incrementar i mientras los elementos sean menores que el pivote
        i += 1
        while i < r and accederPosicion(A, i) < x:
            i += 1
        
        # Si los índices se cruzan, terminar
        if i < j:
            cambiar(i, j, A)
        else:
            return j

def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q)
        QUICKSORT(A, q + 1, r)

# Ejemplo de uso
A = Pila(9)
A.push(1)
A.push(10)
A.push(9)
A.push(3)
A.push(2)
A.push(8)
A.push(3)
A.push(9)
A.push(4)

print("Pila original:", A)
QUICKSORT(A, 0, A.top)
print("Pila ordenada:", A)



    