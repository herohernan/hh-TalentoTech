# Exercise1 (hh version):
# supervised learning about linear regression
# Relation between the independent variable (x) and the dependent variable (y) for a sensor
# y = 2*x + 1

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

# Data
x = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]]) # real values
y = np.array([9.8, 19.5, 29.2, 39.0, 49.1, 59.5, 69.3, 79.8, 89.2, 99.6]) # values gotten by the sensor

# model and training
model = LinearRegression()
model.fit(x, y)

# prediction and result
realValueExpected = 55
predictedValueOfSensor = model.predict([[realValueExpected]])
print(f"Correction for real {realValueExpected}cm: {predictedValueOfSensor[0]:.2f}")

# plot
plt.style.use('dark_background')
plt.scatter(x, y, color='blue', label='Sensor Measurements') 
plt.plot(x, model.predict(x), color='red', label='Fitted line') 
for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i,0]:.1f}, {y[i]:.1f})", fontsize=9, ha='right', va='bottom')
plt.title('Linear Regresion')
plt.xlabel('Real value (cm)')
plt.ylabel('Values gotten by the sensor')
plt.grid(color='gray')
plt.legend()

plt.show()
