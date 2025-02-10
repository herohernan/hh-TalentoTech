import pandas as pd

# read excel file
df = pd.read_csv("./Estudiantes.csv")

# original data
print("Data original")
print(df)

# Calcular la calificación promedio por departamento.
calificacionPromedioPorDepartamento = df.groupby("Departamento")["Calificacion"].mean()
print("calificación promedio por departamento")
print(calificacionPromedioPorDepartamento)

# Filtrar los estudiantes cuya calificación sea superior a 80.
estudiantesConCalificacionSuperiorA8 = df[df['Calificacion']>8.0][["Nombre"]]
print("estudiantes cuya calificación sea superior a 8")
print(estudiantesConCalificacionSuperiorA8)

# Calcular el porcentaje de estudiantes con beca.
numeroDeEstudiantesConBeca = df[df["Beca"]=="Si"]["Beca"].count()
totalDeElementos = df.shape[0] # o con len 
porcentajeDeEstudiantesConBeca = numeroDeEstudiantesConBeca * 100 / totalDeElementos
print("porcentaje de estudiantes con beca")
print(f"{porcentajeDeEstudiantesConBeca}%")

# Calcular el porcentaje de estudiantes con beca pero con lennumeroDeEstudiantesConBeca = df[df["Beca"]=="Si"]["Beca"].count()
numeroDeEstudiantesConBeca_2 = len(df[df["Beca"]=="Si"])
totalDeElementos_2 = len(df) 
porcentajeDeEstudiantesConBeca_2 = numeroDeEstudiantesConBeca_2 * 100 / totalDeElementos_2
print("porcentaje de estudiantes con beca")
print(f"{porcentajeDeEstudiantesConBeca_2}%")