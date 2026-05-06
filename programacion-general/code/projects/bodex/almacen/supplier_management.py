from PySide6.QtWidgets import (QMainWindow, QTableWidget,
                               QTableWidgetItem, QMessageBox, QToolBar)
from PySide6.QtGui import QIcon, QAction
from models.supplier import Supplier
from PySide6.QtCore import Qt, QSize
from supplier.add_supplier_dialog import AddSupplierDialog

class SupplierManagement(QMainWindow):
    def __init__(self):
        """Inicializa la aplicación de gestión de almacén."""
        super().__init__()
        self.supplier = Supplier()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Proveedores')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('assets/icons/icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create widgets and layout here
        self.create_table()
        self.load_suppliers()
        self.create_actions()
        self.create_toolbar()
        self.create_menu()
    
    def create_table(self):
        # Create a table to display products
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        labels = ['ID', 'Nombre','Código','Tipo','Télefono','Dirección','Email']
        self.table.setHorizontalHeaderLabels(labels)
        self.table.setGeometry(50, 50, 700, 400)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.itemSelectionChanged.connect(self.update_state_actions)
        self.setCentralWidget(self.table)

    def load_suppliers(self):
        # Load data from the database
        self.table.setRowCount(0)
        try:
            self.suppliers = self.supplier.get_suppliers(True)
            for supplier in self.suppliers:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(str(supplier['id'])))
                self.table.setItem(row_position, 1, QTableWidgetItem(supplier['name']))
                self.table.setItem(row_position, 2, QTableWidgetItem(supplier['code']))
                self.table.setItem(row_position, 3, QTableWidgetItem(supplier['type']))
                self.table.setItem(row_position, 4, QTableWidgetItem(supplier['phone']))
                self.table.setItem(row_position, 5, QTableWidgetItem(supplier['address']))
                self.table.setItem(row_position, 6, QTableWidgetItem(supplier['email']))
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()
        except Exception as e:
            print(f"Error loading products: {e}")
        
    def create_actions(self):
        # Create actions for menu items
        # Action agregar producto   
        self.add_action = QAction(QIcon("assets/icons/add.png"), "Agregar", self)
        self.add_action.setToolTip("Agregar nuevo proveedor al inventario")
        self.add_action.triggered.connect(self.add_supplier)
        
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
    
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('Archivo')
        file_menu.addSeparator()
        file_menu.addAction("Salir", self.close)
        
        # menu invetario
        inventory_menu = menu.addMenu('Inventario')
        inventory_menu.addAction(self.add_action)
        inventory_menu.addAction(self.edit_action)

    def add_supplier(self):
        # Logic to add a new product
        dialog = AddSupplierDialog(self)
        try:
            if dialog.exec():
                new_supplier = dialog.get_values()
                self.supplier.add_supplier(new_supplier['name'],
                                            new_supplier['code'],
                                            new_supplier['address'],
                                            new_supplier['type'],
                                            new_supplier['phone'],
                                            new_supplier['email'],
                                            "/")
                # Show success message
                self.statusBar().showMessage("Producto Agregado con Èxito",3000)
                self.load_products()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
    def edit_supplier(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto")
            return None
        supplier = self.suppliers[self.table.row(selected[0])]
        
        # Logic to add a new product
        dialog = AddSupplierDialog(self)
        dialog.setWindowTitle("Editar Proveedor ")
        dialog.setWindowIcon(QIcon('assets/icons/edit.png'))
        dialog.set_values(supplier[1], supplier[2], supplier[3], supplier[4], supplier[5], supplier[6])

        try:
            if dialog.exec():
                new_supplier = dialog.get_values()
                self.producto.add_producto(new_supplier['nombre'],
                                          new_supplier['descripcion'],
                                          0,
                                          80*new_supplier['precio_usd'],
                                          new_supplier['precio_usd'],
                                          new_supplier['categoria'],
                                          new_supplier['sub_categoria'],
                                          new_supplier['proveedor'],
                                          "/")
                # Show success message
                self.statusBar().showMessage("Producto Agregado con Èxito",3000)
                self.load_products()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")