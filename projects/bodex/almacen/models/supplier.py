"""""
Modelo de gestión de proveedores
"""""

from models.connect_db import DatabaseConnection

class Supplier:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('almacen.db')
    def get_suppliers(self,dic=False):
        """Obtiene todos los proveedores de la base de datos."""
        select_query = "SELECT * FROM suppliers"
        self.db.execute_query(select_query)
        if dic:
            columns = [column[0] for column in self.db.cursor.description]
            return [dict(zip(columns, row)) for row in self.db.fetch_all()]
        else:
            return self.db.fetch_all()
    def add_supplier(self, name, code, type, phone, address, email,image=''):
        """Agrega un nuevo proveedor a la base de datos."""
        insert_query = """
            INSERT INTO suppliers (name, code, type, phone, address, email,image)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_query(insert_query, (name, code, type, phone, address, email,image))
        
        