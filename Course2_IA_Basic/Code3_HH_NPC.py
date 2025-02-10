# Exercise3 (hh version):
# Decision Tree Classifier - IA
# NPC in a video game who decides if attack, escape, patrol 
# TODO : IT IS NOT WORKING AS EXPECTED OR CHECK AND KNOW HOW TO INTERPRETATE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from enum import Enum 

# possible decisions
class Decision(Enum):
    PATROL = 0  # player doesn't detected
    ESCAPE = 1  # low life and the player is near
    ATTACK = 2  # Enough life and the player is near 
    
# training data
# to ignore data (with low data set) put a value out of range as 9999 or -1
x = np.array([
    [0, 9999, 100], # player detected (false) --> PATROL
    [1, 10, 90], # player detected (true), distance [m] to the player (far),  current life [%] (high) --> PATROL
    [1, 7, 80],  # player detected (true), distance [m] to the player (far),  current life [%] (high) --> PATROL
    [1, 4, 30],  # player detected (true), distance [m] to the player (near), current life [%] (low)  --> ESCAPE
    [1, 3, 40],  # player detected (true), distance [m] to the player (near), current life [%] (low)  --> ESCAPE  
    [1, 2, 70],  # player detected (true), distance [m] to the player (near), current life [%] (high) --> ATTACK
    [1, 1, 75],  # player detected (true), distance [m] to the player (near), current life [%] (high) --> ATTACK
    [1, 2, 100], # player detected (true), distance [m] to the player (near), current life [%] (high) --> ATTACK
    [1, 3, 88],  # player detected (true), distance [m] to the player (near), current life [%] (high) --> ATTACK
])

# output labels (NPC decision)
y = np.array([
    Decision.PATROL.value,
    Decision.PATROL.value,
    Decision.PATROL.value,
    Decision.ESCAPE.value,
    Decision.ESCAPE.value,
    Decision.ATTACK.value,
    Decision.ATTACK.value,
    Decision.ATTACK.value,
    Decision.ATTACK.value,
])

# model and training
model = DecisionTreeClassifier(criterion='gini') 
# Note: gini (default) = check the impurity of a data between 0 and 1 
#                        0.5 means we have a equitative division between two decisions
#                        0.0 means all the measures are part of the same decision
model.fit(x,y)

# prediction
#pointToPredict = [[1.6]]
#prediction = model.predict(pointToPredict)

# result 
#print(f"Prediction for the point [{pointToPredict}] = {prediction}") 

# plot
plt.figure(figsize=(6,6)) 
plot_tree(model, 
               filled=True, 
               feature_names=["Player detected", "Distance (mt)", "Life (%)"], 
               class_names=[e.name for e in Decision])
plt.title('NPC Decision Tree Classifier - IA')
plt.show()