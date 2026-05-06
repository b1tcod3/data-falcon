from PySide6.QtWidgets import (QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox,
                               QTableWidgetItem, QMessageBox, QToolBar, QStackedWidget)
from PySide6.QtGui import QIcon, QAction
from models.category import Category
from models.sub_category import SubCategory
from PySide6.QtCore import Qt, QSize
from category.add_category_dialog import AddCategoryDialog
from category.add_sub_category_dialog import AddSubCategoryDialog

class CategoryManagement(QMainWindow):
    def __init__(self):
        """Inicializa la aplicación de gestión de almacén."""
        super().__init__()
        self.category = Category()
        self.sub_category = SubCategory()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Categorias')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('assets/icons/category-icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create widgets and layout here
        self.create_tables()
        self.create_actions()
        self.show_categories()
        self.create_toolbar()
        self.create_menu()
        
    def create_tables(self):
        
        self.table_category = QTableWidget(self)
        self.table_category.setColumnCount(3)
        labels = ['ID',  'Nombre','Description']
        self.table_category.setHorizontalHeaderLabels(labels)
        self.table_category.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_category.itemSelectionChanged.connect(self.update_state_actions_category)
        
        # Create a table to display subproducts
        self.table_sub_category = QTableWidget(self)
        self.table_sub_category.setColumnCount(4)
        labels = ['ID',  'Nombre','Categoria','Description']
        self.table_sub_category.setHorizontalHeaderLabels(labels)
        self.table_sub_category.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_sub_category.itemSelectionChanged.connect(self.update_state_actions_sub_category)
        
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.table_category)
        self.stacked_widget.addWidget(self.table_sub_category)
        self.setCentralWidget(self.stacked_widget)
    
    def load_categories(self):
        # Load data from the database
        self.table_category.setRowCount(0)
        try:
            self.categories = self.category.get_categories(True)
            for category in self.categories:
                row_position = self.table_category.rowCount()
                self.table_category.insertRow(row_position)
                self.table_category.setItem(row_position, 0, QTableWidgetItem(str(category['id'])))
                self.table_category.setItem(row_position, 1, QTableWidgetItem(category['name']))
                self.table_category.setItem(row_position, 2, QTableWidgetItem(category['description']))
            self.table_category.resizeColumnsToContents()
            self.table_category.resizeRowsToContents()
            self.table_sub_category.clearSelection()
        except Exception as e:
            print(f"Error loading categoria: {e}")    
    
    def get_selected_category(self):
        # Get the selected category from the table
        selected_items = self.table_category.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            return self.categories[selected_row]
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione una categoria")
            return None
    
    def get_selected_sub_category(self):
        # Get the selected category from the table
        selected_items = self.table_sub_category.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            return self.sub_categories[selected_row]
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione una sub categoria")
            return None
        
    def load_sub_categories(self,category_id=None):
        # Load data from the database
        self.table_sub_category.setRowCount(0)
        try:
            self.sub_categories = self.sub_category.get_sub_categories(True,category_id)
            for sub_category in self.sub_categories:
                row_position = self.table_sub_category.rowCount()
                self.table_sub_category.insertRow(row_position)
                self.table_sub_category.setItem(row_position, 0, QTableWidgetItem(str(sub_category['id'])))
                self.table_sub_category.setItem(row_position, 1, QTableWidgetItem(sub_category['name']))
                self.table_sub_category.setItem(row_position, 2, QTableWidgetItem(sub_category['category']))
                self.table_sub_category.setItem(row_position, 3, QTableWidgetItem(sub_category['description']))
            self.table_sub_category.resizeColumnsToContents()
            self.table_sub_category.resizeRowsToContents()
            self.table_category.clearSelection()
        except Exception as e:
            print(f"Error loading sub_categories: {e}")        
    def create_actions(self):
        # Create actions for menu items
        # Action agregar producto   
        
        self.show_action_category = QAction("Mostrar Categoria", self)
        self.show_action_category.setToolTip("Mostrar Categoria")
        self.show_action_category.triggered.connect(self.show_categories)
        
        self.add_action_category = QAction(QIcon("assets/icons/add.png"), "Agregar Categoria", self)
        self.add_action_category.setToolTip("Agregar nueva categoria")
        self.add_action_category.triggered.connect(self.add_category)
        
        self.edit_action_category = QAction(QIcon("assets/icons/edit.png"), "Editar", self)
        self.edit_action_category.setToolTip("Editar producto al inventario")
        self.edit_action_category.triggered.connect(self.edit_category)                
        
        self.delete_action_category = QAction(QIcon("assets/icons/remove.png"), "Eliminar", self)
        self.delete_action_category.setToolTip("Eliminar producto al inventario")
        self.delete_action_category.triggered.connect(self.delete_category)
        
        self.show_action_sub_category_by_category = QAction(QIcon("assets/icons/relations.png"), "Ver Subcategorias Asociadas", self)
        self.show_action_sub_category_by_category.setToolTip("Ver Subcategorias Asociadas")
        self.show_action_sub_category_by_category.triggered.connect(self.show_sub_category_by_category)
        
        self.edit_action_category.setEnabled(False)
        self.delete_action_category.setEnabled(False)
        self.show_action_sub_category_by_category.setEnabled(False)
        
        # actions sub category
        self.show_action_sub_category = QAction("Mostrar Sub Categoria", self)
        self.show_action_sub_category.setToolTip("Mostrar Sub Categoria")
        self.show_action_sub_category.triggered.connect(self.show_sub_categories)
        
        self.add_sub_category_action = QAction(QIcon("assets/icons/add-2.png"), "Agregar Sub Categoria", self)
        self.add_sub_category_action.setToolTip("Agregar nueva categoria")
        self.add_sub_category_action.triggered.connect(self.add_sub_category)
        
        self.edit_action_sub_category = QAction(QIcon("assets/icons/edit.png"), "Editar", self)
        self.edit_action_sub_category.setToolTip("Editar producto al inventario")
        self.edit_action_sub_category.triggered.connect(self.edit_sub_category)                
    
    def update_state_actions_category(self):
        # Enable or disable actions based on the current state
        
        have_selection = len(self.table_category.selectedItems()) > 0
        
        self.edit_action_category.setEnabled(have_selection)
        self.delete_action_category.setEnabled(have_selection)
        self.show_action_sub_category_by_category.setEnabled(have_selection)
    
    def update_state_actions_sub_category(self):
        # Enable or disable actions based on the current state
        
        have_selection = len(self.table_sub_category.selectedItems()) > 0
        
        self.edit_action_sub_category.setEnabled(have_selection)
    
    def show_categories(self):
        # Show the category table
        self.stacked_widget.setCurrentIndex(0)
        self.load_categories()
        self.update_state_actions_category()
        
    def show_sub_categories(self,category_id=None):
        # Show the subcategory table
        self.stacked_widget.setCurrentIndex(1)
        self.load_sub_categories(category_id)
        self.update_state_actions_sub_category()
    
    def create_toolbar(self):
        # Create a toolbar for quick access to actions
        toolbar = QToolBar('Barra de Herramienta Principal')
        
        toolbar.setIconSize(QSize(32, 32))
        # agregar acción
        toolbar.addAction(self.show_action_category)
        toolbar.addAction(self.add_action_category)
        toolbar.addAction(self.edit_action_category)
        toolbar.addAction(self.delete_action_category)
        toolbar.addAction(self.show_action_sub_category_by_category)
        
        toolbar.addSeparator()
        # actions sub category
        toolbar.addAction(self.show_action_sub_category)
        toolbar.addAction(self.add_sub_category_action)

        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # Add more actions to the toolbar as needed
    
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('Archivo')
        file_menu.addSeparator()
        file_menu.addAction("Salir", self.close)
        
        # menu category
        category_menu = menu.addMenu('Categoria')
        category_menu.addAction(self.show_action_category)
        category_menu.addAction(self.add_action_category)
        category_menu.addAction(self.edit_action_category)
        category_menu.addAction(self.delete_action_category)
        
        # menu sub category
        sub_category_menu = menu.addMenu('Sub Categoria')
        sub_category_menu.addAction(self.show_action_sub_category)
        sub_category_menu.addAction(self.add_sub_category_action)
        sub_category_menu.addAction(self.add_action_category)

    def add_category(self):
        # Logic to add a new product
        dialog = AddCategoryDialog(self)
        try:
            if dialog.exec():
                new_category = dialog.get_values()
                self.category.add_category(new_category['name'],
                                          new_category['description'],
                                          )
                # Show success message
                self.statusBar().showMessage("Categoria Agregado con Èxito",3000)
                self.load_categories()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
    def add_sub_category(self):
        # Logic to add a new product
        dialog = AddSubCategoryDialog(self)
        try:
            if dialog.exec():
                new_sub_category = dialog.get_values()
                self.sub_category.add_sub_category(new_sub_category['name'],
                                          new_sub_category['description'],
                                          new_sub_category['category_id']
                                          )
                # Show success message
                self.statusBar().showMessage("Sub Categoria Agregado con Èxito",3000)
                self.load_sub_categories()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
            
    def edit_category(self):
        
        #get category selected
        category = self.get_selected_category()
        if not category:
            return
        
        # Logic to add a new product
        dialog = AddCategoryDialog(self)
        dialog.setWindowTitle("Editar Producto")
        dialog.setWindowIcon(QIcon('assets/icons/edit.png'))
        dialog.set_values(category)
        try:
            if dialog.exec():
                new_category = dialog.get_values()
                self.category.update_category(category['id'],
                                          new_category['name'],
                                          new_category['description'],
                                          )
                # Show success message
                self.statusBar().showMessage("Categoria Editado con Èxito",3000)
                self.load_categories()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
        
    def edit_sub_category(self):
        #get category selected
        sub_category = self.get_selected_sub_category()
        if not sub_category:
            return
        
        # Logic to add a new product
        dialog = AddSubCategoryDialog(self)
        dialog.setWindowTitle("Editar Producto")
        dialog.setWindowIcon(QIcon('assets/icons/edit.png'))
        sub_category = self.sub_category.find_sub_category(sub_category[0])
        dialog.set_values(sub_category)
        try:
            if dialog.exec():
                new_sub_category = dialog.get_values()
                self.sub_category.update_sub_category(sub_category[0],
                                          new_sub_category['name'],
                                          new_sub_category['description'],
                                          new_sub_category['category_id']
                                          )
                # Show success message
                self.statusBar().showMessage("Sub Categoria Editado con Èxito",3000)
                self.load_sub_categories()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Error al agregar: {str(e)}")
    
    def delete_category(self):
        # Logic to delete a product
        
        category = self.get_selected_category()
        if not category:
            return
        
        confirm = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            "¿Eliminar la Categoria seleccionada?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            try:
                self.category.delete_category(category['id'])
                self.statusBar().showMessage("Categoria Eliminado con Èxito",3000)
                self.load_categories()
            except Exception as e:
                QMessageBox.critical(self,"Error",f"Error al eliminar: {str(e)}")
    def show_sub_category_by_category(self):
        #get category selected
        category = self.get_selected_category()
        if not category:
            return
        self.show_sub_categories(category['id'])
        
        
    