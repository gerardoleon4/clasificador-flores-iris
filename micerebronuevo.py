import pandas as pd
import joblib 

print("El cerebro se esta cargando espera un momento...")
cerebro_cargado=joblib.load('cerebro.joblib')
print("Cerebro cargado de manera correcta")
print("+"*100)

while True:
    print("---------------------------------------------")
    print("ML PARA CLASIFICACIÓN DE FLORES IRIS")
    print("---------------------------------------------")
    print("ESCRIBE 'salir' PARA TERMINAR EL PROGRAMA")
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
        prediccion_final=cerebro_cargado.predict(flor_inventada)[0]
        print("---------------------------------------------")
        print("---------------------------------------------")
        print(f"La especie de la flor es: {prediccion_final}")
        print("---------------------------------------------")
        print("---------------------------------------------")
    except ValueError:
        print("---------------------------------------------")
        print("\nPor favor, ingresa un valor numérico válido para las dimensiones de la flor.")