# Exercise1:
# supervised learning using linear regression
# Relation between the independent variable (x) and the dependent variable (y) 
# y = 2*x + 1

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

# data
x = np.array([[1], [2], [3], [4]])
y = np.array([2, 3, 4, 5])

# model and training
model = LinearRegression()
model.fit(x, y)

# predictions
y_pred = model.predict(x)
print("Predictions: ", y_pred)

# plot
plt.style.use('dark_background')
plt.scatter(x, y, color='blue', label='Original data') # Points
plt.plot(x, y_pred, color='red', label='Fitted line') # Line
for i in range(len(x)): # Values
    plt.text(x[i], y[i], f"({(x[i,0]):.1f}, {y[i]:.1f})", fontsize=9, ha='right', va='bottom')
plt.title('Linear Regresion')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(color='gray')
plt.legend()

plt.show()
