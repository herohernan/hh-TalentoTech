import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import tree

# Datos de entrada (simulados)
data = {
    'Ingreso': [3500, 4500, 5000, 1500, 2000, 7000, 6000, 3000, 5500, 2500],
    'Numero de dependientes': [2, 3, 1, 4, 2, 1, 0, 2, 3, 1],
    'Antigüedad laboral': [5, 10, 3, 1, 2, 12, 7, 4, 9, 3],
    'Tipo de empleo': ['Tiempo completo', 'Medio tiempo', 'Independiente', 'Tiempo completo', 'Medio tiempo',
                       'Tiempo completo', 'Independiente', 'Tiempo completo', 'Medio tiempo', 'Tiempo completo'],
    'Riesgo de crédito': [1, 1, 0, 1, 0, 0, 0, 1, 1, 0]  # 0: Bajo riesgo, 1: Alto riesgo
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Convertir la variable 'Tipo de empleo' en valores numéricos
df['Tipo de empleo'] = df['Tipo de empleo'].map({'Tiempo completo': 0, 'Medio tiempo': 1, 'Independiente': 2})

# Separar las características (X) y la etiqueta (y)
X = df[['Ingreso', 'Numero de dependientes', 'Antigüedad laboral', 'Tipo de empleo']]  # Características
y = df['Riesgo de crédito']  # Etiqueta

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier(criterion='entropy', random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicción sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Realizar predicción sobre todo el conjunto de datos (o conjunto de prueba)
y_pred_all = model.predict(X)

# Añadir las predicciones al DataFrame original
df['Predicción Riesgo de Crédito'] = y_pred_all

# Filtrar clientes por tipo de riesgo
alto_riesgo = df[df['Predicción Riesgo de Crédito'] == 1]
bajo_riesgo = df[df['Predicción Riesgo de Crédito'] == 0]

# Mostrar los resultados
print("Clientes de Alto Riesgo:")
print(alto_riesgo[['Ingreso', 'Numero de dependientes', 'Antigüedad laboral', 'Tipo de empleo', 'Predicción Riesgo de Crédito']])

print("\nClientes de Bajo Riesgo:")
print(bajo_riesgo[['Ingreso', 'Numero de dependientes', 'Antigüedad laboral', 'Tipo de empleo', 'Predicción Riesgo de Crédito']])


# Graficar el árbol de decisión
plt.figure(figsize=(12, 8))
tree.plot_tree(model, filled=True, feature_names=['Ingreso', 'Numero de dependientes', 'Antigüedad laboral', 'Tipo de empleo'],
               class_names=['Bajo riesgo', 'Alto riesgo'], fontsize=10)

plt.title("Árbol de decisión para clasificación de Riesgo de Crédito")
plt.show()
