import pandas as pd
import joblib
from pathlib import Path

#CARGAR EL CEREBRO ENTRENADO (NO NECESITA LA BASE DE DATOS)
modelo=joblib.load(Path(__file__).parent.parent/'modelo'/'cerebro.joblib')
columnas=modelo.feature_names_in_

while True:
    print('----------------------------------------------------------------------')
    print("CLASIFICADOR DE FLORES IRIS (USANDO cerebro.joblib)")
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
                                  ]],columns=columnas)
        prediccion_final=modelo.predict(flor_nueva)
        print(f" ES DE TIPO: {prediccion_final[0]}")
    except ValueError:
        print("ERROR EN LOS VALORES, NO SON VALIDOS")
