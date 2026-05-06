import pandas as pd
from sqlalchemy import create_engine
import os

# conexión a postgre
DB_USER = "ds_user"
DB_PASS = "Didi.871."
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ds_project_db"

# La cadena debe usar 'postgresql+psycopg2'
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Ejemplo del formato: postgresql+psycopg2://ds_user:contraseña@localhost:5432/ds_project_db
engine = create_engine(connection_string)

csv_file_path =os.path.expanduser("data/ventas_ejemplo.csv")

df_ventas = pd.read_csv(csv_file_path)
# En este punto, puedes agregar pasos de limpieza:
# df_ventas['monto'] = df_ventas['monto'].fillna(0)
# print("Limpieza básica completada.")

# --- PASO 3: Ingesta a la Base de Datos ---
# Utilizamos 'ventas_pandas' para no sobrescribir la tabla 'ventas' que ya creamos
df_ventas.to_sql(
    name='ventas_pandas',
    con=engine,
    if_exists='replace', # ¿Qué hacer si la tabla ya existe? 'fail', 'replace', o 'append'
    index=False,         # No incluir el índice de Pandas como una columna
    chunksize=1000       # Opcional: Cargar en bloques de 1000 filas
)

print(f"\nDatos de {len(df_ventas)} filas cargados exitosamente en la tabla 'ventas_pandas'.")
