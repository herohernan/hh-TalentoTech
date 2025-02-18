# Exercise2:
# K-NN (K-Nearest Neighbors) algoritm
# Clasification and regresion algoritm

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# create data set
x = [[0],[3],[9],[7]] # input data
y = [0, 0, 1, 1] # labels (group 0 or 1)

# model and training
model = KNeighborsClassifier(n_neighbors=3) # 3 = average all and show three nearest neighbors
model.fit(x,y)

# prediction
pointToPredict = [[7.5]]
predictions = model.predict(pointToPredict)
print(f"Prediction for the point [{pointToPredict}] = {predictions}")

### PLOT ### 
plt.style.use('dark_background')
plt.title('K.NN algoritm of classification')
plt.xlabel('value')
plt.ylabel('class')
plt.grid('gray')
# plot: groups
plt.scatter(x[:2], y[:2], color='blue', label="class 0", s=200)
plt.scatter(x[2:4], y[2:4], color='red', label="class 1", s=200)
# plot: prediction
plt.scatter(pointToPredict[0], predictions, color='green', label="prediction", s=200)

plt.legend()
plt.show()
