import pandas as pd
from sqlalchemy import create_engine

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

# Asumamos que 'final_df' contiene los datos originales + la nueva columna de predicción
# Simulación de la nueva columna de predicción:

final_df = pd.read_csv('code/sql/postgre/basico/ventas_procesadas_final.csv')

# Simulación de la nueva columna de predicción 5 predicciones:
final_df['prediccion_ventas'] = [155.00, 26.50, 505.00, 234, 345]  # Ejemplo de predicciones

# Reutilizar la conexión engine
# connection_string = "..."
# engine = create_engine(connection_string) 

# --- Persistencia a Postgre ---
# Guardamos el DataFrame de predicciones en una nueva tabla
final_df.to_sql(
    name='predicciones_modelo',
    con=engine,
    if_exists='replace', # Creamos una tabla nueva (si existe, la sobrescribe)
    index=False
)

print("\nPredicciones del modelo guardadas exitosamente en la tabla 'predicciones_modelo'.")
