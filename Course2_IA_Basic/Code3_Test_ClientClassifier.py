# Test for the Exercise3:
# Decision Tree Classifier
# Classify the clients into 2 groups

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from enum import Enum 

# possible decisions
class Decision(Enum):
    OCASIONALLY = 0  # the client but OCASIONALLY
    FRECUENTLY = 1   # the client but FRECUENTLY

# training data
# datum1 : frecuency       = Cliente frecuency (number of days between purchases)
# datum2 : averageSpending = Average spending on each purchase 
x = np.array([
    [30, 20],
    [15, 50],
    [10, 45],
    [25, 35],
    [5, 60],
    [20, 25],
    [12, 55],
    [18, 40]
])

# output labels (Client decision)
y = np.array([
    Decision.OCASIONALLY.value,
    Decision.FRECUENTLY.value,
    Decision.FRECUENTLY.value,
    Decision.OCASIONALLY.value,
    Decision.FRECUENTLY.value,
    Decision.OCASIONALLY.value,
    Decision.FRECUENTLY.value,
    Decision.OCASIONALLY.value
])

# model and training
model = DecisionTreeClassifier(criterion='gini') 
model.fit(x,y)

# prediction
newClient = [[30, 20]]
prediction = model.predict(newClient)

# result 
print(f"Prediction for the newClient [{newClient}] = {prediction}") 

# plot
plt.figure(figsize=(6,6)) 
plot_tree(model, 
          filled=True, 
          feature_names=["frecuency", "averageSpending"], 
          class_names=[e.name for e in Decision])
plt.title('Client decision')
plt.show()
    