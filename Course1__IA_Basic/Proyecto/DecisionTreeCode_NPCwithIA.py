# CREADO POR
# Hernán Hernández 
# Claudia Victoria Rueda

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from enum import Enum 

# Leer Excel que contiene:
#    data de entrenamiento, 
#    la última fila es la data a predecir
#    la última columna son las decisiones (labels)
path = os.path.dirname(os.path.abspath(__file__)) # obtiene el path del archivo actual
df = pd.read_excel(path + "/DataDeEntrenamiento.xlsx", sheet_name="Hoja1")

# Obtener la data
#    x = data de entrenamiento
#    y = decisiones (labels)
x = df.iloc[:-1, :-1].to_numpy() # toma todo ignorando la última columna
yRaw = df.iloc[:-1, -1].to_numpy() # toma la última columna pero quita el último row
Decisiones = Enum("Decisiones", {decision: i for i, decision in enumerate(np.unique(yRaw))}) # crea un enum con las decisiones
y = np.vectorize(lambda x: Decisiones[x].value)(yRaw) # remplaza la palabra clave por el enum.value 

# modelos y entrenamiento
modelGini = DecisionTreeClassifier(criterion='gini', random_state=42) 
modelEntropy = DecisionTreeClassifier(criterion='entropy', random_state=42) 
modelGini.fit(x,y)
modelEntropy.fit(x,y)

# predicción para Gini
estadoActual = df.iloc[-1, :-1].to_numpy().reshape(1, -1) # 1D array to 2D array
prediction = modelGini.predict(estadoActual)
print("La decisión a tomar por parte de la IA es en el modelo Gini es:")
print(Decisiones(prediction).name)

# predicción para Gini
prediction = modelEntropy.predict(estadoActual)
print("La decisión a tomar por parte de la IA es en el modelo Entropy es:")
print(Decisiones(prediction).name)

# plot Gini
plt.figure(figsize=(12,8)) 
plot_tree(modelGini, 
               filled=True, 
               feature_names = df.columns[:-1], # pone automáticamente el nombre de las columnas 
               class_names=[e.name for e in Decisiones])
plt.title('Decision Tree Classifier (Gini) - IA')
plt.savefig(path + '/DecisionTree_Gini.png', dpi=300, bbox_inches='tight')
plt.show()

# plot Entropy
plt.figure(figsize=(12,8)) 
plot_tree(modelEntropy, 
               filled=True, 
               feature_names = df.columns[:-1], # pone automáticamente el nombre de las columnas 
               class_names=[e.name for e in Decisiones])
plt.title('Decision Tree Classifier (Entropy) - IA')
plt.savefig(path + '/DecisionTree_Entropy.png', dpi=300, bbox_inches='tight')
plt.show()

