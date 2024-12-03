# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingresarmatriziKqEdt.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget, QMessageBox, QDialog)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 401)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 621, 591))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 381, 51))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tipoMatriz = QComboBox(self.frame)
        self.tipoMatriz.addItem("")
        self.tipoMatriz.addItem("")
        self.tipoMatriz.addItem("")
        self.tipoMatriz.setObjectName(u"tipoMatriz")
        self.tipoMatriz.setGeometry(QRect(430, 30, 171, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.tipoMatriz.setFont(font)
        self.tipoMatriz.setLayoutDirection(Qt.LeftToRight)
        self.tipoMatriz.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.aplicarMatriz = QPushButton(self.frame)
        self.aplicarMatriz.setObjectName(u"aplicarMatriz")
        self.aplicarMatriz.setGeometry(QRect(430, 70, 171, 31))
        self.aplicarMatriz.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.tablaMatriz = QTableWidget(self.frame)
        if (self.tablaMatriz.columnCount() < 3):
            self.tablaMatriz.setColumnCount(3)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tablaMatriz.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaMatriz.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaMatriz.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tablaMatriz.rowCount() < 2):
            self.tablaMatriz.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaMatriz.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaMatriz.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaMatriz.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaMatriz.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaMatriz.setItem(0, 2, __qtablewidgetitem7)
        self.tablaMatriz.setObjectName(u"tablaMatriz")
        self.tablaMatriz.setGeometry(QRect(40, 130, 338, 88))
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
        self.label_6.setGeometry(QRect(40, 330, 131, 31))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 15pt \"Segoe UI Black\";")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.resolverGauss = QPushButton(self.frame)
        self.resolverGauss.setObjectName(u"resolverGauss")
        self.resolverGauss.setGeometry(QRect(180, 330, 91, 31))
        self.resolverGauss.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.resolverGaussJordan = QPushButton(self.frame)
        self.resolverGaussJordan.setObjectName(u"resolverGaussJordan")
        self.resolverGaussJordan.setGeometry(QRect(280, 330, 121, 31))
        self.resolverGaussJordan.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.resolverCramer = QPushButton(self.frame)
        self.resolverCramer.setObjectName(u"resolverCramer")
        self.resolverCramer.setGeometry(QRect(410, 330, 91, 31))
        self.resolverCramer.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.resolverInversa = QPushButton(self.frame)
        self.resolverInversa.setObjectName(u"resolverInversa")
        self.resolverInversa.setGeometry(QRect(510, 330, 91, 31))
        self.resolverInversa.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        #Conexión de botones
        self.resolverGaussJordan.clicked.connect(self.resolverGauss_Jordan)
        self.aplicarMatriz.clicked.connect(self.actualizarTabla)
        QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seleccione el tipo de matriz:", None))
        self.tipoMatriz.setItemText(0, QCoreApplication.translate("MainWindow", u"2 X 2", None))
        self.tipoMatriz.setItemText(1, QCoreApplication.translate("MainWindow", u"3 X 3", None))
        self.tipoMatriz.setItemText(2, QCoreApplication.translate("MainWindow", u"4 X 4", None))
        self.aplicarMatriz.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        ___qtablewidgetitem = self.tablaMatriz.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None));
        ___qtablewidgetitem1 = self.tablaMatriz.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X2", None));
        ___qtablewidgetitem2 = self.tablaMatriz.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"B", None));
        ___qtablewidgetitem3 = self.tablaMatriz.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Eq 1", None));
        ___qtablewidgetitem4 = self.tablaMatriz.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Eq 2", None));
        __sortingEnabled = self.tablaMatriz.isSortingEnabled()
        self.tablaMatriz.setSortingEnabled(False)
        self.tablaMatriz.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Resolver por:", None))
        self.resolverGauss.setText(QCoreApplication.translate("MainWindow", u"Gauss", None))
        self.resolverGaussJordan.setText(QCoreApplication.translate("MainWindow", u"Gauss-Jordan", None))
        self.resolverCramer.setText(QCoreApplication.translate("MainWindow", u"Cramer", None))
        self.resolverInversa.setText(QCoreApplication.translate("MainWindow", u"Inversa", None))

    def actualizarTabla(self):
        tipo = self.tipoMatriz.currentIndex()
        if tipo == 0:  # 2x2
            self.tablaMatriz.setGeometry(QRect(40, 130, 338, 88))
            self.tablaMatriz.setRowCount(2)
            self.tablaMatriz.setColumnCount(3)
        elif tipo == 1:  # 3x3
            self.tablaMatriz.setGeometry(QRect(40, 130, 435, 118))
            self.tablaMatriz.setRowCount(3)
            self.tablaMatriz.setColumnCount(4)
        elif tipo == 2:  # 4x4
            self.tablaMatriz.setGeometry(QRect(40, 130, 540, 150))
            self.tablaMatriz.setRowCount(4)
            self.tablaMatriz.setColumnCount(5)

        # Inicializar la tabla con valores vacíos
        for i in range(self.tablaMatriz.rowCount()):
            for j in range(self.tablaMatriz.columnCount()):
                self.tablaMatriz.setItem(i, j, QTableWidgetItem(""))

        # Configurar los encabezados de las columnas
        for j in range(self.tablaMatriz.columnCount() - 1):
            self.tablaMatriz.setHorizontalHeaderItem(j, QTableWidgetItem(f"X{j + 1}"))
        self.tablaMatriz.setHorizontalHeaderItem(self.tablaMatriz.columnCount() - 1, QTableWidgetItem("B"))

        # Configurar los encabezados de las filas
        for i in range(self.tablaMatriz.rowCount()):
            self.tablaMatriz.setVerticalHeaderItem(i, QTableWidgetItem(f"Eq {i + 1}"))
    def resolverGauss_Jordan(self):
        # Obtener los coeficientes de la tabla
        filas = self.tablaMatriz.rowCount()
        columnas = self.tablaMatriz.columnCount()
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                item = self.tablaMatriz.item(i, j)
                if item and item.text():
                    try:
                        valor = float(item.text())
                    except ValueError:
                        QMessageBox.warning(None, "Error", "Por favor, ingrese solo números.")
                        return
                    fila.append(valor)
                else:
                    QMessageBox.warning(None, "Error", "Complete todos los campos de la matriz.")
                    return
            matriz.append(fila)

        # Inicializar listas para las iteraciones y pasos
        iteraciones = []
        pasos = []

        # Implementar el método Gauss-Jordan
        n = len(matriz[0]) - 1  # Número de variables
        for i in range(n):
            # Verificar que el pivote no sea cero
            if matriz[i][i] == 0:
                QMessageBox.warning(None, "Error", f"El pivote en la fila {i+1} es cero, no se puede continuar.")
                return
            # Hacer el pivote igual a 1
            pivote = matriz[i][i]
            matriz[i] = [elemento / pivote for elemento in matriz[i]]
            pasos.append(f"F{i+1} = F{i+1} / {pivote}")
            iteraciones.append([fila[:] for fila in matriz])
            # Hacer ceros en la columna i
            for j in range(filas):
                if j != i:
                    factor = matriz[j][i]
                    matriz[j] = [elem_j - factor * elem_i for elem_j, elem_i in zip(matriz[j], matriz[i])]
                    pasos.append(f"F{j+1} = F{j+1} - ({factor}) * F{i+1}")
                    iteraciones.append([fila[:] for fila in matriz])
        from ui_pasos import Ui_Form
        MainWindow.close()
        dialogo = QDialog()
        ui = Ui_Form()
        ui.setupUi(dialogo)
        ui.mostrar_pasos(iteraciones, pasos)
        dialogo.exec()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())