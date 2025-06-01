import csv

# Paso 0: Leer archivo CSV de una sola columna
with open('datos.csv', newline='', encoding='utf-8') as archivo:
    datos = [float(fila[0]) for fila in csv.reader(archivo)]  # Convertimos cada dato a float

# Paso 1: Calcular la media (promedio)
suma_total = sum(datos)           # Sumar todos los datos
cantidad_datos = len(datos)       # Contar cuántos datos hay
media = suma_total / cantidad_datos  # Dividir para obtener la media
print(f"Media: {media}")

# Paso 2: Crear nueva lista restando la media a cada dato
diferencias = []                  # Nueva lista vacía
for dato in datos:
    diferencia = dato - media     # Restar la media a cada dato
    diferencias.append(diferencia)  # Agregar el resultado a la nueva lista

# Mostrar los primeros 5 resultados
print("Primeros 5 elementos después de restar la media:")
print(diferencias[:5])

import math  # Para la función sqrt (raíz cuadrada)

# Paso 3: Crear nueva lista con las diferencias al cuadrado
cuadrados = []
for diferencia in diferencias:
    cuadrados.append(diferencia ** 2)  # Elevar al cuadrado

# Paso 4: Sumar todos los cuadrados
suma_cuadrados = sum(cuadrados)

# Paso 5: Dividir entre (n - 1)
varianza = suma_cuadrados / (cantidad_datos - 1)

# Paso 6: Sacar la raíz cuadrada para obtener la desviación estándar
desviacion_estandar = math.sqrt(varianza)

print(f"Desviación estándar (cálculo manual): {desviacion_estandar}")

