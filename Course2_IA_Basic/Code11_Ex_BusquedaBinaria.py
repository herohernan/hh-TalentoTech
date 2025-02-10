import time
import pandas as pd

# Función de Búsqueda Secuencial
def busqueda_secuencial(lista, objetivo):
    # Recorremos toda la lista
    for i in range(len(lista)):
        # Comprobamos si el elemento actual es igual al objetivo
        if lista[i] == objetivo:
            return i  # Retornamos el índice donde encontramos el objetivo
    return -1  # Si no encontramos el objetivo, retornamos -1

# Funcion de busqueda binaria
def busqueda_binaria(lista, objetivo):
    # indices de inicio y fin
    inicio = 0 
    fin = len(lista)-1

    while inicio <= fin:
        # calcular el indice medio
        medio = (inicio+fin)//2 # / = división flotante y // división entera
        # comprobar si el elemento es ele medio objetivo
        if lista[medio] == objetivo:
            return medio # elemento encontrado
        # si el objetivo es menor al valor medio,
        #  buscar en la mitad izquierda
        elif lista[medio] > objetivo:
            fin = medio-1
        # si el objetivo es mayor al valor medio,
        #  buscar en la mitad derecha
        else:
            inicio = medio+1
    return -1 # elemento no encontrado 

# Function Print result
def imprimir_resultado(valorObjetivo, resultado):
    if (resultado != -1):
        print(f"el valor [{valorObjetivo}] se encunentra en el index [{resultado}] de la lista")
    else:
        print(f"el valor [{valorObjetivo}] no se encunentra en la lista")

# lista de un millón de datos y valor objetivo
lista = [i for i in range(1_000_000)] # lis5ta ordenada
valorObjetivo = 987_620

# Algoritmo#1 de busqueda secuencial
time_inicio = time.perf_counter()
resultado = busqueda_secuencial(lista, valorObjetivo)
time_fin = time.perf_counter()
time_algoritmo1 = time_fin - time_inicio
imprimir_resultado(valorObjetivo, resultado)

# Algoritmo#2 de busqueda binaria
time_inicio = time.perf_counter()
resultado = busqueda_binaria(lista, valorObjetivo)
time_fin = time.perf_counter()
time_algoritmo2 = time_fin - time_inicio
imprimir_resultado(valorObjetivo, resultado)

# Algoritmo#3 usando pandas
df = pd.Series(lista)
time_inicio = time.perf_counter()
indice = df[df == valorObjetivo].index[0]
time_fin = time.perf_counter()
time_algoritmo3 = time_fin - time_inicio
imprimir_resultado(valorObjetivo, resultado)

# Medición de tiempos
print(f"El tiempo utilizado en la busqueda secuencial fue: {time_algoritmo1:.6f} ms")
print(f"El tiempo utilizado en la busqueda binaria fue: {time_algoritmo2:.6f} ms")
print(f"El tiempo utilizado en la busqueda por pandas fue: {time_algoritmo3:.6f} ms")


