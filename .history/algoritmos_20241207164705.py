import copy

class Pila:
    def __init__(self, size):
        self.pila= []
        self.top = -1
        self.size = size
        
    def stackEmpty(self):
        return self.top<0
          
        
    def push(self,x):
        if self.top == self.size-1:
            raise Exception("Overflow")
        else: 
            self.pila.append(x)
            self.top+=1

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
       
    
        
p = Pila(5)
p.push(10)
p.push(20)
p.push(30)
p.push(40)

# Acceder a una posición específica
print("Elemento en la posicion 2:", accederPosicion(p, 2))  # Debería imprimir 30

# Verificar que la pila no ha cambiado
print("Pila despues de acceder:", p)

""" def cambiar(i, j, A):
    p = Pila(A.size)
    valor_i = accederPosicion(A,i)
    valor_j = accederPosicion(A,j)
    while A.top > i - 1:
        p.push(A.pop())
        
    A.push(valor_j)
    while A.top < j-1:
        i += 1
        A.push(accederPosicion(p,i))
    A.push(valor_i)
    while p.top > A.top:
        j+=1
        A.push(accederPosicion(p,j))
    return A """
    
def cambiar(i, j, A):
    p = Pila(A.size)
    valor_i = accederPosicion(A,i)
    valor_j = accederPosicion(A,j)
    while A.top > i - 1:
        p.push(A.pop())
        
    A.push(valor_j)
    while A.top < j-1:
        A.push(p.pop())
    print(p.top)
    A.push(valor_i)
    while p.top > A.top:
        j+=1
        A.push(accederPosicion(p,j))
    return A


    
print(cambiar(0,1,p))
        

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
            1
            #cambiar(i,j,A)
        
        

    




def QUICKSORT(A, p , r):
    if p < r:
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q)
        QUICKSORT(A,q+1,r)
        
        
        
        
        
    
    