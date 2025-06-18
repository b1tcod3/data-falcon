from PySide6.QtWidgets import (QMainWindow, QTableWidget,
                               QTableWidgetItem, QMessageBox, QToolBar)
from PySide6.QtGui import QIcon, QAction
from models.product import Producto
from PySide6.QtCore import Qt, QSize
from product.add_product_dialog import AddProductDialog

class StockManagement(QMainWindow):
    def __init__(self):
        """Inicializa la aplicación de gestión de almacén."""
        super().__init__()
        self.producto = Producto()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Almacén')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create widgets and layout here
        self.create_table()
        self.load_products()
        self.create_actions()
        self.create_toolbar()
        self.create_menu()
        
    def create_actions(self):
        # Create actions for menu items
        # Action agregar producto   
        self.add_action = QAction(QIcon("assets/icons/add.png"), "Agregar", self)
        self.add_action.setToolTip("Agregar nuevo producto al inventario")
        self.add_action.triggered.connect(self.add_product)
        
        self.edit_action = QAction(QIcon("assets/icons/edit.png"), "Editar", self)
        self.edit_action.setToolTip("Editar producto al inventario")
        self.edit_action.triggered.connect(self.edit_product)                
        
        self.edit_action.setEnabled(False)
    
    def update_state_actions(self):
        # Enable or disable actions based on the current state
        
        have_selection = len(self.table.selectedItems()) > 0
        
        self.edit_action.setEnabled(have_selection)
        
    def create_toolbar(self):
        # Create a toolbar for quick access to actions
        toolbar = QToolBar('Barra de Herramienta Principal')
        toolbar.setIconSize(QSize(32, 32))
        # agregar acción
        toolbar.addAction(self.add_action)
        toolbar.addAction(self.edit_action)

        
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # Add more actions to the toolbar as needed
        
    def create_table(self):
        # Create a table to display products
        self.table = QTableWidget(self)
        self.table.setColumnCount(8)
        labels = ['ID', 'Nombre', 'Cantidad', 'Precio', 'Precio USD', 'Categoría', 'Subcategoría', 'Proveedor']
        self.table.setHorizontalHeaderLabels(labels)
        self.table.setGeometry(50, 50, 700, 400)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.itemSelectionChanged.connect(self.update_state_actions)
        self.setCentralWidget(self.table)

    def load_products(self):
        # Load data from the database
        self.table.setRowCount(0)
        try:
            self.products = self.producto.get_productos()
            for product in self.products:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for column, data in enumerate(product):
                    self.table.setItem(row_position, column, QTableWidgetItem(str(data)))
        except Exception as e:
            print(f"Error loading products: {e}")
    
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('Archivo')
        file_menu.addSeparator()
        file_menu.addAction("Salir", self.close)
        
        # menu invetario
        inventory_menu = menu.addMenu('Inventario')
        inventory_menu.addAction(self.add_action)
        inventory_menu.addAction(self.edit_action)

    def add_product(self):
        # Logic to add a new product
        dialog = AddProductDialog(self)
        try:
            if dialog.exec():
                new_producto = dialog.get_values()
                self.producto.add_producto(new_producto['nombre'],
                                          new_producto['descripcion'],
                                          0,
                                          80*new_producto['precio_usd'],
                                          new_producto['precio_usd'],
                                          new_producto['categoria'],
                                          new_producto['sub_categoria'],
                                          new_producto['proveedor'],
                                          "/")
                # Show success message
                self.statusBar().showMessage("Producto Agregado con Èxito",3000)
                self.load_products()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
    def edit_product(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto")
            return None
        product = self.products[self.table.row(selected[0])]
        
        # Logic to add a new product
        dialog = AddProductDialog(self)
        dialog.setWindowTitle("Editar Producto")
        dialog.setWindowIcon(QIcon('assets/icons/edit.png'))
        dialog.name_input.setText(product[1])
        product = self.producto.find_product(product[0])
        print(product)
        try:
            if dialog.exec():
                new_producto = dialog.get_values()
                self.producto.add_producto(new_producto['nombre'],
                                          new_producto['descripcion'],
                                          0,
                                          80*new_producto['precio_usd'],
                                          new_producto['precio_usd'],
                                          new_producto['categoria'],
                                          new_producto['sub_categoria'],
                                          new_producto['proveedor'],
                                          "/")
                # Show success message
                self.statusBar().showMessage("Producto Agregado con Èxito",3000)
                self.load_products()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")