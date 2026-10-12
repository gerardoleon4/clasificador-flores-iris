import pandas as pd
import joblib
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from conexion import obtener_conexion

conexion=obtener_conexion()
query="SELECT * FROM iris"
df_iris=pd.read_sql(query,conexion)
#SEPARAR VARIABLES "X","y"
X=df_iris.drop(columns=['Id','Species'])
y=df_iris['Species']

print("ENTRENANDO EL MODELO FINAL")
modelo_produccion=DecisionTreeClassifier(random_state=42)
modelo_produccion.fit(X,y)
joblib.dump(modelo_produccion,Path(__file__).parent.parent/'modelo'/'cerebro.joblib')
print("CEREBRO CREADO CON ÉXITO")
