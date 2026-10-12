import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from conexion import obtener_conexion

conexion=obtener_conexion()
query="SELECT * FROM iris"
df_iris=pd.read_sql(query,conexion)

#SEPARAR VARIABLES "X","Y"
X=df_iris.drop(columns=['Id','Species'])
y=df_iris['Species']

#DIVIDIR LOS DATOS DE ENTRENAMIENTO Y PRUEBA
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.20,random_state=42)
print(f"LAS FLORES PARA ESTUDIAR (ENTRENAMIENTO): {len(X_train)}")
print(f"LAS FLORES PARA MI EXAMEN (PRUEBA) SON:{len(X_test)}")

#CREAR UN MODELO DE ÁRBOL DE DECISIÓN
modelo_arbol=DecisionTreeClassifier(random_state=42)
modelo_arbol.fit(X_train,y_train)

predicciones=modelo_arbol.predict(X_test)
precision=accuracy_score(y_test,predicciones)
print(f"TU MODELO TIENE UNA EFECTIVIDAD DEL :{precision*100}%")

while True:
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print("ML PARA CLASIFICAR ESPECIES DE FLORES IRIS")
    print('ESCRIBE "salir" PARA FINALIZAR EL PROGRAMA')
    try:
        dato1=input("1-ESCRIBE EL LARGO DEL SÉPALO: ")
        if dato1.lower()=="salir":break
        sepal_length=float(dato1)

        dato2=input("2-ESCRIBE EL ANCHO DEL SÉPALO: ")
        if dato2.lower()=="salir":break
        sepal_width=float(dato2)

        dato3=input("3-ESCRIBE EL LARGO DEL PÉTALO: ")
        if dato3.lower()=="salir":break
        petal_length=float(dato3)

        dato4=input("4-ESCRIBE EL ANCHO DEL PÉTALO: ")
        if dato4.lower()=="salir":break
        petal_width=float(dato4)

        flor_nueva=pd.DataFrame([[sepal_length,
                                  sepal_width,
                                  petal_length,
                                  petal_width
                                  ]],columns=X.columns)
        prediccion_final=modelo_arbol.predict(flor_nueva)
        print(f" ES DE TIPO: {prediccion_final[0]}")
    except ValueError:
        print("ERROR EN LOS VALORES, NO SON VALIDOS")


                                
   