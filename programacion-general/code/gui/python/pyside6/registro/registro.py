import sys
import random
import re
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                     QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QComboBox,
                     QTableWidgetItem, QMessageBox, QMainWindow, QDockWidget, QFormLayout, QSpinBox, QToolBar)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize
import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

def validate_age(age):
    if age.isdigit():
        age_num = int(age)
        return 0 <= age_num <= 99
    return False

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Registro de Usuarios")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 600, 400)
        
        create_database()
        self.init_ui()
        self.update_table()
        self.setStyleSheet("background-color: #f0f0f0;")
        
    def init_ui(self):
        self.current_page = 1
        self.items_per_page = 10
        
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)
        
        self.setCentralWidget(self.table)
        # cantidad de columnas de la tabla
        self.table.setColumnCount(4)
        # encabezado de la tabla
        labels = ["ID", "Nombre", "Email", "Edad"]
        self.table.setHorizontalHeaderLabels(labels)
        
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 50)
        
        self.table.cellClicked.connect(self.load_user)
        
        #dock widget
        dock = QDockWidget("Nuevo Usuario")
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        
        # Crear Formulario
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)
        
        # entradas
        self.entry_name = QLineEdit(form)
        self.entry_email = QLineEdit(form)
        self.entry_age = QSpinBox(form,minimum=2,maximum=100)
        self.entry_age.clear()
        
        # agregando entradas
        layout.addRow("Nombre: ",self.entry_name)
        layout.addRow("Email: ",self.entry_email)
        layout.addRow("Age: ",self.entry_age)
        
        # botón de guardar
        btn_save = QPushButton("Guardar", self)
        btn_save.clicked.connect(self.insert_user)
        layout.addRow(btn_save)
        
        # botón de actualizar
        btn_edit = QPushButton("Actualizar", self)
        btn_edit.clicked.connect(self.update_user)
        layout.addRow(btn_edit)
        
        #botón de limpiar
        btn_clear = QPushButton("Limpiar", self)
        btn_clear.clicked.connect(self.clear_fields)
        layout.addRow(btn_clear)
        
        # agregar delete y edit button
        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        delete_action = QAction(QIcon('remove.png'),'&Delete',self)
        delete_action.triggered.connect(self.delete_user)
        toolbar.addAction(delete_action)
        
        delete_quit = QAction(QIcon('exit.png'),'&Quit',self)
        delete_quit.triggered.connect(self.close)
        toolbar.addAction(delete_quit)
        
        self.entry_search = QLineEdit()
        self.entry_search.setPlaceholderText("Buscar usuario...")
        self.entry_search.setMaximumWidth(200)
        self.entry_search.textChanged.connect(self.filter_users)
        toolbar.addWidget(self.entry_search)
        
        # controles de paginación
        page_label = QLabel("Registros por página:")
        page_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        toolbar.addWidget(page_label)
        self.page_size_combo = QComboBox()
        self.page_size_combo.addItems(["5", "10", "20"])
        self.page_size_combo.setCurrentText("10")
        self.page_size_combo.currentTextChanged.connect(self.update_items_per_page)
        toolbar.addWidget(self.page_size_combo)
        
        # buton anterior
        self.prev_btn = QPushButton("Anterior")
        self.prev_btn.clicked.connect(self.previous_page)
        toolbar.addWidget(self.prev_btn)
        
        # buton siguiente
        self.next_btn = QPushButton("Siguiente")
        self.next_btn.clicked.connect(self.next_page)
        toolbar.addWidget(self.next_btn)
        
        self.page_label = QLabel()
        toolbar.addWidget(self.page_label)
        
        self.update_pagination_label()
            
        # agregar widget
        dock.setMinimumWidth(250)
        dock.setWidget(form)
        
    def insert_user(self):
        name = self.entry_name.text().strip()
        email = self.entry_email.text().strip()
        age = self.entry_age.text().strip()
        
        if not name or not age:
            QMessageBox.warning(self,'Error','Datos Incompletos')
            return
        if not name.isalpha():
            QMessageBox.warning(self,'Error','Nombre Incorrecto')
            return
        if not validate_age(age):
            QMessageBox.warning(self,'Error','Edad Incorrecta')
            return
        if not validate_email(email):
            QMessageBox.warning(self,'Error','Email Incorrecta')
            return
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''
                INSERT INTO users (name, email, age)
                VALUES (?, ?, ?)
            ''', (name, email,age))
        QMessageBox.information(self,'Èxito','Datos guardados exitosamente')
        conn.commit()
        conn.close()
        
        self.clear_fields()
        self.update_table()
    
    def filter_users(self):
        self.current_page = 1
        self.update_pagination_label()
        self.update_table()

    def get_users(self):
        search_text = self.entry_search.text().strip()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''
                SELECT id,name,email,age FROM users
                WHERE name LIKE ? OR email LIKE ? OR age LIKE ?
                ORDER BY id ASC
                LIMIT ? OFFSET ?
            ''', ('%' + search_text + '%', '%' + search_text + '%','%' + search_text + '%', self.items_per_page, (self.current_page - 1) * self.items_per_page)) 
        rows = c.fetchall()
        conn.close()

        self.table.setRowCount(0)
        for user in rows:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for i, data in enumerate(user):
                self.table.setItem(row_position, i, QTableWidgetItem(str(data)))
        
    def load_user(self,row,column):
        self.entry_name.setText(self.table.item(row, 1).text())
        self.entry_email.setText(self.table.item(row, 2).text())
        self.entry_age.setValue(int(self.table.item(row, 3).text()))
        
    def update_user(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, 'Error', 'Seleccione un usuario para actualizar.')
            return

        user_id = self.table.item(selected_row, 0).text()
        name = self.entry_name.text().strip()
        email = self.entry_email.text().strip()
        age = self.entry_age.text().strip()

        if not name or not age:
            QMessageBox.warning(self, 'Error', 'Datos Incompletos')
            return
        if not name.isalpha():
            QMessageBox.warning(self, 'Error', 'Nombre Incorrecto')
            return
        if not validate_age(age):
            QMessageBox.warning(self, 'Error', 'Edad Incorrecta')
            return
        if not validate_email(email):
            QMessageBox.warning(self, 'Error', 'Email Incorrecta')
            return

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''
                UPDATE users
                SET name=?, email=?, age=?
                WHERE id=?
            ''', (name, email, age, user_id))
        conn.commit()
        conn.close()
        self.clear_fields()
        self.update_table()
    
    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, 'Error', 'Seleccione un usuario para eliminar.')
            return

        user_id = self.table.item(selected_row, 0).text()

        button = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estás Seguro de Eliminar el usuario?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if(button==QMessageBox.StandardButton.No):
            return        
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id=?', (user_id,))
        conn.commit()
        conn.close()
        self.clear_fields()
        self.update_table()    
            
    def update_table(self):
        self.get_users()
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()    
    
    def clear_fields(self):
        self.entry_name.clear()
        self.entry_email.clear()
        self.entry_age.clear()
    
    def update_items_per_page(self,text):
        self.items_per_page = int(text)
        self.current_page = 1
        self.update_pagination_label()
        self.update_table
        
    def update_pagination_label(self):
        total_records = self.get_total_records()
        total_pages = max(1, (total_records + self.items_per_page - 1) // self.items_per_page)
        self.page_label.setText(f"Página {self.current_page} de {total_pages}")
        self.prev_btn.setEnabled(self.current_page > 1)
        self.next_btn.setEnabled(self.current_page < total_pages)
        self.update_table()
        
    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_pagination_label()
            self.update_table()
        else:
            QMessageBox.warning(self, 'Error', 'No hay más páginas anteriores.')
    def next_page(self):
        total_records = self.get_total_records()
        total_pages = max(1, (total_records + self.items_per_page - 1) // self.items_per_page)
        if self.current_page < total_pages:
            self.current_page += 1
            self.update_pagination_label()
            self.update_table()
        else:
            QMessageBox.warning(self, 'Error', 'No hay más páginas siguientes.')
    def get_total_records(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM users')
        total_records = c.fetchone()[0]
        conn.close()
        return total_records
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())