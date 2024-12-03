# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resolver_biseccionvgHbLV.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from sympy import (parse_expr, sympify, simplify, evalf, symbols, sstr, sin, cos, 
tan, cot, csc, sec, asin, acos, atan, acot, asin, 
acos, atan, acot, Eq, solve, ln, pi)
from sympy.abc import x
import iconos
import ui_ingresarecuacion

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(577, 342)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 691, 611))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 511, 31))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 15pt \"Segoe UI Black\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ecuacionDP = QLineEdit(self.frame)
        self.ecuacionDP.setObjectName(u"ecuacionDP")
        self.ecuacionDP.setGeometry(QRect(30, 70, 531, 41))
        self.ecuacionDP.setStyleSheet(u"background-color: white;\n"
"font: 900 14pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"color: black")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(68, 130, 311, 61))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error = QLineEdit(self.frame)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(388, 140, 71, 41))
        self.error.setStyleSheet(u"background-color: white;\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"color: black")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 150, 31, 20))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resolver_bt = QPushButton(self.frame)
        self.resolver_bt.setObjectName(u"resolver_bt")
        self.resolver_bt.setGeometry(QRect(460, 266, 101, 31))
        self.resolver_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(99, 89, 133);\n"
"font: 900 12pt Segoe UI Black;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}")
        self.volver_bt = QPushButton(self.frame)
        self.volver_bt.setObjectName(u"volver_bt")
        self.volver_bt.setGeometry(QRect(24, 264, 91, 31))
        self.volver_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(99, 89, 133);\n"
"font: 900 12pt Segoe UI Black;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}")
        self.a_intervalo = QLineEdit(self.frame)
        self.a_intervalo.setObjectName(u"a_intervalo")
        self.a_intervalo.setGeometry(QRect(412, 200, 51, 41))
        self.a_intervalo.setStyleSheet(u"background-color: white;\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"color: black")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 361, 61))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(383, 202, 21, 31))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(467, 208, 21, 31))
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_intervalo = QLineEdit(self.frame)
        self.b_intervalo.setObjectName(u"b_intervalo")
        self.b_intervalo.setGeometry(QRect(490, 200, 51, 41))
        self.b_intervalo.setStyleSheet(u"background-color: white;\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"color: black")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(550, 200, 21, 31))
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ecuaci\u00f3n a ser resuelta por m\u00e9todo de bisecci\u00f3n:", None))
        self.ecuacionDP.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ingrese el porcentaje de error deseado:", None))
        self.error.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.resolver_bt.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        self.volver_bt.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.a_intervalo.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ingrese los extremos del intervalo a evaluar:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.b_intervalo.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"]", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self, ecuacion, ecuacionDP):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.volver_bt.clicked.connect(self.volver)
        ecuacion_mostrar = sstr(ecuacion)
        self.ui.ecuacionDP.setText(ecuacionDP)
        self.ui.ecuacionDP.setReadOnly(True)
        self.ui.ecuacionDP.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def volver(self):
        self.ventana = ui_ingresarecuacion.MainWindow()
        self.ui = ui_ingresarecuacion.Ui_MainWindow()
        self.ventana.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ecuacion_prueba = Eq(x**3 - 3*x + 1, x)
    window = MainWindow(ecuacion_prueba, "x=2")
    window.show()
    sys.exit(app.exec())