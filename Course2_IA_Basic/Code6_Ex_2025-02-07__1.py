# Exercise4:
# Dataframe 
# Use the pandas library in python

import pandas as pd

# dataframe
data = {
    'producto': ['Camiseta','Pantalon','Sombrero','Zapatos','Chaqueta'],
    'cantidad': [10,5,12,8,3],
    'precioUnitario': [15,25,10,50,40],
    'fecha': ['2025-01-01','2025-01-02','2025-01-02','2025-01-03','2025-01-04']
}

# print original DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# add new column 'totalDeVentas' calculating the 20% for everyone
df['totalDeVentas'] = df['precioUnitario'] * df['cantidad']
print("\nDataFrame with the new column 'totalDeVentas'")
print(df)


# print the DataFrame filtered by: productos vendidos en la fecha 2025-01-02
print("\nProductos vendidos en la fecha 2025-01-02:")
filtered_df = df[df['fecha']=='2025-01-02']
print(filtered_df)

# sacar el producto más vendido
# print the first row of the DataFrame
print("\nProducto más vendido:")
print(df.loc[df["totalDeVentas"].idxmax(), "producto"])
print(df.iloc[df["totalDeVentas"].idxmax(), 0])
# hacen lo mismo pero el primero loc toma el indice por la etiqueta, el segundo el indice de posición