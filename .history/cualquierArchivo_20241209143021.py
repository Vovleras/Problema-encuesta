
with open('datos.txt', 'r', encoding='utf-8') as file:
    data = file.read()

segments = [segment.strip() for segment in data.split('\n\n') if segment.strip()]

print((segments[0])


