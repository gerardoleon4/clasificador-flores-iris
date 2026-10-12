import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
#lee los datos de acceso del archivo .env (no se sube a GitHub)
load_dotenv()
def obtener_conexion():
    usuario=os.getenv('IRIS_DB_USER')
    contrasenia=os.getenv('IRIS_DB_PASSWORD')
    host=os.getenv('IRIS_DB_HOST','localhost')
    base_de_datos=os.getenv('IRIS_DB_NAME','iris_db')
    conexion=create_engine(f'mysql+mysqlconnector://{usuario}:{contrasenia}@{host}/{base_de_datos}')
    return conexion
