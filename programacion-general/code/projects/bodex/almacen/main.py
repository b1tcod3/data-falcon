import sys
from PySide6.QtWidgets import QApplication
from supplier_management import SupplierManagement
   
if __name__ == "__main__": 
    print(__name__)
    app = QApplication(sys.argv)
    window = SupplierManagement()
    window.show()
    sys.exit(app.exec())