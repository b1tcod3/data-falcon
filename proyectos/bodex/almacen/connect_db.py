import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        """Inicializa la conexión a la base de datos."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, params=()):
        """Ejecuta una consulta SQL."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
    def fetch_all(self):
        """Recupera todos los resultados de la última consulta."""
        return self.cursor.fetchall()
    def fetch_one(self):
        """Recupera un solo resultado de la última consulta."""
        return self.cursor.fetchone()
    def execute_script(self, script):
        """Ejecuta un script SQL."""
        try:
            self.cursor.executescript(script)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error executing script: {e}")
            self.connection.rollback()
    
