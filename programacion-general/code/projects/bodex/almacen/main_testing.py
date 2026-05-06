from PySide6.QtWidgets import QMainWindow

class Testing(QMainWindow):
    def __init__(self):
        """Inicializa la aplicación de gestión de almacén."""
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Categorias')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")