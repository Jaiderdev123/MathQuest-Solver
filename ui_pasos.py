# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pasosapdLJj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget, QVBoxLayout)
import iconos
from ui_solucionmatriz import Ui_Form as solucionresultado
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(580, 316)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 621, 361))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tablaMatriz = QTableWidget(self.frame)
        self.tablaMatriz.setObjectName(u"tablaMatriz")
        self.tablaMatriz.setGeometry(QRect(10, 50, 561, 192))
        self.tablaMatriz.setStyleSheet(u"QHeaderView::section { background-color: #635985; \n"
"color: white;             \n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QTableWidget{\n"
"color: white;\n"
"background-color: #635985; \n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: black;\n"
"color: white;  \n"
"}\n"
" ")
        self.tablaMatriz.horizontalHeader().setVisible(True)
        self.tablaMatriz.horizontalHeader().setCascadingSectionResizes(False)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 260, 71, 31))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 15pt \"Segoe UI Black\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pasosLabel = QLabel(self.frame)
        self.pasosLabel.setObjectName(u"pasosLabel")
        self.pasosLabel.setGeometry(QRect(80, 260, 381, 50))
        self.pasosLabel.setStyleSheet(u"background-color: rgb(68, 60, 104);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 15pt \"Segoe UI Black\";\n"
"border-radius: 3px;")
        self.botonAnterior = QPushButton(self.frame)
        self.botonAnterior.setObjectName(u"botonAnterior")
        self.botonAnterior.setGeometry(QRect(470, 250, 41, 51))
        self.botonAnterior.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        icon = QIcon()
        icon.addFile(u":/icons/volver.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAnterior.setIcon(icon)
        self.botonAnterior.setIconSize(QSize(40, 40))
        self.botonSiguiente = QPushButton(self.frame)
        self.botonSiguiente.setObjectName(u"botonSiguiente")
        self.botonSiguiente.setGeometry(QRect(530, 250, 41, 51))
        self.botonSiguiente.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        icon1 = QIcon()
        icon1.addFile(u":/icons/siguiente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonSiguiente.setIcon(icon1)
        self.botonSiguiente.setIconSize(QSize(40, 50))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 131, 36))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.botonRegresar = QPushButton(self.frame)
        self.botonRegresar.setObjectName(u"botonRegresar")
        self.botonRegresar.setGeometry(QRect(530, 0, 41, 51))
        self.botonRegresar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/regresar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonRegresar.setIcon(icon2)
        self.botonRegresar.setIconSize(QSize(40, 40))
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        #Conexion de botones
        self.botonSiguiente.clicked.connect(self.siguiente_paso)
        self.botonAnterior.clicked.connect(self.anterior_paso)
        self.botonRegresar.clicked.connect(Form.close)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Pasos: ", None))
        
        # Configurar encabezados dinámicamente
        columnas = self.tablaMatriz.columnCount()
        filas = self.tablaMatriz.rowCount()
        
        # Configurar encabezados de columnas
        headerColumnas = []
        for j in range(columnas - 1):
            headerColumnas.append(f"X{j + 1}")
        headerColumnas.append("B")
        self.tablaMatriz.setHorizontalHeaderLabels(headerColumnas)
        
        # Configurar encabezados de filas
        headerFilas = [f"Eq {i + 1}" for i in range(filas)]
        self.tablaMatriz.setVerticalHeaderLabels(headerFilas)
        
        self.pasosLabel.setText("")
        self.botonAnterior.setText("")
        self.botonSiguiente.setText("")
        self.label.setText(QCoreApplication.translate("Form", u" Solución:", None))
        self.botonRegresar.setText("")

    def mostrar_pasos(self, iteraciones, pasos, metodo, tipo_matriz, soluciones_resultados):
        self.metodo = metodo
        self.iteraciones = iteraciones
        self.pasos = pasos
        self.indice = 0
        self.mostrar_paso()
        self.tipo_matriz = tipo_matriz
        self.soluciones_resultados = soluciones_resultados

    def mostrar_paso(self):
        if self.indice < len(self.iteraciones):
            matriz = self.iteraciones[self.indice]
            paso = self.pasos[self.indice]
            self.pasosLabel.setText(paso)
            # Actualizar tabla
            filas = len(matriz)
            columnas = len(matriz[0])
            self.tablaMatriz.setRowCount(filas)
            self.tablaMatriz.setColumnCount(columnas)
            for i in range(filas):
                for j in range(columnas):
                    self.tablaMatriz.setItem(i, j, QTableWidgetItem(str(matriz[i][j])))

    def siguiente_paso(self):
        if self.metodo == "Gauss-Jordan":
            if self.indice < len(self.iteraciones) - 1:
                self.indice += 1
                self.mostrar_paso()
                self.resultado = []
                for i in range(len(self.iteraciones[self.indice])):
                    self.resultado.append(self.iteraciones[self.indice][i][-1])
            else:
                self.enviar_resultados(self.resultado)
        else:
            if self.indice < len(self.iteraciones) - 1:
                self.indice += 1
                self.mostrar_paso()
                self.resultado = []
                # for i in range(len(self.iteraciones[self.indice])):
                #     self.resultado.append(self.iteraciones[self.indice][i][-1])
            else:
                for i in range(self.tipo_matriz-1, -1, -1):
                    print(self.soluciones_resultados[i])
                    self.resultado.append(self.soluciones_resultados[i])
                self.enviar_resultados(self.resultado)
                
        
    def anterior_paso(self):
        if self.indice > 0:
            self.indice -= 1
            self.mostrar_paso()

    def enviar_resultados(self, resultado):
        solucionresultado.set_solucion(self, resultado)
        #Mostrar ventana de solucion
        self.ventanaSolucion = QWidget()
        self.ventanaSolucion.setWindowModality(Qt.ApplicationModal)
        self.solucion = solucionresultado()
        self.solucion.setupUi(self.ventanaSolucion)
        self.ventanaSolucion.raise_() 
        self.ventanaSolucion.activateWindow()
        self.ventanaSolucion.show()
#Main method
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())