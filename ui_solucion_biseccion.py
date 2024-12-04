# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solucion_biseccionNsfAhn.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form_Solucion(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 230)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 511, 301))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.descripcion = QLabel(self.frame)
        self.descripcion.setObjectName(u"descripcion")
        self.descripcion.setGeometry(QRect(10, 10, 491, 36))
        self.descripcion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"Segoe UI Black\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 201, 36))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(13, 118, 131, 36))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(13, 176, 121, 36))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.solucion = QLabel(self.frame)
        self.solucion.setObjectName(u"solucion")
        self.solucion.setGeometry(QRect(215, 61, 250, 36))
        self.solucion.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.error = QLabel(self.frame)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(152, 117, 200, 36))
        self.error.setStyleSheet(u"color: rgb(0, 170, 255);\n"
"font: 900 14pt \"Segoe UI Black\";")
        self.iteraciones = QLabel(self.frame)
        self.iteraciones.setObjectName(u"iteraciones")
        self.iteraciones.setGeometry(QRect(140, 180, 161, 31))
        self.iteraciones.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"font: 900 12pt \"Segoe UI Black\";")
        self.ok_bt = QPushButton(self.frame)
        self.ok_bt.setObjectName(u"ok_bt")
        self.ok_bt.setGeometry(QRect(350, 180, 101, 31))
        self.ok_bt.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font:15pt \"Yu Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.ok_bt.setIconSize(QSize(100, 100))
        self.ok_bt.clicked.connect(Form.close)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def llenar_datos(self, desc, solucion, error, iteraciones):
        print("llenando datos")
        print("El error es: "+error)
        print("La solucion es: "+solucion)
        print("La iteraciones son: "+iteraciones)
        print("La descripcion es: "+desc)
        self.descripcion.setText(desc)
        self.solucion.setText(solucion)
        if error == "None":
            error = "0"
            self.descripcion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        print(f"El error es: {error}")
        self.error.setText(error+" %")
        self.iteraciones.setText(iteraciones+" iteraciones")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.descripcion.setText(QCoreApplication.translate("Form", u"Se termin\u00f3 el proceso porque se encontr\u00f3 la soluci\u00f3n exacta", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"La ra\u00edz de la ecuaci\u00f3n es:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Con un error del:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Encontrada en:", None))
        self.solucion.setText(QCoreApplication.translate("Form", u"2.58259823", None))
        self.error.setText(QCoreApplication.translate("Form", u"10 %", None))
        self.iteraciones.setText(QCoreApplication.translate("Form", u"10 iteraciones", None))
        self.ok_bt.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

class WidgetSolucion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Solucion()
        self.ui.setupUi(self)
        self.ui.ok_bt.clicked.connect(self.close)
        
    def llenar_datos(self, desc, solucion, error, iteraciones):
        print("llenando datos")
        print("El error es: "+error)
        print("La solucion es: "+solucion)
        print("La iteraciones son: "+iteraciones)
        print("La descripcion es: "+desc)
        self.ui.descripcion.setText(desc)
        self.ui.solucion.setText(solucion)
        if error == "None":
            error = "0"
            self.ui.descripcion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
            print(f"El error es: {error}")
        self.ui.error.setText(error+" %")
        self.ui.iteraciones.setText(iteraciones+" iteraciones")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WidgetSolucion()
    window.show()
    sys.exit(app.exec())