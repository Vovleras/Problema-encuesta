
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Dividir el texto en segmentos separados por líneas en blanco
segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]

# Imprimir los segmentos separados
for i, segment in enumerate(segments, 1):
    print(f"Segmento {i}:\n{segment}\n")
