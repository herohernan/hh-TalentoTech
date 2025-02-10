from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# cargar dataset de digitos
digits = load_digits()
x = digits.data    # caracteristicas de las imágenes
y = digits.target  # etiquetas digitos reales

# crear el modelos KMeans para 10 cluster
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(x)

# predecir el cluster para una muestra de prueba 
sample_image = x[0].reshape(1, -1)
predicted_cluster = kmeans.predict(sample_image)
print(f"El digito de la muestra esta en el cluster:{predicted_cluster}")

# mostrar los cluster
fig, axes = plt.subplots(2,5, figsize=(10,5)) # nos va a mostrar dos filas de 5 columnas
centroids = kmeans.cluster_centers_.reshape(10,8,8) # se redimensionan los pixeles

for ax, centroid in zip(axes.ravel(), centroids):
    ax.imshow(centroid, cmap=plt.cm.binary)
    ax.axis('off')

plt.suptitle('Centroides de los clusters de digitos', fontsize=16)
plt.show()
