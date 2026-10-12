from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
app=Flask(__name__)
#carga el modelo cuando se inicia el servidor
modelo=joblib.load('cerebro.joblib')
#las 150 flores exportadas de MySQL (para la gráfica y los rangos normales)
flores=pd.read_json('static/iris.json')
RANGOS={columna:(flores[columna].min(),flores[columna].max()) for columna in modelo.feature_names_in_}

#nombres en español de cada columna para explicar las reglas
NOMBRES={
    'SepalLengthCm':'Largo del sépalo',
    'SepalWidthCm':'Ancho del sépalo',
    'PetalLengthCm':'Largo del pétalo',
    'PetalWidthCm':'Ancho del pétalo',
}

def leer_flor(formulario):
    #recibir datos del formulario
    datos={
        'SepalLengthCm':
        [float(formulario['sepal_lenght'])],
                    'SepalWidthCm':
        [float(formulario['sepal_width'])],
                    'PetalLengthCm':
        [float(formulario['petal_lenght'])],
                    'PetalWidthCm':
        [float(formulario['petal_width'])],
    }
    return pd.DataFrame(datos)

def explicar(df):
    #recorre el camino que siguió la flor dentro del árbol de decisión
    arbol=modelo.tree_
    columnas=list(modelo.feature_names_in_)
    nodos=modelo.decision_path(df).indices
    limites={}
    for nodo in nodos:
        if arbol.children_left[nodo]==arbol.children_right[nodo]:
            continue #es la hoja final, ya no tiene pregunta
        columna=columnas[arbol.feature[nodo]]
        umbral=round(float(arbol.threshold[nodo]),2)
        minimo,maximo=limites.get(columna,(None,None))
        if df[columna].iloc[0]<=umbral:
            maximo=umbral if maximo is None else min(maximo,umbral)
        else:
            minimo=umbral if minimo is None else max(minimo,umbral)
        limites[columna]=(minimo,maximo)
    #juntar las preguntas de una misma medida en una sola regla
    reglas=[]
    for columna,(minimo,maximo) in limites.items():
        nombre=NOMBRES[columna]
        if minimo is not None and maximo is not None:
            reglas.append(f"{nombre} entre {minimo} y {maximo} cm")
        elif maximo is not None:
            reglas.append(f"{nombre} ≤ {maximo} cm")
        else:
            reglas.append(f"{nombre} > {minimo} cm")
    return reglas

def revisar_rangos(df):
    #avisa si alguna medida está fuera de lo que el modelo vio al entrenar
    avisos=[]
    for columna,(minimo,maximo) in RANGOS.items():
        valor=df[columna].iloc[0]
        if valor<minimo or valor>maximo:
            avisos.append(f"{NOMBRES[columna]}: lo normal es de {minimo} a {maximo} cm")
    return avisos

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    try:
        df=leer_flor(request.form)
        #prediccion
        prediccion=modelo.predict(df)[0]
        return render_template('index.html', prediccion=prediccion, reglas=explicar(df), avisos=revisar_rangos(df))
    except Exception as e:
        return render_template('index.html', error="Revisa que todos los campos sean números")

#la página usa esta ruta para clasificar sin recargar
@app.route('/api/predecir', methods=['POST'])
def api_predecir():
    try:
        df=leer_flor(request.form)
        prediccion=modelo.predict(df)[0]
        return jsonify(especie=prediccion, reglas=explicar(df), avisos=revisar_rangos(df))
    except Exception as e:
        return jsonify(error="Revisa que todos los campos sean números"), 400

if __name__ == '__main__':
    app.run(debug=True)
