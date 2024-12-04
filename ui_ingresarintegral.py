# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingresarintegralJqzuDl.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget, QMessageBox, QDialog)
from sympy import sympify, parse_expr, Eq
import re
import iconos
import ui_ecuacion_invalida
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(608, 463)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-25, 0, 621, 591))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 60, 491, 51))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        self.resolverIntegral = QPushButton(self.frame)
        self.resolverIntegral.setObjectName(u"resolverIntegral")
        self.resolverIntegral.setGeometry(QRect(130, 340, 151, 31))
        self.resolverIntegral.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.funcionIntegral = QLineEdit(self.frame)
        self.funcionIntegral.setObjectName(u"funcionIntegral")
        self.funcionIntegral.setGeometry(QRect(150, 140, 351, 51))
        self.funcionIntegral.setStyleSheet(u"background-color: white;\n"
"font: 900 10pt \"Segoe UI\";\n"
"color:black;\n"
"border-radius: 10px")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 220, 411, 101))
        self.label.setStyleSheet(u"background-color: rgb(68, 60, 104);\n"
"border: 2px  solid black;\n"
"border-radius: 10px")
        self.bt_sqrt = QPushButton(self.frame)
        self.bt_sqrt.setObjectName(u"bt_sqrt")
        self.bt_sqrt.setGeometry(QRect(150, 230, 51, 31))
        self.bt_sqrt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.log_bt = QPushButton(self.frame)
        self.log_bt.setObjectName(u"log_bt")
        self.log_bt.setGeometry(QRect(270, 230, 51, 31))
        self.log_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.power_bt = QPushButton(self.frame)
        self.power_bt.setObjectName(u"power_bt")
        self.power_bt.setGeometry(QRect(210, 230, 51, 31))
        self.power_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.sen_bt = QPushButton(self.frame)
        self.sen_bt.setObjectName(u"sen_bt")
        self.sen_bt.setGeometry(QRect(390, 230, 51, 31))
        self.sen_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.cos_bt = QPushButton(self.frame)
        self.cos_bt.setObjectName(u"cos_bt")
        self.cos_bt.setGeometry(QRect(450, 230, 51, 31))
        self.cos_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.tan_bt = QPushButton(self.frame)
        self.tan_bt.setObjectName(u"tan_bt")
        self.tan_bt.setGeometry(QRect(150, 280, 51, 31))
        self.tan_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.cot_bt = QPushButton(self.frame)
        self.cot_bt.setObjectName(u"cot_bt")
        self.cot_bt.setGeometry(QRect(210, 280, 51, 31))
        self.cot_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.csc_bt = QPushButton(self.frame)
        self.csc_bt.setObjectName(u"csc_bt")
        self.csc_bt.setGeometry(QRect(270, 280, 51, 31))
        self.csc_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.sec_bt = QPushButton(self.frame)
        self.sec_bt.setObjectName(u"sec_bt")
        self.sec_bt.setGeometry(QRect(330, 280, 51, 31))
        self.sec_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.arc_bt = QPushButton(self.frame)
        self.arc_bt.setObjectName(u"arc_bt")
        self.arc_bt.setGeometry(QRect(390, 280, 111, 31))
        self.arc_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.pi_bt = QPushButton(self.frame)
        self.pi_bt.setObjectName(u"pi_bt")
        self.pi_bt.setGeometry(QRect(330, 230, 51, 31))
        self.pi_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.arcsen_bt = QPushButton(self.frame)
        self.arcsen_bt.setObjectName(u"arcsen_bt")
        self.arcsen_bt.setGeometry(QRect(390, 230, 51, 31))
        self.arcsen_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arccos_bt = QPushButton(self.frame)
        self.arccos_bt.setObjectName(u"arccos_bt")
        self.arccos_bt.setGeometry(QRect(450, 230, 51, 31))
        self.arccos_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arctan_bt = QPushButton(self.frame)
        self.arctan_bt.setObjectName(u"arctan_bt")
        self.arctan_bt.setGeometry(QRect(150, 280, 51, 31))
        self.arctan_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arccot_bt = QPushButton(self.frame)
        self.arccot_bt.setObjectName(u"arccot_bt")
        self.arccot_bt.setGeometry(QRect(210, 280, 51, 31))
        self.arccot_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arccsc_bt = QPushButton(self.frame)
        self.arccsc_bt.setObjectName(u"arccsc_bt")
        self.arccsc_bt.setGeometry(QRect(270, 280, 51, 31))
        self.arccsc_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arcsec_bt = QPushButton(self.frame)
        self.arcsec_bt.setObjectName(u"arcsec_bt")
        self.arcsec_bt.setGeometry(QRect(330, 280, 51, 31))
        self.arcsec_bt.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"font: 900 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.arc_bt_2 = QPushButton(self.frame)
        self.arc_bt_2.setObjectName(u"arc_bt_2")
        self.arc_bt_2.setGeometry(QRect(390, 280, 111, 31))
        self.arc_bt_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 110, 81, 101))
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet(u" background-color: rgba(0,0,0,0);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setPixmap(QPixmap(u":/icons/integralsigno.png"))
        self.label_2.setScaledContents(True)
        self.limInferior = QLineEdit(self.frame)
        self.limInferior.setObjectName(u"limInferior")
        self.limInferior.setGeometry(QRect(100, 100, 31, 21))
        self.limInferior.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        self.limSuperior = QLineEdit(self.frame)
        self.limSuperior.setObjectName(u"limSuperior")
        self.limSuperior.setGeometry(QRect(100, 200, 31, 21))
        self.limSuperior.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ingrese la integral para resolverla mediante regla de Boole", None))
        self.resolverIntegral.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        self.label.setText("")
        self.bt_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.log_bt.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.power_bt.setText(QCoreApplication.translate("MainWindow", u"x\u02b8", None))
        self.sen_bt.setText(QCoreApplication.translate("MainWindow", u"sen", None))
        self.cos_bt.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.tan_bt.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.cot_bt.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.csc_bt.setText(QCoreApplication.translate("MainWindow", u"csc", None))
        self.sec_bt.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.arc_bt.setText(QCoreApplication.translate("MainWindow", u"modo arc", None))
        self.pi_bt.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.arcsen_bt.setText(QCoreApplication.translate("MainWindow", u"arc sen", None))
        self.arccos_bt.setText(QCoreApplication.translate("MainWindow", u"arc cos", None))
        self.arctan_bt.setText(QCoreApplication.translate("MainWindow", u"arc tan", None))
        self.arccot_bt.setText(QCoreApplication.translate("MainWindow", u"arc cot", None))
        self.arccsc_bt.setText(QCoreApplication.translate("MainWindow", u"arc csc", None))
        self.arcsec_bt.setText(QCoreApplication.translate("MainWindow", u"arc sec", None))
        self.arc_bt_2.setText(QCoreApplication.translate("MainWindow", u"modo normal", None))
        self.label_2.setText("")
        self.limInferior.setText("")
        self.limSuperior.setText("")
    # retranslateUi
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar botones con sus funciones
        self.ui.bt_sqrt.clicked.connect(lambda: self.add_operation("sqrt"))
        self.ui.log_bt.clicked.connect(lambda: self.add_operation("log"))
        self.ui.power_bt.clicked.connect(lambda: self.add_operation("power"))
        self.ui.sen_bt.clicked.connect(lambda: self.add_operation("sen"))
        self.ui.cos_bt.clicked.connect(lambda: self.add_operation("cos"))
        self.ui.tan_bt.clicked.connect(lambda: self.add_operation("tan"))
        self.ui.cot_bt.clicked.connect(lambda: self.add_operation("cot"))
        self.ui.csc_bt.clicked.connect(lambda: self.add_operation("csc"))
        self.ui.sec_bt.clicked.connect(lambda: self.add_operation("sec"))
        self.ui.pi_bt.clicked.connect(lambda: self.add_operation("pi"))
        
        # Botones modo arco
        self.ui.arc_bt.clicked.connect(self.arc_mode)
        self.ui.arc_bt_2.clicked.connect(self.normal_mode)
        self.ui.arcsen_bt.clicked.connect(lambda: self.add_operation("arcsen"))
        self.ui.arccos_bt.clicked.connect(lambda: self.add_operation("arccos"))
        self.ui.arctan_bt.clicked.connect(lambda: self.add_operation("arctan"))
        self.ui.arccot_bt.clicked.connect(lambda: self.add_operation("arccot"))
        self.ui.arccsc_bt.clicked.connect(lambda: self.add_operation("arccsc"))
        self.ui.arcsec_bt.clicked.connect(lambda: self.add_operation("arcsec"))
        
        # Ocultar botones de arco inicialmente
        self.ui.arcsen_bt.hide()
        self.ui.arccos_bt.hide()
        self.ui.arctan_bt.hide()
        self.ui.arccot_bt.hide()
        self.ui.arccsc_bt.hide()
        self.ui.arcsec_bt.hide()
        self.ui.arc_bt_2.hide()
        self.ui.resolverIntegral.clicked.connect(self.resolver_integral_boole)

    def add_operation(self, operation):
        current_text = self.ui.funcionIntegral.text()
        cursor_position = self.ui.funcionIntegral.cursorPosition()
        
        operations = {
            "sqrt": "√()",
            "log": "log()",
            "power": "^",
            "sen": "sen()",
            "cos": "cos()",
            "tan": "tan()",
            "cot": "cot()",
            "csc": "csc()",
            "sec": "sec()",
            "arcsen": "sen⁻¹()",
            "arccos": "cos⁻¹()",
            "arctan": "tan⁻¹()",
            "arccot": "cot⁻¹()",
            "arccsc": "csc⁻¹()",
            "arcsec": "sec⁻¹()",
            "pi": "π"
        }
        
        insert_text = operations.get(operation, "")
        new_text = current_text[:cursor_position] + insert_text + current_text[cursor_position:]
        self.ui.funcionIntegral.setText(new_text)
        self.ui.funcionIntegral.setCursorPosition(cursor_position + len(insert_text))
        self.ui.funcionIntegral.setFocus()

    def arc_mode(self):
        # Mostrar botones de arco
        self.ui.arcsen_bt.show()
        self.ui.arccos_bt.show()
        self.ui.arctan_bt.show()
        self.ui.arccot_bt.show()
        self.ui.arccsc_bt.show()
        self.ui.arcsec_bt.show()
        self.ui.arc_bt_2.show()
        
        # Ocultar botones normales
        self.ui.sen_bt.hide()
        self.ui.cos_bt.hide()
        self.ui.tan_bt.hide()
        self.ui.cot_bt.hide()
        self.ui.csc_bt.hide()
        self.ui.sec_bt.hide()
        self.ui.arc_bt.hide()

    def normal_mode(self):
        # Ocultar botones de arco
        self.ui.arcsen_bt.hide()
        self.ui.arccos_bt.hide()
        self.ui.arctan_bt.hide()
        self.ui.arccot_bt.hide()
        self.ui.arccsc_bt.hide()
        self.ui.arcsec_bt.hide()
        self.ui.arc_bt_2.hide()
        
        # Mostrar botones normales
        self.ui.sen_bt.show()
        self.ui.cos_bt.show()
        self.ui.tan_bt.show()
        self.ui.cot_bt.show()
        self.ui.csc_bt.show()
        self.ui.sec_bt.show()
        self.ui.arc_bt.show()

    
    def add_operation(self, operation):
        current_ecuation = self.ui.funcionIntegral.text()
        cursor_position = self.ui.funcionIntegral.cursorPosition()
        insert_operation = ""
        if operation == "sqrt":
            insert_operation = "√()"
        elif operation == "ln":
            insert_operation = "ln()"
        elif operation == "power":
            insert_operation = "^"
        elif operation == "sen":
            insert_operation = "sen()"
        elif operation == "cos":
            insert_operation = "cos()"
        elif operation == "tan":
            insert_operation = "tan()"
        elif operation == "cot":
            insert_operation = "cot()"
        elif operation == "csc":
            insert_operation = "csc()"
        elif operation == "sec":
            insert_operation = "sec()"
        elif operation == "arcsen":
            insert_operation = "sen⁻¹()"
        elif operation == "arccos":
            insert_operation = "cos⁻¹()"
        elif operation == "arctan":
            insert_operation = "tan⁻¹()"
        elif operation == "arccot":
            insert_operation = "cot⁻¹()"
        elif operation == "arccsc":
            insert_operation = "csc⁻¹()"
        elif operation == "arcsec":
            insert_operation = "sec⁻¹()"
        elif operation == "pi":
            insert_operation = "π"
        new_text = (
             current_ecuation[:cursor_position]
            + insert_operation  
            + current_ecuation[cursor_position:]  
        )
        self.ui.funcionIntegral.setText(new_text)
        self.ui.funcionIntegral.setCursorPosition(cursor_position + len(insert_operation))
        self.ui.funcionIntegral.setFocus()
    def convertir_expresion(self):
        try:
            # Obtener la expresión y los límites
            ecuacion = self.ui.funcionIntegral.text()
            lim_inf = self.ui.limInferior.text()
            lim_sup = self.ui.limSuperior.text()

            # Verificar que se ingresaron los límites
            if not lim_inf or not lim_sup:
                QMessageBox.warning(None, "Error", "Por favor ingrese los límites de integración")
                return
            # Validar que los límites sean números
            try:
                lim_inf = float(lim_inf)
                lim_sup = float(lim_sup)
            except ValueError:
                QMessageBox.warning(None, "Error", "Los límites deben ser números")
                return

            # Reemplazar funciones matemáticas
            sustituciones = {
                r"√(\w+|\(.*?\))": r"sqrt(\1)",
                r"ln(\w+|\(.*?\))": r"log(\1)",
                r"(\w+|\(.*?\))\^(\w+|\(.*?\))": r"\1**\2",
                r"sen\(": r"sin(",
                r"cos\(": r"cos(",
                r"tan\(": r"tan(",
                r"cot\(": r"1/tan(",
                r"csc\(": r"1/sin(",
                r"sec\(": r"1/cos(",
                r"sen⁻¹": r"asin",
                r"cos⁻¹": r"acos",
                r"tan⁻¹": r"atan",
                r"cot⁻¹": r"1/atan",
                r"csc⁻¹": r"1/asin",
                r"sec⁻¹": r"1/acos",
                r"π": r"pi"
            }

            # Aplicar todas las sustituciones
            for patron, reemplazo in sustituciones.items():
                ecuacion = re.sub(patron, reemplazo, ecuacion)

            # Convertir la expresión a formato sympy
            expr = parse_expr(ecuacion)
            expr = sympify(expr)

            return expr

        except Exception as e:
            self.ingresar_ecuacion = ui_ecuacion_invalida.MainWindow()
            self.ingresar_ecuacion.exec()
            self.ui.funcionIntegral.setFocus()
            return None
    def resolver_integral_boole(self):
        try:
            # Obtener la expresión y validarla
            expr = self.convertir_expresion()
            if expr is None:
                return None

            # Obtener límites de integración
            b = float(self.ui.limInferior.text())  # límite inferior
            a = float(self.ui.limSuperior.text())  # límite superior
            n = 4  # número de subintervalos para Boole

            # Calcular h
            h = (b - a) / n

            # Calcular los 5 puntos x
            x0 = a
            x1 = a + h
            x2 = a + 2*h
            x3 = a + 3*h
            x4 = b

            # Evaluar la función en los puntos
            from sympy.abc import x
            f = lambda x_val: float(expr.subs(x, x_val))
            
            y0 = f(x0)
            y1 = f(x1)
            y2 = f(x2)
            y3 = f(x3)
            y4 = f(x4)

            # Aplicar la regla de Boole
            integral = ((2*h)/45) * (7*y0 + 32*y1 + 12*y2 + 32*y3 + 7*y4)

            # Crear diccionario con resultados
            resultados = {
                'h': h,
                'puntos_x': [x0, x1, x2, x3, x4],
                'puntos_y': [y0, y1, y2, y3, y4],
                'integral': integral
            }

            # Mostrar resultados en una nueva ventana
            self.mostrar_resultados_boole(resultados)
            
            return resultados

        except Exception as e:
            QMessageBox.warning(None, "Error", f"Error al resolver la integral: {str(e)}")
            return None

    def mostrar_resultados_boole(self, resultados):
        from ui_solucionintegral import Ui_MainWindow
        self.ventana_resultados = QMainWindow()
        self.ui_resultados = Ui_MainWindow()
        self.ui_resultados.setupUi(self.ventana_resultados)
        
        # Preparar los datos para enviar
        h = f"{resultados['h']:.1f}"
        puntos = [f"x{i} = {x:.1f}, f(x{i}) = {y:.1f}" for i, (x, y) in enumerate(zip(resultados['puntos_x'], resultados['puntos_y']))]
        
        # Construir la fórmula de Boole con los puntos evaluados
        x0, x1, x2, x3, x4 = resultados['puntos_x']
        y0, y1, y2, y3, y4 = resultados['puntos_y']
        formula = (
            f"Integral ≈ (2h/45) * [7*f({x0:.1f}) + 32*f({x1:.1f}) + 12*f({x2:.1f}) + 32*f({x3:.1f}) + 7*f({x4:.1f})]\n"
            f"Integral ≈ (2*{resultados['h']:.1f}/45) * [7*{y0:.1f} + 32*{y1:.1f} + 12*{y2:.1f} + 32*{y3:.1f} + 7*{y4:.1f}]"
        )
        
        solucion = f"{resultados['integral']:.3f}"
        
        # Enviar los datos a la ventana de resultados
        self.ui_resultados.recibirDatos(h, puntos, formula, solucion)
        
        self.ventana_resultados.show()
#Main method
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
