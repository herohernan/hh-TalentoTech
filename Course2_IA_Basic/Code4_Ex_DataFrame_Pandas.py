# Exercise4:
# Dataframe 
# Use the pandas library in python

import pandas as pd

# create DataFrame
# > Note: but we can import a Excel file too 
data = {
    'name':   ['Alicia', 'Bob', 'Carlos', 'David', 'Evelyn'],
    'age':    [25, 30, 35, 40, 22 ],
    'salary': [50000, 55000, 60000, 65000, 48000]
}

# print original DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# print only the 'name' column from DataFrame 
print("\nColumna 'name':")
print(df['name'])

# print the first row of the DataFrame
print("\nFirst row of the DataFrame:")
print(df.iloc[0])

# print the DataFrame filtered by age > 30
print("\nFilter people older than 30 years old:")
filtered_df = df[df['age']>30]
print(filtered_df)

# add new column 'salaryIncrease' calculating the 20% for everyone
df['salaryIncrease'] = df['salary'] * 0.2
print("\nDataFrame with the new column 'salaryIncrease'")
print(df)

# calculate a descriptive statistics (statistics summary)
#    count = número de valores o nulos en la columna
#    mean  = media aritmética (promedio)
#    std   = desviación estándar (variabilidad de los datos)
#    min   = valor mínimo
#    25%   = primer cuartil (percentil 25, el 25% de los datos están por debajo)
#    50%   = mediana (percentil 50, el valor central)
#    75%   = tercer cuartil (percentil 75, el 75% de los datos están por debajo)
#    max   = valor máximo
print("\nDescriptive Statistics for the DataFrame")
print(df.describe())