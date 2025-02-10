# algoritmo de aprendizaje supervizado 
# predecir si un tumor de cancer es maligno o benigno
# usando una libreria que ya tiene info de ese tema 

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# cargar la db
data = load_breast_cancer()
x = data.data # características
y = data.target # etiquetas (maligno=0, benigno=1)

# model and training (70% entrenamiento y 30% prueba)
seedRandomState = 42
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=seedRandomState)
clf = RandomForestClassifier(n_estimators=100, random_state=seedRandomState) # clasificar 100 tipos de arboles
clf.fit(x_train, y_train)

# predicciones
y_pred = clf.predict(x_test)

# mostrar el reporte
print("Reporte de clasificación")
print(classification_report(y_test,y_pred))