
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()
segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]
encuestados = segments[0]
encuestados = [line.strip() for line in encuestados.split('\n') if line.strip()]
print(encuestados)


cantidad_temas = len(segments) - 1


for i in range(1, cantidad_temas + 1): 
    temas = segments[i]
    temas = [line.strip() for line in temas.split('\n') if line.strip()]
    for tema in temas:
         numeros = [int(num) for num in tema.strip("{}").split(", ")]
         print(numeros)
    
    
