import statistics  # Importa el módulo statistics, que contiene funciones para realizar cálculos estadísticos

with open('numeros.txt', 'r') as file:  # Abre el archivo 'numeros.txt' en modo de lectura ('r')
    numeros = [int(line.strip()) for line in file]  
    # Lee cada línea del archivo, elimina espacios en blanco y saltos de línea con strip(), 
    # convierte cada línea en un entero y lo almacena en la lista 'numeros'

# Calcular la media (promedio) de los números
media = statistics.mean(numeros)
# La función mean() del módulo statistics calcula y devuelve la media aritmética de la lista 'numeros'

# Calcular la mediana (valor central) de los números
mediana = statistics.median(numeros)
# La función median() del módulo statistics encuentra y devuelve la mediana de la lista 'numeros'

# Calcular la moda (valor más frecuente) de los números
try:
    moda = statistics.mode(numeros)
    # La función mode() del módulo statistics devuelve el valor más frecuente en la lista 'numeros'
except statistics.StatisticsError:
    moda = "No hay una moda única"
    # Si no hay un único valor que sea más frecuente (es decir, hay más de una moda o ninguna), 
    # se lanza una excepción StatisticsError, y en ese caso, asignamos el mensaje "No hay una moda única"

# Calcular la desviación estándar (medida de la dispersión) de los números
desviacion_estandar = statistics.stdev(numeros)
# La función stdev() del módulo statistics calcula y devuelve la desviación estándar de la lista 'numeros', 
# que mide la cantidad de variación o dispersión de los datos

# Imprimir los resultados
print(f"Media: {media}")
# Muestra el valor calculado de la media
print(f"Mediana: {mediana}")
# Muestra el valor calculado de la mediana
print(f"Moda: {moda}")
# Muestra el valor calculado de la moda, o el mensaje "No hay una moda única" si no existe una moda única
print(f"Desviacion Estandar: {desviacion_estandar}")
# Muestra el valor calculado de la desviación estándar
