import sys
from PySide6.QtWidgets import (QMainWindow, QComboBox, QVBoxLayout, QWidget, 
                               QMessageBox, QToolBar, QApplication, )
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QCategoryAxis
from PySide6.QtGui import QIcon, QAction, QPen, QFont
from resultados import Resultado
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QSize, QLocale

class ResultadosElectorales(QMainWindow):
    def __init__(self):
        """Inicializa la aplicación de resultados electorales."""
        super().__init__()
        self.resultados = Resultado()
        self.initUI()
        self.populate_municipios()
        self.create_graph()
    
    def initUI(self):
        self.setWindowTitle('Resultados electorales 2015-2021')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")
        self.create_toolbar()
    
    def create_toolbar(self):
        toolbar = QToolBar("Filtros")
        self.addToolBar(toolbar)
        
        # combo boxes para los filtros
        self.municipio_combo = QComboBox(self)
        self.municipio_combo.setPlaceholderText("Seleccione un municipio")
        self.municipio_combo.setMinimumWidth(200)
        self.municipio_combo.setMaximumWidth(300)
        self.municipio_combo.setStyleSheet("background-color: #ffffff;")
        self.municipio_combo.addItem("Seleccione un municipio", None)
        
        # combo box de parroquias
        self.parroquia_combo = QComboBox(self)
        self.parroquia_combo.setPlaceholderText("Seleccione una parroquia")
        self.parroquia_combo.setMinimumWidth(200)
        self.parroquia_combo.setMaximumWidth(300)
        self.parroquia_combo.setStyleSheet("background-color: #ffffff;")
        self.parroquia_combo.addItem("Seleccione una parroquia", None)
        self.parroquia_combo.setEnabled(False)
        
        # combo box de centros
        self.centro_combo = QComboBox(self)
        self.centro_combo.setPlaceholderText("Seleccione un centro")
        self.centro_combo.setMinimumWidth(200)
        self.centro_combo.setMaximumWidth(300)
        self.centro_combo.setStyleSheet("background-color: #ffffff;")  
        self.centro_combo.addItem("Seleccione un centro", None)
        self.centro_combo.setEnabled(False)
        
        self.municipio_combo.currentIndexChanged.connect(self.populate_parroquias)
        self.parroquia_combo.currentIndexChanged.connect(self.populate_centros)
        self.centro_combo.currentIndexChanged.connect(self.update_plot_centro)
        
        toolbar.addWidget(self.municipio_combo)
        toolbar.addWidget(self.parroquia_combo)
        toolbar.addWidget(self.centro_combo)
        
        
    def populate_municipios(self):
        """Llena el combo box de municipios con los datos de la base de datos."""
        municipios = self.resultados.get_municipios()
        self.municipio_combo.clear()
        for municipio in municipios:
            self.municipio_combo.addItem(municipio[0])
    
    def populate_parroquias(self):
        """Llena el combo box de parroquias con los datos de la base de datos."""
        municipio = self.municipio_combo.currentText()
        self.parroquia_combo.clear()
        
        if municipio:
            parroquias = self.resultados.get_parroquias(municipio)
            self.parroquia_combo.clear()
            self.parroquia_combo.addItem("Seleccione una parroquia", None)
            for parroquia in parroquias:
                self.parroquia_combo.addItem(parroquia[0])
            self.parroquia_combo.setEnabled(True)
            self.update_plot_municipio()
        else:
            self.parroquia_combo.clear()
            self.parroquia_combo.addItem("Seleccione una parroquia", None)
            self.parroquia_combo.setEnabled(False)
            self.update_plot_all()
    def populate_centros(self):
        """Llena el combo box de parroquias con los datos de la base de datos."""
        parroquia = self.parroquia_combo.currentText()
        municipio = self.municipio_combo.currentText()
        
        self.centro_combo.clear()
        
        if parroquia:
            centros = self.resultados.get_centros(municipio,parroquia)
            self.centro_combo.addItem("Seleccione una parroquia", None)
            for centro in centros:
                self.centro_combo.addItem(centro[1],centro[0])
            self.centro_combo.setEnabled(True)
            self.update_plot_parroquia()
        else:
            self.centro_combo.clear()
            self.centro_combo.setEnabled(False)
    def create_graph(self):
        """Crea un gráfico de lineas con los resultados electorales."""
        # Aquí iría el código para crear el gráfico
        self.chart = QChart()
        self.chart.setLocale(QLocale(QLocale.Spanish, QLocale.Venezuela))
        self.chart.setAnimationOptions(QChart.AllAnimations)
        
        self.series = QLineSeries()
        self.series.setPointLabelsVisible(True)
        self.series.setName("Resultados electorales")
        self.series.setPointLabelsFormat("@yPoint")
        self.series.setPointLabelsFont(QFont("Arial", 14))
        self.series.setPen(QPen(Qt.blue, 2))
        
        
        self.chart.addSeries(self.series)
        
        # Ejes
        self.axisX = QCategoryAxis()
        self.chart.setTitle("Resultados electorales 2015-2021")
        self.axisX.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        self.axisX.append("AN2015",1)
        self.axisX.append("REG2017",2)
        self.axisX.append("PRES2018",3)
        self.axisX.append("REG2021",4)
        self.axisX.setRange(0, 5)
        
        # eje Y
        self.axisY = QValueAxis()
        self.axisY.setTitleText("Votos")
        self.axisY.setLabelsVisible(False)
        self.axisY.setGridLineVisible(False)
        
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setMinimumSize(QSize(800, 600))
        
        # widget central
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.update_plot_all()
        
    def update_plot(self,resultados):
        """Actualiza el gráfico con los resultados electorales."""
        self.series.clear()
        for i in range(1, 5):
            self.series.append(i, resultados[i-1])
        
        max_value = max(resultados)
        self.axisY.setRange(0, max_value*1.2)
        
        self.chart_view.setChart(self.chart)
        self.chart_view.update()
        self.chart_view.repaint()
        self.chart_view.show()
        
    def update_plot_all(self):
        resultados = self.resultados.get_resultados()
        
        self.series.clear()
        self.update_plot(resultados)
        
    def update_plot_municipio(self):
        
        """Actualiza el gráfico con los resultados de un municipio específico."""
        municipio = self.municipio_combo.currentText()
        
        if municipio:
            resultados = self.resultados.get_resultados_municipio(municipio)
            self.update_plot(resultados)  
    
    def update_plot_parroquia(self):
        
        """Actualiza el gráfico con los resultados de un municipio específico."""
        municipio = self.municipio_combo.currentText()
        parroquia = self.parroquia_combo.currentText()
        
        if municipio and parroquia:
            resultados = self.resultados.get_resultados_parroquia(municipio,parroquia)
            self.update_plot(resultados)  
    
    def update_plot_centro(self):
        centro = self.centro_combo.currentData()
        if centro:
            resultados = self.resultados.get_resultados_centro(centro)
            self.update_plot(resultados)
            
if __name__ == "__main__": 
    print(__name__)
    app = QApplication(sys.argv)
    window = ResultadosElectorales()
    window.show()
    sys.exit(app.exec())
