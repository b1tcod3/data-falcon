from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                               QComboBox,QDialogButtonBox, QFormLayout, QPlainTextEdit)
from lib.validator import FormValidator, Validator
from PySide6.QtGui import QIcon

class AddSupplierDialog(QDialog):
    def __init__(self, parent=None):
        """Inicializa el diálogo para agregar un nueva categoria."""
        super().__init__(parent)
        self.setWindowTitle('Agregar Proveedor')
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
        
        self.code_label = QLabel('Código:')
        self.code_input = QLineEdit(self)
        
        self.type_label = QLabel('Tipo:')
        self.type_input = QComboBox(self)
        self.type_input.addItem("Seleccione ...",None)
        types = ['Privada', 'Mixta', 'Pública','Cooperativa', 'Comunal']
        self.type_input.addItems(types)
        
        self.phone_label = QLabel('Télefono:')
        self.phone_input = QLineEdit(self)
        
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit(self)
        
        self.address_label = QLabel('Dirección:')
        self.address_input = QPlainTextEdit()
        self.address_input.setPlaceholderText("Calle, número, ciudad, código postal")
        self.address_input.setMinimumHeight(80)
        self.address_input.setMaximumHeight(150)
        self.address_input.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        
        # Buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
        
        # Add widgets to layout
        form_layout.addRow(self.name_label, self.name_input)    
        form_layout.addRow(self.code_label, self.code_input)
        form_layout.addRow(self.type_label, self.type_input)
        form_layout.addRow(self.phone_label, self.phone_input)
        form_layout.addRow(self.email_label, self.email_input)
        form_layout.addRow(self.address_label, self.address_input)
        
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
            'validator': Validator.validate_string()
        })
        
        self.validator.add_field_validation('code', {
            'required': True,
            'min_length': 3,
            'max_length': 15,
            'validator': Validator.validate_string()
        })   
        
        self.validator.add_field_validation('type', {
            'required': True,
            'min_length': 3,
            'max_length': 15,
            'validator': Validator.validate_string()
        })
        
        self.validator.add_field_validation('phone', {
            'required': True,
            'validator': Validator.validate_phone()
        })
        
        self.validator.add_field_validation('address', {
            'required': True,
            'min_length': 3,
            'max_length': 15,
            'validator': Validator.validate_text()
        })
        
        self.validator.add_field_validation('email', {
            'required': True,
            'validator': Validator.validate_email()
        })
    def _conexion_signals(self):
        """Conecta las señales de los campos de entrada a los validadores."""
        self.name_input.textChanged.connect(self.validate_form)
        self.code_input.textChanged.connect(self.validate_form)
        self.type_input.currentTextChanged.connect(self.validate_form)
        self.phone_input.textChanged.connect(self.validate_form)
        self.address_input.textChanged.connect(self.validate_form)
        self.email_input.textChanged.connect(self.validate_form)
        self.address_input.textChanged.connect(self.validate_form)
        
    def validate_form(self):
        """Valida el formulario completo."""
        form_data = {
            'name': self.name_input.text(),
            'code': self.code_input.text(),
            'phone':self.phone_input.text(),
            'address':self.address_input.toPlainText(),
            'type':self.type_input.currentText(),
            'email':self.email_input.text(),
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
    
    def set_values(self, category):
        """Establece los valores iniciales del formulario."""
        self.name_input.setText(category['name'])
        self.code_input.setText(category['code'])
        self.type_input.setCurrentText(category['type'])
        self.phone_input.setText(category['phone'])
        self.address_input.setPlainText(category['address'])
        self.email_input.setText(category['email'])
            
    def get_values(self):
        """Devuelve los valores del formulario."""
        return {
            'name': self.name_input.text(),
            'code': self.code_input.text(),
            'type': self.type_input.currentText(),
            'phone': self.phone_input.text(),
            'address': self.address_input.toPlainText(),
            'email': self.email_input.text(),
        }
