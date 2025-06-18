"""""
Modelo de producto para la gestión de productos en la base de datos.
NAME:
CODE: codigo interno-SKU
BARCODE: codigo de barra
DESCRIPTION:
SUBCATEGORY: en esta esta inmersa la categoria
SUPPLIER:
IMAGE:
UNIT: como es empaquetada el producto: unidad, caja, bolsa, paquete, kilogramo, litros, metros, gramos, toneladas, pulgadas
QUANTITY:
PRICE_USD:
"""""

from models.connect_db import DatabaseConnection

class Producto:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('almacen.db')
    def get_productos(self):
        """Obtiene todos los productos de la base de datos."""
        select_query = "SELECT * FROM productos"
        self.db.execute_query(select_query)
        return self.db.fetch_all()
    
    def find_product(self, id):
        """Busca un producto por su ID. retornando un diccionario con los datos del producto"""
        select_query = "SELECT * FROM productos WHERE id = ?"
        self.db.execute_query(select_query, (id,))
        result = self.db.fetch_one()
        if result:
            return {
                'id': result[0],
                'name': result[1],
                'code': result[2],
                'barcode': result[3],
                'description': result[4],
                'quantity': result[5],
                'category': result[6],
                'subcategory': result[7],
                'supplier': result[8],
                'unit': result[9],
                'price_usd': result[6],
                'image': result[10]
                
            }
        return None
    
    def add_producto(self, name, description, quantity, precio, precio_usd, categoria, subcategoria, proveedor, imagen):
        """Agrega un nuevo producto a la base de datos."""
        insert_query = """
        INSERT INTO productos
        """
        self.db.execute_query(insert_query, (nombre, description, cantidad, precio, precio_usd, categoria, subcategoria, proveedor, imagen))
    
    def update_producto(self, id, nombre, cantidad, precio, precio_usd, categoria, subcategoria, proveedor, imagen):
        """Actualiza un producto existente en la base de datos."""
        update_query = """
        UPDATE productos
        SET nombre = ?, cantidad = ?, precio = ?, precio_usd = ?, categoria = ?, subcategoria = ?, proveedor = ?, imagen = ?
        WHERE id = ?
        """
        self.db.execute_query(update_query, (nombre, cantidad, precio, precio_usd, categoria, subcategoria, proveedor, imagen, id))    
     
    def delete_producto(self, id):
        """Elimina un producto de la base de datos."""
        delete_query = "DELETE FROM productos WHERE id = ?"
        self.db.execute_query(delete_query, (id,))
    
    def add_amount(self, id, amount):
        """Aumenta la cantidad de un producto en la base de datos."""
        update_query = "UPDATE productos SET cantidad = cantidad + ? WHERE id = ?"
        self.db.execute_query(update_query, (amount, id))
    
    def subtract_amount(self, id, amount):
        """Disminuye la cantidad de un producto en la base de datos."""
        update_query = "UPDATE productos SET cantidad = cantidad - ? WHERE id = ?"
        self.db.execute_query(update_query, (amount, id))
    
    def filter_productos(self, **kwargs):
        """Filtra los productos según los criterios dados."""
        query = "SELECT * FROM productos WHERE "
        conditions = []
        params = []
        
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            params.append(value)
        
        query += " AND ".join(conditions)
        self.db.execute_query(query, tuple(params))
        return self.db.fetch_all()
    def find_product(self, id):
        """Busca un producto por su ID. retornando un diccionario con los datos del producto"""
        select_query = "SELECT * FROM productos WHERE id = ?"
        self.db.execute_query(select_query, (id,))
        result = self.db.fetch_one()
        if result:
            return {
                'id': result[0],
                'nombre': result[1],
                'description': result[2],
                'cantidad': result[3],
                'precio': result[4],
                'precio_usd': result[5],
                'categoria': result[6],
                'subcategoria': result[7],
                'proveedor': result[8],
                'imagen': result[9]
            }
        return None
        
        