"""""
crear consultas generales
"""""

from models.connect_db import DatabaseConnection

class Almacen:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('almacen.db')
    def exists(self, table, column, value, exclude_id=None):
        """Verifica si un valor existe en una columna de una tabla."""
        query = f"SELECT * FROM {table} WHERE {column} = ?"
        params = [value]
        if exclude_id:
            query += f" AND id != ?"
            params.append(exclude_id)
        self.db.execute_query(query, params)
        return self.db.fetch_one() is not None        
    
        
