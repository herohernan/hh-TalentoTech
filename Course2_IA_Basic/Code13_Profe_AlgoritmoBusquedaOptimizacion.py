Enunciado del Ejercicio: Problema del Viajante de Comercio (TSP)
Objetivo:
El objetivo de este ejercicio es implementar un algoritmo de optimización para resolver el Problema del Viajante de Comercio 
utilizando el enfoque de fuerza bruta o backtracking (debido a que la solución exacta puede ser costosa para grandes cantidades de ciudades).

Enunciado:
Imagina que un vendedor debe visitar varias ciudades y regresar a su ciudad de origen. El problema consiste en encontrar el camino
 más corto posible que pase por cada ciudad exactamente una vez y regrese a la ciudad de origen.

Datos:

Tienes 4 ciudades representadas por índices (0, 1, 2, 3), y las distancias entre ellas son las siguientes:

Ciudad	0	1	2	3
0	0	10	15	20
1	10	0	35	25
2	15	35	0	30
3	20	25	30	0
El vendedor comienza en la ciudad 0 y debe visitar todas las demás ciudades exactamente una vez, luego regresar a la ciudad de origen (ciudad 0).

Debes implementar un algoritmo que calcule la distancia mínima del recorrido.

Instrucciones:
Implementar el algoritmo de optimización: Usa un algoritmo basado en fuerza bruta o backtracking para probar todas las permutaciones
 posibles de las ciudades y encontrar el recorrido más corto.
Prueba el algoritmo: Usa los datos proporcionados para calcular la distancia mínima total del recorrido.



import itertools

# Función para calcular la distancia total de un recorrido dado
def calcular_distancia(perm, distancias):
    distancia_total = 0
    # Recorrer la permutación de las ciudades
    for i in range(len(perm) - 1):
        distancia_total += distancias[perm[i]][perm[i + 1]]
    # Agregar la distancia de regreso a la ciudad inicial
    distancia_total += distancias[perm[-1]][perm[0]]
    return distancia_total

# Función para resolver el problema del viajante de comercio (TSP)
def viajante_comercio(distancias):
    # Obtener todas las permutaciones posibles de las ciudades (sin la ciudad 0, ya que es la de origen)
    ciudades = list(range(1, len(distancias)))
    permutaciones = itertools.permutations(ciudades)
    
    distancia_minima = float('inf')
    mejor_ruta = None

    # Evaluar cada permutación de las ciudades
    for perm in permutaciones:
        ruta = [0] + list(perm)  # Ruta que comienza desde la ciudad 0
        distancia_actual = calcular_distancia(ruta, distancias)
        
        # Verificar si la ruta actual es mejor que la anterior
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = ruta

    return mejor_ruta, distancia_minima

# Matriz de distancias entre ciudades
distancias = [
    [0, 10, 15, 20],  # Distancias desde la ciudad 0
    [10, 0, 35, 25],  # Distancias desde la ciudad 1
    [15, 35, 0, 30],  # Distancias desde la ciudad 2
    [20, 25, 30, 0]   # Distancias desde la ciudad 3
]

# Llamar a la función para obtener la mejor ruta y su distancia
mejor_ruta, distancia_minima = viajante_comercio(distancias)

# Mostrar el resultado
print(f"La mejor ruta es: {mejor_ruta}")
print(f"La distancia mínima es: {distancia_minima}")




Codigo de Ahora la ruta detallada por ciudades y paso a paso cual ciudad recorrer en orden


import itertools

# Función para calcular la distancia total de un recorrido dado
def calcular_distancia(perm, distancias):
    distancia_total = 0
    # Recorrer la permutación de las ciudades
    for i in range(len(perm) - 1):
        distancia_total += distancias[perm[i]][perm[i + 1]]
    # Agregar la distancia de regreso a la ciudad inicial
    distancia_total += distancias[perm[-1]][perm[0]]
    return distancia_total

# Función para resolver el problema del viajante de comercio (TSP)
def viajante_comercio(distancias, ciudades):
    # Obtener todas las permutaciones posibles de las ciudades (sin la ciudad 0, ya que es la de origen)
    ciudades_indices = list(range(1, len(distancias)))  # Ciudades sin la ciudad 0
    permutaciones = itertools.permutations(ciudades_indices)
    
    distancia_minima = float('inf')
    mejor_ruta = None

    # Evaluar cada permutación de las ciudades
    for perm in permutaciones:
        ruta = [0] + list(perm)  # Ruta que comienza desde la ciudad 0
        distancia_actual = calcular_distancia(ruta, distancias)
        
        # Verificar si la ruta actual es mejor que la anterior
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = ruta

    # Convertir la ruta de índices a nombres de ciudades
    ruta_ciudades = [ciudades[i] for i in mejor_ruta]
    
    return ruta_ciudades, distancia_minima

# Nombres de las ciudades colombianas
ciudades = ["Bogotá", "Medellín", "Cali", "Cartagena"]

# Matriz de distancias entre ciudades
distancias = [
    [0, 380, 450, 1100],  # Distancias desde Bogotá
    [380, 0, 440, 650],   # Distancias desde Medellín
    [450, 440, 0, 1050],  # Distancias desde Cali
    [1100, 650, 1050, 0]  # Distancias desde Cartagena
]

# Llamar a la función para obtener la mejor ruta y su distancia
mejor_ruta, distancia_minima = viajante_comercio(distancias, ciudades)

# Mostrar el resultado
print(f"La mejor ciudad para empezar es: {mejor_ruta[0]}")
print("El orden de las ciudades a visitar es:")
for ciudad in mejor_ruta:
    print(f"- {ciudad}")
print(f"La distancia mínima es: {distancia_minima} km")




Ahora que grafique el recorrido

import itertools
import matplotlib.pyplot as plt

# Función para calcular la distancia total de un recorrido dado
def calcular_distancia(perm, distancias):
    distancia_total = 0
    # Recorrer la permutación de las ciudades
    for i in range(len(perm) - 1):
        distancia_total += distancias[perm[i]][perm[i + 1]]
    # Agregar la distancia de regreso a la ciudad inicial
    distancia_total += distancias[perm[-1]][perm[0]]
    return distancia_total

# Función para resolver el problema del viajante de comercio (TSP)
def viajante_comercio(distancias, ciudades, coordenadas):
    # Obtener todas las permutaciones posibles de las ciudades (sin la ciudad 0, ya que es la de origen)
    ciudades_indices = list(range(1, len(distancias)))  # Ciudades sin la ciudad 0
    permutaciones = itertools.permutations(ciudades_indices)
    
    distancia_minima = float('inf')
    mejor_ruta = None

    # Evaluar cada permutación de las ciudades
    for perm in permutaciones:
        ruta = [0] + list(perm)  # Ruta que comienza desde la ciudad 0
        distancia_actual = calcular_distancia(ruta, distancias)
        
        # Verificar si la ruta actual es mejor que la anterior
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = ruta

    # Convertir la ruta de índices a nombres de ciudades
    ruta_ciudades = [ciudades[i] for i in mejor_ruta]
    ruta_coordenadas = [coordenadas[i] for i in mejor_ruta]
    
    return ruta_ciudades, ruta_coordenadas, distancia_minima

# Nombres de las ciudades colombianas
ciudades = ["Bogotá", "Medellín", "Cali", "Cartagena"]

# Matriz de distancias entre ciudades
distancias = [
    [0, 380, 450, 1100],  # Distancias desde Bogotá
    [380, 0, 440, 650],   # Distancias desde Medellín
    [450, 440, 0, 1050],  # Distancias desde Cali
    [1100, 650, 1050, 0]  # Distancias desde Cartagena
]

# Coordenadas aproximadas de las ciudades (latitud, longitud)
coordenadas = [
    (4.60971, -74.08175),  # Bogotá
    (6.25184, -75.56359),  # Medellín
    (3.45165, -76.53198),  # Cali
    (10.39104, -75.47942)  # Cartagena
]

# Llamar a la función para obtener la mejor ruta, coordenadas y su distancia
mejor_ruta, mejor_ruta_coordenadas, distancia_minima = viajante_comercio(distancias, ciudades, coordenadas)

# Mostrar el resultado
print(f"La mejor ciudad para empezar es: {mejor_ruta[0]}")
print("El orden de las ciudades a visitar es:")
for ciudad in mejor_ruta:
    print(f"- {ciudad}")
print(f"La distancia mínima es: {distancia_minima} km")

# Graficar la ruta en un plano
plt.figure(figsize=(8, 6))

# Extraemos las latitudes y longitudes en el orden correcto
latitudes = [coord[0] for coord in mejor_ruta_coordenadas]
longitudes = [coord[1] for coord in mejor_ruta_coordenadas]

# Graficamos los puntos (ciudades) y las rutas entre ellas en el orden correcto
plt.plot(longitudes, latitudes, marker='o', color='b', linestyle='-', markersize=8)

# Etiquetas para cada ciudad
for i, ciudad in enumerate(mejor_ruta):
    plt.text(longitudes[i] + 0.02, latitudes[i] + 0.02, ciudad, fontsize=12, ha='left')

# Conectar las ciudades con las distancias
for i in range(len(mejor_ruta_coordenadas) - 1):
    lat1, lon1 = mejor_ruta_coordenadas[i]
    lat2, lon2 = mejor_ruta_coordenadas[i + 1]
    
    # Acceder al índice correcto de la ciudad
    indice_ciudad_origen = ciudades.index(mejor_ruta[i])
    indice_ciudad_destino = ciudades.index(mejor_ruta[i + 1])
    
    # Calcular la distancia entre las ciudades
    distancia_segmento = distancias[indice_ciudad_origen][indice_ciudad_destino]
    
    # Añadir texto de la distancia entre las ciudades en la mitad de cada segmento
    plt.text((lon1 + lon2) / 2 + 0.02, (lat1 + lat2) / 2 + 0.02, f"{distancia_segmento} km", fontsize=10, color='red')

# Título y etiquetas
plt.title('Ruta Óptima del Viajante de Comercio (TSP)', fontsize=14)
plt.xlabel('Longitud (Coordenadas)', fontsize=12)
plt.ylabel('Latitud (Coordenadas)', fontsize=12)

# Mostrar el gráfico
plt.grid(True)
plt.show()

