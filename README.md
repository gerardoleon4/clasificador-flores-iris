# Clasificador de flores Iris

Proyecto de Machine Learning que clasifica flores Iris en una de tres especies (**setosa**, **versicolor** o **virginica**) a partir de cuatro medidas: largo y ancho del sépalo y largo y ancho del pétalo.

## La actividad

El objetivo fue recorrer el flujo completo de un proyecto de ML, desde los datos guardados en una base de datos hasta una aplicación web que cualquiera puede usar:

1. **Guardar y consultar los datos en MySQL.** El dataset Iris (150 flores, 50 por especie) está en la tabla `iris` de una base de datos MySQL. Python se conecta con SQLAlchemy.
2. **Explorar los datos.** Con consultas SQL se obtienen los rangos (mínimo y máximo) y los promedios de cada medida por especie, y con matplotlib se grafica el tamaño del sépalo de cada especie para ver cómo se separan.
3. **Entrenar y evaluar un modelo.** Los datos se dividen en 80 % para entrenamiento y 20 % para prueba, se entrena un **árbol de decisión** (`DecisionTreeClassifier`) y se mide su precisión con las flores de prueba.
4. **Guardar el modelo ("cerebro").** Se entrena el modelo final con las 150 flores y se guarda en `cerebro.joblib`, así ya no hace falta la base de datos para clasificar.
5. **Usar el modelo.** Primero desde la terminal y al final en una página web hecha con Flask.

## Archivos

| Archivo | Qué hace |
|---|---|
| `conexion.py` | Crea la conexión a la base de datos MySQL `iris_db` con los datos del archivo `.env`. |
| `analizador.py` | Exploración de los datos: rangos, promedios por especie y gráficas de dispersión del sépalo. |
| `prueba.py` | Primer modelo: divide los datos, entrena el árbol y clasifica flores escritas en la terminal. |
| `analizador_ml.py` | Igual que `prueba.py`, pero además mide la precisión del modelo con `accuracy_score`. |
| `entrenador.py` | Entrena el modelo final con todas las flores y lo guarda en `cerebro.joblib`. |
| `micerebronuevo.py` / `clasificador.py` | Cargan `cerebro.joblib` y clasifican desde la terminal, sin base de datos. |
| `app.py` | Aplicación web con Flask. |
| `templates/index.html` | Interfaz de la página web. |
| `static/` | Fotos de cada especie e `iris.json` (las 150 flores exportadas de MySQL). |

## La aplicación web

`app.py` levanta una página donde se escriben las cuatro medidas (o se elige un ejemplo) y el modelo responde la especie. Además:

- **Explica la decisión:** recorre el camino que siguió la flor dentro del árbol y lo muestra como reglas sencillas, por ejemplo "Largo del pétalo ≤ 2.45 cm".
- **Avisa si una medida es rara:** si un valor está fuera del rango de las flores con las que se entrenó, lo indica.
- **Muestra una gráfica** con la flor nueva junto a las 150 flores del dataset y la foto de la especie.
- Clasifica sin recargar la página usando la ruta `/api/predecir`.

## Cómo ejecutarlo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Aplicación web** (solo necesita `cerebro.joblib`, no la base de datos):

```bash
python app.py
```

Después abre <http://127.0.0.1:5000>.

**Scripts que leen de la base de datos** (`analizador.py`, `prueba.py`, `analizador_ml.py`, `entrenador.py`): necesitan un servidor MySQL con la base `iris_db` y la tabla `iris` (columnas `Id`, `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`, `Species`).

Los datos de acceso no están en el código: `conexion.py` los lee de un archivo `.env`, que no se sube a GitHub. Para crearlo, copia la plantilla y escribe tu usuario y contraseña:

```bash
cp .env.example .env
```

## Tecnologías

Python · pandas · scikit-learn · matplotlib · MySQL + SQLAlchemy · joblib · Flask
