# Exercise3:
# Decision Tree Classifier
# Clasification and regresion algoritm

from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree

# data set
xRaw = np.array([0, 1, 2, 3])
y =    np.array([0, 0, 1, 1])

x = xRaw.reshape(-1,1) # convert x to a (n,1) format

# model and training
model = DecisionTreeClassifier(criterion='gini') # criterion is the function to measure the quality of a split. 'Gini' measures the impurity 
model.fit(x,y)

# prediction
pointToPredict = [[1.6]]
prediction = model.predict(pointToPredict)
print(f"Prediction for the point [{pointToPredict}] = {prediction}") 

# plot
plt.figure(figsize=(4,6)) # size of the boxes
tree.plot_tree(model, 
               filled=True, 
               feature_names=['x'], 
               class_names=['Class0','Class1'])
plt.title('Decision Tree Classifier')
plt.show()
