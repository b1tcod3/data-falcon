from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QMessageBox

from models.almacen import Almacen

class Validator:
    """Clase para validar entradas en los campos de texto."""
    @staticmethod
    def validate_string():
        """Valida string letras y numeros """
        regex = QRegularExpression("^[a-zA-Z0-9\s]{3,30}$") 
        return QRegularExpressionValidator(regex)

    @staticmethod
    def validate_text():
        """Valida la descripción del producto."""
        regex = QRegularExpression("^[a-zA-Z0-9\s]{3,100}$") 
        return QRegularExpressionValidator(regex)
    
    @staticmethod
    def validate_integer():
        """Valida entero"""
        regex = QRegularExpression("^[0-9]{1,10}$") 
        return QRegularExpressionValidator(regex)

    @staticmethod
    def validate_email():
        """Valida email"""
        # Regex para validar un correo electrónico
        regex = QRegularExpression("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$") 
        return QRegularExpressionValidator(regex)
    
    def validate_phone():
        """Valida telefono"""
        # Regex para validar un telefono
        regex = QRegularExpression("^(\+58|58)?(0?4\d{10}|0?2[1-9]\d{10})$")
        return QRegularExpressionValidator(regex)
    
    @staticmethod
    def validate_real():
        """Valida si algo es real"""
        regex = QRegularExpression("^[0-9]+(\.[0-9]{1,5})?$") 
        return QRegularExpressionValidator(regex)
    
class FormValidator:
    """Clase para validar formularios."""
    def __init__(self):
        self.errors = {}
        self.almacen = Almacen()
        self.field_validations ={}
    
    def add_field_validation(self, field_name, rules):
        """Agrega validaciones para un campo específico."""
        self.field_validations[field_name] = rules
    
    def validate_form(self,form_data):
        """Valida el formulario completo."""
        self.errors.clear()
        
        for field_name, rules in self.field_validations.items():
            value = form_data.get(field_name,'')
            self._validate_field(field_name, value, rules)
    
    def _validate_field(self, field_name, value, rules):
        """Valida un campo específico."""
        field_errors = []
        
        # validacion de requerido
        if rules.get('required', False) and not value:
            field_errors.append(f"{field_name} es requerido.")
        
        # validacion de longitud minima
        if 'min_length' in rules and len(value) < rules['min_length']:
            field_errors.append(f"{field_name} debe tener al menos {rules['min_length']} caracteres.")
        # validacion de longitud maxima
        if 'max_length' in rules and len(value) > rules['max_length']:
            field_errors.append(f"{field_name} no puede tener más de {rules['max_length']} caracteres.")
        # validacion de regex
        if 'validator' in rules:
            state, _,_ = rules['validator'].validate(value,0)
            if state != QRegularExpressionValidator.Acceptable:
                field_errors.append(f"{field_name} no es válido.")
        if 'unique' in rules:
            # Aquí puedes agregar la lógica para verificar la unicidad en la base de datos
            # Por ejemplo, si estás usando SQLite:
            if self.almacen.exists(rules['unique']['table'],field_name, value,rules['unique'].get('exclude_id',None)):
               field_errors.append(f"{field_name} ya existe.")
            pass
        
        if field_errors:
            self.errors[field_name] = field_errors
            
    def get_error_messages(self):
        """Devuelve los mensajes de error formateados."""
        messages = []
        for field, errors in self.errors.items():
            for error in errors:
                messages.append(f"{field.capitalize()}: {error}")
        return messages
    @staticmethod
    def mostrar_errores(parent,messages):
        """Muestra los errores en un cuadro de diálogo."""
        if messages:
            error_message = "\n".join(messages)
            QMessageBox.critical(parent, "Errores de Validación", error_message)
            return True
        return False
    
    def has_errors(self):
        """Verifica si hay errores en el formulario."""
        return bool(self.errors)
    def clear_errors(self):
        """Limpia los errores del formulario."""
        self.errors.clear()
    
    