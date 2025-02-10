# instalar esta libreria para la practica
## pip install pandas openpyxl

import pandas as pd

# read excel file
df = pd.read_excel("./Empleados.xlsx", sheet_name="empleados")

# original data
print("Data original")
print(df)

# sacar el salario promedio por departamento
salarioPromedioPorDepartamento = df.groupby("Departamento")["Salario"].mean()
print("Salario promedio por departamento")
print(salarioPromedioPorDepartamento)

# filtrar empleados con salario superio a 4000 
empleadosConSalarioSuperioA4000 = df[df['Salario']>4000][["Empleado","Salario"]]
print("Empleados con salarios mayores a 4000")
print(empleadosConSalarioSuperioA4000)

# filtrar el empleado más joven y el empleado más antinguo
empleadoMasJoven = df.loc[df['Edad'].idxmin(), ["Empleado", "Edad"]]
empleadoMasViejo = df.loc[df['Edad'].idxmax(), ["Empleado", "Edad"]]

print("Empleado más joven")
print(empleadoMasJoven)
print("Empleado más viejo")
print(empleadoMasViejo)


