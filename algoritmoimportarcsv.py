import csv

# Leer archivo CSV de una sola columna
with open('archivo.csv', newline='', encoding='utf-8') as archivo:
    datos = [fila[0] for fila in csv.reader(archivo)]

# Imprimir los primeros 5 elementos
print(datos[:5])

