"""""
crear una clase Resultado que se encargue de la conexión a la base de datos
"""""

from connect_db import DatabaseConnection

class Resultado:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.db = DatabaseConnection('resultados.db')
        
    def get_municipios(self,dic=False):
        """Obtiene todas las categorías de la base de datos."""
        select_query = "SELECT DISTINCT MUNICIPIO FROM resultados"
        self.db.execute_query(select_query)
        if dic:
            columns = [column[0] for column in self.db.cursor.description]
            return [dict(zip(columns, row)) for row in self.db.fetch_all()]
        else:
            return self.db.fetch_all()
    def get_parroquias(self, municipio):
        """Obtiene todas las parroquias de un municipio específico."""
        select_query = "SELECT DISTINCT PARROQUIA FROM resultados WHERE MUNICIPIO = ?"
        self.db.execute_query(select_query, (municipio,))
        return self.db.fetch_all()
    def get_centros(self, municipio, parroquia):
        """Obtiene todos los centros de votación de una parroquia específica."""
        select_query = "SELECT ID, NOMBRE FROM resultados WHERE MUNICIPIO = ? AND PARROQUIA = ?"
        self.db.execute_query(select_query, (municipio, parroquia))
        return self.db.fetch_all()
    
    def get_resultados(self):
        """Obtiene los resultados electorales de un municipio y parroquia específicos."""
        select_query = """
            SELECT SUM(AN2015),SUM(REG2017),SUM(PRES2018),SUM(REG2021)
            FROM resultados
        """
        self.db.execute_query(select_query)
        return self.db.fetch_one()
    
    def get_resultados_municipio(self, municipio):
        """Obtiene los resultados electorales de un municipio específico."""
        select_query = """
            SELECT SUM(AN2015),SUM(REG2017),SUM(PRES2018),SUM(REG2021)
            FROM resultados
            WHERE MUNICIPIO = ?
        """
        self.db.execute_query(select_query, (municipio,))
        return self.db.fetch_one()

    def get_resultados_parroquia(self, municipio, parroquia):
        """Obtiene los resultados electorales de una parroquia específica."""
        select_query = """
            SELECT SUM(AN2015),SUM(REG2017),SUM(PRES2018),SUM(REG2021)
            FROM resultados
            WHERE MUNICIPIO = ? AND PARROQUIA = ?
        """
        self.db.execute_query(select_query, (municipio, parroquia))
        return self.db.fetch_one()

    def get_resultados_centro(self,centro):
        """Obtiene los resultados electorales de un centro específico."""
        select_query = """
            SELECT AN2015,REG2017,PRES2018,REG2021
            FROM resultados
            WHERE ID = ?
        """
        self.db.execute_query(select_query, (centro,))
        return self.db.fetch_one()
resultado = Resultado()
print(resultado.get_resultados())