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
    
    def __str__(self):
        if self.stackEmpty():
            return "Pila vacía"
        else:
            # Construir una lista de elementos no nulos desde el inicio hasta el tope
            elementos = [self.pila[i] for i in range(self.top + 1)]
            # Unir los elementos con un salto de línea
            return "\n".join(str(e) for e in elementos)
        
    def __repr__(self):
        return f"Pila({self.pila[:self.top + 1]})"


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





def PARTITION(A,p,r):
    x = accederPosicion(A,p)
    
    i = p-1
    j = r+1

    
    while True:
        j -=1
        while j >= p and accederPosicion(A, j) > x:
            j -= 1
            
    
        i+=1  
        while i <= r and accederPosicion(A,i) < x:
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