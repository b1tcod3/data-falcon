"""""
Modelo de categoria de productos
NAME: UNIQUE
CATEGORY_ID: 
DESCRIPTION: Modelo de categoria de productos
"""""

from models.connect_db import DatabaseConnection

class SubCategory:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('almacen.db')
        
    def get_sub_categories(self,dic=False,category_id=None):
        """Obtiene todos las subcategories, combinadas con categoria de la base de datos."""
        if category_id:
            select_query = """
            SELECT sub_categories.id, sub_categories.name, sub_categories.description, 
                categories.name as category FROM sub_categories 
                INNER JOIN categories ON sub_categories.category_id = categories.id
                WHERE sub_categories.category_id = ?
            """
            self.db.execute_query(select_query, (category_id,))
        else:
            select_query = """
            SELECT sub_categories.id, sub_categories.name, sub_categories.description, 
                categories.name as category FROM sub_categories 
                INNER JOIN categories ON sub_categories.category_id = categories.id
                
            """
            self.db.execute_query(select_query)
        if dic:
            columns = [column[0] for column in self.db.cursor.description]
            return [dict(zip(columns, row)) for row in self.db.fetch_all()]
        else:
            return self.db.fetch_all()
    def add_sub_category(self, name, description, category_id):
        """Agrega una nueva subcategoria a la base de datos."""
        insert_query = """
        INSERT INTO sub_categories (name, description, category_id)
        VALUES (?, ?, ?);
        """
        self.db.execute_query(insert_query, (name, description, category_id))
