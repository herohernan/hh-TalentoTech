from itertools import permutations
import matplotlib.pyplot as plt 

# data (distancias entre ciudades)
matrixDeCiudades = [[0,  10, 15, 20],
                    [10, 0,  35, 25],
                    [15, 35, 0 , 30],
                    [20, 25, 30, 0]]

# datos iniciales
ciudadInicial = 0
totalCiudades = len(matrixDeCiudades)
ciudades = list(range(totalCiudades))
rutas = permutations(ciudades[1:]) # genera todas las posibles permutaciones excluyendo la primera ciudad ciudades[0]
# rutas:
# 1, 2, 3,
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1

mejorDistancia = 999_999_999
mejorRuta = None

# Algoritmo
for ruta in rutas:
    distanciaTotal = 0
    ciudadActual = ciudadInicial
    for siguienteCiudad in ruta:
        distanciaTotal = distanciaTotal + matrixDeCiudades[ciudadActual][siguienteCiudad]
        ciudadActual = siguienteCiudad
    distanciaTotal = distanciaTotal + matrixDeCiudades[ciudadActual][0] # regresar a la ciudad 0
    print(f"evaluacion actual de ruta {(0,) + ruta + (0,)} da una distancia total de: {distanciaTotal}")

    # encontrar ruta más corta
    if distanciaTotal < mejorDistancia:
        mejorDistancia = distanciaTotal
        mejorRuta = (0,) + ruta + (0,)

# resultado
print(mejorDistancia)
print(mejorRuta)
