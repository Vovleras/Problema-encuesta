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
    elementos = []

    while p.top >i:
        elementos.append(p.pop())

    else:
        p1.pop()
        return accederPosicion(p1,i)
       
    
        
p = Pila(4)
p.push(2)
p.push(3)
p.push(4)
k = accederPosicion(p,2)

print(k)

def cambiar(i, j, A):
    p = copy.deepcopy(A)
    pi = accederPosicion(A,i)
    pj = accederPosicion(A,j)
    while A.top > i - 1:
        A.pop()
    A.push(pj)
    while A.top < j-1:
        i += 1
        A.push(accederPosicion(p,i))
    A.push(pi)
    while p.top > A.top:
        j+=1
        A.push(accederPosicion(p,j))
    return A


    
print(cambiar(0,1,p)) 
print(accederPosicion(p,0))
        
        

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
        
        
        
        
        
    
    