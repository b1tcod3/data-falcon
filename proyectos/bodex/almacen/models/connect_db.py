import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        """Inicializa la conexión a la base de datos."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_all_tables()

    def close(self):
        self.cursor.close()
        self.connection.close()
    def create_all_tables(self):
        """Crea todas las tablas necesarias en la base de datos."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL
            );
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS sub_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
                );
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS suppliers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    code TEXT NOT NULL UNIQUE,
                    address TEXT NOT NULL UNIQUE,
                    type TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    image TEXT NOT NULL
                );
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            barcode TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            description TEXT NOT NULL,                    
            unit TEXT NOT NULL,
            quantity REAL NOT NULL,            
            price_usd REAL NOT NULL,
            image TEXT NOT NULL,
            subcategory_id INTEGER,
            supplier_id INTEGER,
            
            FOREIGN KEY (subcategory_id) REFERENCES subcategorias(id),
            FOREIGN KEY (supplier_id) REFERENCES proveedores(id)
        );
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            self.connection.rollback()

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
    
