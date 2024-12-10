
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()
segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]
encuestados = segments[0]
encuestados = [line.strip() for line in encuestados.split('\n') if line.strip()]
print(encuestados)


cantidad_temas = len(segments) - 1


#for i in range(1, cantidad_temas + 1): 
temas = segments[1]
temas = [line.strip() for line in temas.split('\n') if line.strip()]
pregunta_por_tema=[]
numeros = [int(num) for num in temas[1].strip("{}").split(", ")]
pregunta_por_tema.append(numeros)
print(pregunta_por_tema) 
    
    
