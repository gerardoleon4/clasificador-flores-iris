import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from conexion import obtener_conexion
conexion=obtener_conexion()
query="SELECT*FROM iris"
df_iris=pd.read_sql(query,conexion)

#separar variables "X" y "y"
X=df_iris.drop(columns=['Id', 'Species'])
y=df_iris['Species']

#dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)
print(f"Flores para estudiar(entrenamiento): {len(X_train)}")
print(f"Flores para probar(prueba) son: {len(X_test)}")

#crear el modelo de árbol de decisión
modelo_arbol=DecisionTreeClassifier(random_state=42)
modelo_arbol.fit(X_train, y_train)

while True:
    print("ML PARA CLASIFICACIÓN DE FLORES IRIS")
    print("ESCRIBE 'salir' PARA TERMINAR EL PROGRAMA")
    print("---------------------------------------------")
    try:
        dato1=input("Escribe el largo del sépalo: ")
        if dato1.lower() == 'salir': break
        sepal_length=float(dato1)
        dato2=input("Escribe el ancho del sépalo: ")
        if dato2.lower() == 'salir': break
        sepal_width=float(dato2)
        dato3=input("Escribe el largo del pétalo: ")
        if dato3.lower() == 'salir': break
        petal_length=float(dato3)
        dato4=input("Escribe el ancho del pétalo: ")
        if dato4.lower() == 'salir': break
        petal_width=float(dato4)

        flor_inventada=pd.DataFrame([{'SepalLengthCm':sepal_length, 'SepalWidthCm':sepal_width, 
                                      'PetalLengthCm':petal_length, 'PetalWidthCm':petal_width}])
        prediccion_final=modelo_arbol.predict(flor_inventada)[0]
        print(f"La especie de la flor es: {prediccion_final}")
    except ValueError:
        print("\nPor favor, ingresa un valor numérico válido para las dimensiones de la flor.")