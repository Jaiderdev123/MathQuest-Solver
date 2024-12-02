# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingresarecuacionSJitAL.ui'
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
from scipy import constants
import numpy as np
import re
import math
import rc_iconos

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
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 70, 581, 51))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 360, 131, 31))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 15pt \"Segoe UI Black\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resolverNR = QPushButton(self.frame)
        self.resolverNR.setObjectName(u"resolverNR")
        self.resolverNR.setGeometry(QRect(260, 360, 151, 31))
        self.resolverNR.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.resolverSecante = QPushButton(self.frame)
        self.resolverSecante.setObjectName(u"resolverSecante")
        self.resolverSecante.setGeometry(QRect(430, 360, 121, 31))
        self.resolverSecante.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.ecuacion = QLineEdit(self.frame)
        self.ecuacion.setObjectName(u"ecuacion")
        self.ecuacion.setGeometry(QRect(150, 140, 351, 51))
        self.ecuacion.setStyleSheet(u"background-color: white;\n"
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
        self.ln_bt = QPushButton(self.frame)
        self.ln_bt.setObjectName(u"ln_bt")
        self.ln_bt.setGeometry(QRect(270, 230, 51, 31))
        self.ln_bt.setStyleSheet(u"QPushButton{\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
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
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(254, 204, 25);\n"
"}\n"
"")
        self.normal_bt = QPushButton(self.frame)
        self.normal_bt.setObjectName(u"normal_bt")
        self.normal_bt.setGeometry(QRect(390, 280, 111, 31))
        self.normal_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ingrese la ecuaci\u00f3n a resolver por m\u00e9todos abiertos a continuaci\u00f3n:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Resolver por:", None))
        self.resolverNR.setText(QCoreApplication.translate("MainWindow", u"Newton-Rhapson", None))
        self.resolverSecante.setText(QCoreApplication.translate("MainWindow", u"Secante", None))
        self.label.setText("")
        self.bt_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.ln_bt.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.power_bt.setText(QCoreApplication.translate("MainWindow", u"x\u02b8", None))
        self.sen_bt.setText(QCoreApplication.translate("MainWindow", u"sen", None))
        self.cos_bt.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.tan_bt.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.cot_bt.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.csc_bt.setText(QCoreApplication.translate("MainWindow", u"csc", None))
        self.sec_bt.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.arc_bt.setText(QCoreApplication.translate("MainWindow", u"modo arc", None))
        self.pi_bt.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.arcsen_bt.setText(QCoreApplication.translate("MainWindow", u"sen ⁻¹", None))
        self.arccos_bt.setText(QCoreApplication.translate("MainWindow", u"cos ⁻¹", None))
        self.arctan_bt.setText(QCoreApplication.translate("MainWindow", u"tan ⁻¹", None))
        self.arccot_bt.setText(QCoreApplication.translate("MainWindow", u"cot ⁻¹", None))
        self.arccsc_bt.setText(QCoreApplication.translate("MainWindow", u"csc ⁻¹", None))
        self.arcsec_bt.setText(QCoreApplication.translate("MainWindow", u"sec ⁻¹", None))
        self.normal_bt.setText(QCoreApplication.translate("MainWindow", u"modo normal", None))
    # retranslateUi
    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.arcsen_bt.hide()
        self.ui.arccos_bt.hide()
        self.ui.arctan_bt.hide()
        self.ui.arccot_bt.hide()
        self.ui.arccsc_bt.hide()
        self.ui.arcsec_bt.hide()
        self.ui.normal_bt.hide()

        self.ui.arc_bt.clicked.connect(self.arc_mode)
        self.ui.normal_bt.clicked.connect(self.normal_mode)

        self.ui.bt_sqrt.clicked.connect(lambda: self.add_operation("sqrt"))
        self.ui.ln_bt.clicked.connect(lambda: self.add_operation("ln"))
        self.ui.power_bt.clicked.connect(lambda: self.add_operation("power"))
        self.ui.sen_bt.clicked.connect(lambda: self.add_operation("sen"))
        self.ui.cos_bt.clicked.connect(lambda: self.add_operation("cos"))
        self.ui.tan_bt.clicked.connect(lambda: self.add_operation("tan"))
        self.ui.cot_bt.clicked.connect(lambda: self.add_operation("cot"))
        self.ui.csc_bt.clicked.connect(lambda: self.add_operation("csc"))
        self.ui.sec_bt.clicked.connect(lambda: self.add_operation("sec"))
        self.ui.arcsen_bt.clicked.connect(lambda: self.add_operation("arcsen"))
        self.ui.arccos_bt.clicked.connect(lambda: self.add_operation("arccos"))
        self.ui.arctan_bt.clicked.connect(lambda: self.add_operation("arctan"))
        self.ui.arccot_bt.clicked.connect(lambda: self.add_operation("arccot"))
        self.ui.arccsc_bt.clicked.connect(lambda: self.add_operation("arccsc"))
        self.ui.arcsec_bt.clicked.connect(lambda: self.add_operation("arcsec"))
        self.ui.pi_bt.clicked.connect(lambda: self.add_operation("pi"))
        self.ui.resolverNR.clicked.connect(self.verificar)
        # self.ui.resolverSecante.clicked.connect(self.resolverSecante)
        
    
    def arc_mode(self):
        self.ui.arcsen_bt.show()
        self.ui.arccos_bt.show()
        self.ui.arctan_bt.show()
        self.ui.arccot_bt.show()
        self.ui.arccsc_bt.show()
        self.ui.arcsec_bt.show()
        self.ui.normal_bt.show()
        self.ui.sen_bt.hide()
        self.ui.cos_bt.hide()
        self.ui.tan_bt.hide()
        self.ui.cot_bt.hide()
        self.ui.csc_bt.hide()
        self.ui.sec_bt.hide()
        self.ui.arc_bt.hide()

    def normal_mode(self):
        self.ui.arcsen_bt.hide()
        self.ui.arccos_bt.hide()
        self.ui.arctan_bt.hide()
        self.ui.arccot_bt.hide()
        self.ui.arccsc_bt.hide()
        self.ui.arcsec_bt.hide()
        self.ui.normal_bt.hide()
        self.ui.sen_bt.show()
        self.ui.cos_bt.show()
        self.ui.tan_bt.show()
        self.ui.cot_bt.show()
        self.ui.csc_bt.show()
        self.ui.sec_bt.show()
        self.ui.arc_bt.show()
    
    def add_operation(self, operation):
        if operation == "sqrt":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "√()")
        elif operation == "ln":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "ln()")
        elif operation == "power":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "^")
        elif operation == "sen":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "sen()")
        elif operation == "cos":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "cos()")
        elif operation == "tan":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "tan()")
        elif operation == "cot":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "cot()")
        elif operation == "csc":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "csc()")
        elif operation == "sec":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "sec()")
        elif operation == "arcsen":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "sen⁻¹()")
        elif operation == "arccos":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "cos⁻¹()")
        elif operation == "arctan":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "tan⁻¹()")
        elif operation == "arccot":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "cot⁻¹()")
        elif operation == "arccsc":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "csc⁻¹()")
        elif operation == "arcsec":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "sec⁻¹()")
        elif operation == "pi":
            self.ui.ecuacion.setText(self.ui.ecuacion.text() + "π")
        self.ui.ecuacion.setFocus()

    def verificar(self):
        ecuacion = self.ui.ecuacion.text()
        print(ecuacion)
        if "√" in ecuacion:
                ecuacion = re.sub(r"√(\w+|\(.*?\))", r"math.sqrt(\1)", ecuacion)
        if "ln" in ecuacion:
                ecuacion = re.sub(r"ln(\w+|\(.*?\))", r"np.log(\1)", ecuacion)
        if "^" in ecuacion:
                ecuacion = re.sub(r"(\w+|\(.*?\))\^(\w+|\(.*?\))", r"(\1)**(\2)", ecuacion)
        if "sen(" in ecuacion:
                ecuacion = re.sub(r"sen(", r"np.sin(", ecuacion)
        if "cos(" in ecuacion:
                ecuacion = re.sub(r"cos\(", r"np.cos(", ecuacion)
        if "tan(" in ecuacion:
                ecuacion = re.sub(r"tan\(", r"np.tan(", ecuacion)
        if "cot(" in ecuacion:
                ecuacion = re.sub(r"cot\(", r"1/np.cot(", ecuacion)
        if "csc(" in ecuacion:
                ecuacion = re.sub(r"csc\(", r"1/np.sin(", ecuacion)
        if "sec(" in ecuacion:
                ecuacion = re.sub(r"sec\(", r"1/np.cos(", ecuacion)
        if "sen⁻¹" in ecuacion:
                ecuacion = re.sub(r"sen⁻¹", r"np.arcsin", ecuacion)
        if "cos⁻¹" in ecuacion:
                ecuacion = re.sub(r"cos⁻¹", r"np.arccos", ecuacion)
        if "tan⁻¹" in ecuacion:
                ecuacion = re.sub(r"tan⁻¹", r"np.arctan", ecuacion)
        if "cot⁻¹" in ecuacion:
                ecuacion = re.sub(r"cot⁻¹", r"1/np.arctan", ecuacion)
        if "csc⁻¹" in ecuacion:
                ecuacion = re.sub(r"csc⁻¹", r"1/np.arcsin", ecuacion)
        if "sec⁻¹" in ecuacion:
                ecuacion = re.sub(r"sec⁻¹", r"1/np.arccos", ecuacion)
        if "π" in ecuacion:
                ecuacion = re.sub(r"π", r"np.pi", ecuacion)
        try:
            print(ecuacion)
            print(eval(ecuacion))
        except Exception as e:
            print("invalid ecuation")
         
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())