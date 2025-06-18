"""""
Módulo para la gestión de categorías en la base de datos.
"""""

from models.connect_db import DatabaseConnection

class Category:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('almacen.db')
        
    def add_category(self, name, description):
        """Agrega una nueva categoría a la base de datos."""
        insert_query = """
        INSERT INTO categories (name, description)
        VALUES (?, ?);
        """
        self.db.execute_query(insert_query, (name, description))    
    def get_categories(self,dic=False):
        """Obtiene todas las categorías de la base de datos."""
        select_query = "SELECT * FROM categories"
        self.db.execute_query(select_query)
        if dic:
            columns = [column[0] for column in self.db.cursor.description]
            return [dict(zip(columns, row)) for row in self.db.fetch_all()]
        else:
            return self.db.fetch_all()
    def find_category(self, category_id):
        """Busca una categoría por su ID y retornar un diccionario."""
        select_query = "SELECT * FROM categories WHERE id = ?"
        self.db.execute_query(select_query, (category_id,))
        columns = [column[0] for column in self.db.cursor.description]
        row = self.db.fetch_one()
        if row:
            return dict(zip(columns, row))
        else:
            return None
    def update_category(self, category_id, name, description):
        """Actualiza una categoría existente en la base de datos."""
        update_query = """
        UPDATE categories
        SET name = ?, description = ?
        WHERE id = ?;
        """
        self.db.execute_query(update_query, (name, description, category_id))
    
    def delete_category(self, category_id):
        """Elimina una categoría de la base de datos."""
        delete_query = "DELETE FROM categories WHERE id = ?"
        self.db.execute_query(delete_query, (category_id,))
        # Eliminar productos asociados a la categoría
        