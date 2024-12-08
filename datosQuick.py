from clases import *
from algoritmos import *

# Abre el archivo 'datos.txt' en modo de lectura
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()

lines = data.split('\n')

# Inicializa una lista para almacenar los pares de valores de Experticia y Opinión
A = Pila(12)

contador_id = 1

# Recorre cada línea del archivo
for line in lines:
    # Verifica si la línea contiene información de encuestado
    if 'Experticia' in line and 'Opinión' in line:
        parts = line.split(',')
        nombre = parts[0].strip()
        experticia = int(parts[1].split(':')[1].strip())
        opinion = int(parts[2].split(':')[1].strip())

        encuestado = Encuestado(contador_id, nombre, experticia, opinion)

        contador_id += 1

        A.push(encuestado)
        
print(A)

QUICKSORT(A, 0, A.top)

print(A)
