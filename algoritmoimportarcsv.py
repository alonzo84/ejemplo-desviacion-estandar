import csv

# Ruta del archivo .csv
ruta_csv = 'datos.csv'

# Leer el CSV y guardarlo como una lista de listas
datos = []
with open(ruta_csv, newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        datos.append(fila)

# Mostrar los primeros 5 registros
for fila in datos[:5]:
    print(fila)
