import pandas as pd
from sqlalchemy import create_engine

# conexión a postgre
DB_USER = "ds_user"
DB_PASS = "Didi.871."
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ds_project_db"

connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# --- 2. Carga por Chunks ---
# Define la consulta que trae los datos ya pre-procesados
query = "SELECT fecha_transaccion, monto, producto, cantidad FROM ventas ORDER BY fecha_transaccion;"

# Lista para almacenar resultados procesados o agregados de cada chunk
all_processed_data = []
chunk_size = 50000 # Define el tamaño de cada bloque (ej. 50,000 filas)

print(f"Iniciando la carga y procesamiento por bloques de {chunk_size} filas...")

# El argumento iterator=True habilita el chunking
for chunk in pd.read_sql(query, engine, chunksize=chunk_size):

    # 3. PROCESAMIENTO DENTRO DEL BLOQUE
    # (Aquí va tu código de limpieza, feature engineering o agregación)

    # Ejemplo: Crear una nueva feature de precio unitario
    chunk['precio_unitario'] = chunk['monto'] / chunk['cantidad']

    # Añade el chunk procesado a la lista (o guárdalo en un archivo intermedio)
    all_processed_data.append(chunk)

    # Para monitoreo:
    print(f"Bloque procesado. Filas totales recopiladas: {sum(len(df) for df in all_processed_data)}")

# --- 4. CONSOLIDACIÓN FINAL ---
# Combina todos los chunks en un único DataFrame final para el modelado
final_df = pd.concat(all_processed_data)

print(f"\nProceso finalizado. DataFrame listo para el modelado con {len(final_df)} filas.")

# Guarda el DataFrame final en un archivo CSV
final_df.to_csv("code/sql/postgre/basico/ventas_procesadas_final.csv", index=False)
