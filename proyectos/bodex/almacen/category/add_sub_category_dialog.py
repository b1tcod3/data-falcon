from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                               QComboBox,QDialogButtonBox, QFormLayout, 
                               QApplication)
from lib.validator import FormValidator, Validator
from PySide6.QtGui import QIcon
from models.category import Category

class AddSubCategoryDialog(QDialog):
    def __init__(self, parent=None):
        """Inicializa el diálogo para agregar un nueva sub categoria."""
        super().__init__(parent)
        self.setWindowTitle('Agregar Sub Categoria')
        self.setGeometry(100, 100, 400, 300)
        # self.setModal(True)
        # mover el diálogo un poco abajo de la pantalla
        self.move(200, 200)
        self.category = Category()
        
        
        # Icono y estilo
        self.setWindowIcon(QIcon('assets/icons/add-2.png'))
        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        # Labels and inputs
        self.name_label = QLabel('Nombre:')
        self.name_input = QLineEdit(self)
        
        self.description_label = QLabel('Description:')
        self.description_input = QLineEdit(self)
        
        self.combo_category_label = QLabel('Categoria:')
        self.category_id_input = QComboBox(self)
        self.category_id_input.addItem("Seleccione ...",None)
        
        # Cargar categorias desde la base de datos
        categories = self.category.get_categories()
        for category in categories:
            self.category_id_input.addItem(category[1], category[0])
        self.category_id_input.setStyleSheet("background-color: #ffffff;")
        
        # Buttons
        
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
        
        # Add widgets to layout
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.description_label, self.description_input)
        form_layout.addRow(self.combo_category_label, self.category_id_input)
        
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
            'max_length': 20,
            'validator': Validator.validate_string(),
            'unique': {
                'table': 'categories',
            }
        })
        
        self.validator.add_field_validation('description', {
            'required': True,
            'min_length': 3,
            'max_length': 100,
            'validator': Validator.validate_text()
        })
        
        self.validator.add_field_validation('category_id', {
            'required': True,
        })
        
    def _conexion_signals(self):
        """Conecta las señales de los campos de entrada a los validadores."""
        self.name_input.textChanged.connect(self.validate_form)
        self.description_input.textChanged.connect(self.validate_form)
        self.category_id_input.currentIndexChanged.connect(self.validate_form)
        
    def validate_form(self):
        """Valida el formulario completo."""
        form_data = {
            'name': self.name_input.text(),
            'description': self.description_input.text(),
            'category_id': self.category_id_input.currentData(),
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
    
    def get_values(self):
        """Devuelve los valores del formulario."""
        return {
            'name': self.name_input.text(),
            'description': self.description_input.text(),
            'category_id': self.category_id_input.currentData(),
        }
