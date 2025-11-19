from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                               QComboBox,QDialogButtonBox, QFormLayout, 
                               QApplication)
from lib.validator import FormValidator, Validator
from PySide6.QtGui import QIcon

class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        """Inicializa el diálogo para agregar un nuevo producto."""
        super().__init__(parent)
        self.setWindowTitle('Agregar Producto')
        self.setGeometry(100, 100, 400, 300)
        # self.setModal(True)
        # mover el diálogo un poco abajo de la pantalla
        self.move(200, 200)
        
        
        # Icono y estilo
        self.setWindowIcon(QIcon('assets/icons/add.png'))
        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        # Labels and inputs
        self.name_label = QLabel('Nombre:')
        self.name_input = QLineEdit(self)
        
        self.description_label = QLabel('Description:')
        self.description_input = QLineEdit(self)
        
        self.price_usd_label = QLabel('Precio USD:')
        self.price_usd_input = QLineEdit(self)
        
        self.categoria_label = QLabel('Categoría:')
        self.categoria_input = QComboBox(self)
        
        self.sub_categoria_label = QLabel('Sub Categoría:')
        self.sub_categoria_input = QComboBox(self)
        
        # Add categories to the combo box
        categories = ['Electrónica', 'Ropa', 'Alimentos']
        self.categoria_input.addItems(categories)
        sub_categories = ['Electrónica', 'Ropa', 'Alimentos']
        self.sub_categoria_input.addItems(sub_categories)
        
        self.proveedor_label = QLabel('Proveedor:')
        self.proveedor_input = QLineEdit(self)
        
        # Buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
        
        # Add widgets to layout
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.description_label, self.description_input)
        form_layout.addRow(self.price_usd_label, self.price_usd_input)
        form_layout.addRow(self.categoria_label, self.categoria_input)
        form_layout.addRow(self.sub_categoria_label, self.sub_categoria_input)
        form_layout.addRow(self.proveedor_label, self.proveedor_input)
        
        layout.addLayout(form_layout)
        layout.addWidget(self.buttons)
        
        self.setLayout(layout)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        self.validator = FormValidator()
        self._configure_validators()
        self._conexion_signals()
        
    def _configure_validators(self):
        """Configura los validadores para los campos del formulario."""
        self.validator.add_field_validation('name', {
            'required': True,
            'min_length': 3,
            'max_length': 100,
            'validator': Validator.validate_name()
        })
        
        self.validator.add_field_validation('description', {
            'required': True,
            'min_length': 3,
            'max_length': 100,
            'validator': Validator.validate_description()
        })
        
        self.validator.add_field_validation('price_usd', {
            'required': True,
            'validator': Validator.validate_price()
        })
        
        self.validator.add_field_validation('categoria', {
            'required': True
        })
        
        self.validator.add_field_validation('sub_categoria', {
            'required': True
        })
        
        self.validator.add_field_validation('proveedor', {
            'required': True,
            'min_length': 3,
            'max_length': 100,
            'validator': Validator.validate_name()
        })
        
    def _conexion_signals(self):
        """Conecta las señales de los campos de entrada a los validadores."""
        self.name_input.textChanged.connect(self.validate_form)
        self.description_input.textChanged.connect(self.validate_form)
        self.price_usd_input.textChanged.connect(self.validate_form)
        self.categoria_input.currentTextChanged.connect(self.validate_form)
        self.sub_categoria_input.currentTextChanged.connect(self.validate_form)
        self.proveedor_input.textChanged.connect(self.validate_form)
    
    def validate_form(self):
        """Valida el formulario completo."""
        form_data = {
            'name': self.name_input.text(),
            'description': self.description_input.text(),
            'price_usd': self.price_usd_input.text(),
            'categoria': self.categoria_input.currentText(),
            'sub_categoria': self.sub_categoria_input.currentText(),
            'proveedor': self.proveedor_input.text()
        }
        
        self.validator.validate_form(form_data)
        self._update_styles()
        self._update_boton_ok()
    
    def _update_styles(self):
        """Actualiza los estilos de los campos según la validación."""
        for field_name, rules in self.validator.field_validations.items():
            field = getattr(self, f"{field_name}_input")
            if field_name in self.validator.errors:
                field.setStyleSheet("border: 1px solid red;")
            else:
                field.setStyleSheet("border: 1px solid green;")
    
    def _update_boton_ok(self):
        """Actualiza el estado del botón OK según la validación."""
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(not bool(self.validator.errors))
        #self.buttons.accepted.setEnabled(not bool(self.validator.errors))
    
    def get_values(self):
        """Devuelve los valores del formulario."""
        return {
            'nombre': self.name_input.text(),
            'descripcion': self.description_input.text(),
            'precio_usd': float(self.price_usd_input.text()),
            'categoria': self.categoria_input.currentText(),
            'sub_categoria': self.sub_categoria_input.currentText(),
            'proveedor': self.proveedor_input.text()
        }
