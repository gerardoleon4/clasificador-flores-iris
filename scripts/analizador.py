import pandas as pd
import matplotlib.pyplot as plt 
from conexion import obtener_conexion
conexion = obtener_conexion()
query = "SELECT * FROM iris"
df = pd.read_sql(query, conexion)
print("ESTAS SON LAS PRIMERAS 5 FILAS QUE SE MUESTRAN DE LA BASE DE DATOS")
print(df.head())

query_rangos = """Select Species, min(PetalWidthCm) as min_ancho_petalo,
max(PetalWidthCm) as max_ancho_petalo
from iris
group by Species"""
df_rangos = pd.read_sql(query_rangos, conexion)
print('----------------------------------------------------------------------')
print("Rangos de ancho petalo")
print(df_rangos)

query_rangos_petalo_largo = """Select Species, min(PetalLengthCm) as min_largo_petalo,
max(PetalLengthCm) as max_largo_petalo
from iris
group by Species"""
df_rangos_petalo_largo = pd.read_sql(query_rangos_petalo_largo, conexion)
print('----------------------------------------------------------------------')
print("Rangos de largo de petalo")
print(df_rangos_petalo_largo)

query_rangos_sepalo_largo = """Select Species, min(SepalLengthCm) as min_largo_sepalo,
max(SepalLengthCm) as max_largo_sepalo
from iris
group by Species"""
df_rangos_sepalo_largo = pd.read_sql(query_rangos_sepalo_largo, conexion)
print('----------------------------------------------------------------------')
print("Rangos de largo de sepalo")
print(df_rangos_sepalo_largo)



query_rangos_sepalo_ancho = """Select Species, min(SepalWidthCm) as min_ancho_sepalo,
max(SepalWidthCm) as max_ancho_sepalo
from iris
group by Species"""
df_rangos_sepalo_ancho = pd.read_sql(query_rangos_sepalo_ancho, conexion)
print('----------------------------------------------------------------------')
print("Rangos de ancho de sepalo")
print(df_rangos_sepalo_ancho)




query_promedios= """
Select Species,
AVG(SepalLengthCm) as promedio_sepalo_largo,
AVG(SepalWidthCm) as promedio_sepalo_ancho,
AVG(PetalLengthCm) as promedio_petalo_largo,
AVG(PetalWidthCm) as promedio_petalo_ancho
From iris
Group by Species
"""
df_promedios = pd.read_sql(query_promedios, conexion)
print("\n----Promedios por especie calculados desde la base de datos----")
print(df_promedios) 



query_setosa = "Select SepalLengthCm, SepalWidthCm from iris where Species = 'Iris-setosa'"
df_setosa = pd.read_sql(query_setosa, conexion)
print('\n----Datos exclusivos para iris setosa ---')
print(df_setosa)

query_versicolor = "Select SepalLengthCm, SepalWidthCm from iris where Species = 'Iris-versicolor'"
df_versicolor = pd.read_sql(query_versicolor, conexion)
print('\n----Datos exclusivos para iris versicolor ---')
print(df_versicolor)

query_virginica = "Select SepalLengthCm, SepalWidthCm from iris where Species = 'Iris-virginica'"
df_virginica = pd.read_sql(query_virginica, conexion)
print('\n----Datos exclusivos para iris virginica ---')
print(df_virginica)

plt.figure (figsize=(8, 5))
plt.scatter (df_setosa['SepalLengthCm'], df_setosa['SepalWidthCm'],
             color='purple', label='Iris-setosa')
plt.title('Tamano de sepalo de la especie setosa')
plt.xlabel('Largo de sepalo (cm)')
plt.ylabel('Ancho de sepalo (cm)')
plt.grid(True)
plt.legend()

plt.figure (figsize=(8, 5))
plt.scatter (df_versicolor['SepalLengthCm'], df_versicolor['SepalWidthCm'],
             color='green', label='Iris-versicolor')
plt.title('Tamano de sepalo de la especie versicolor')
plt.xlabel('Largo de sepalo (cm)')
plt.ylabel('Ancho de sepalo (cm)')
plt.grid(True)
plt.legend()

plt.figure (figsize=(8, 5))
plt.scatter (df_virginica['SepalLengthCm'], df_virginica['SepalWidthCm'],
             color='orange', label='Iris-virginica')
plt.title('Tamano de sepalo de la especie virginica')
plt.xlabel('Largo de sepalo (cm)')
plt.ylabel('Ancho de sepalo (cm)')
plt.grid(True)
plt.legend()

plt.figure (figsize=(8, 5))
plt.scatter (df_setosa['SepalLengthCm'], df_setosa['SepalWidthCm'],
             color='purple', label='Iris-setosa')
plt.scatter (df_versicolor['SepalLengthCm'], df_versicolor['SepalWidthCm'],
             
             color='green', label='Iris-versicolor')
plt.scatter (df_virginica['SepalLengthCm'], df_virginica['SepalWidthCm'],
             color='orange', label='Iris-virginica')
plt.title('Tamano de sepalo de las tres especies')
plt.xlabel('Largo de sepalo (cm)')
plt.ylabel('Ancho de sepalo (cm)')
plt.grid(True)
plt.legend()

plt.show()
