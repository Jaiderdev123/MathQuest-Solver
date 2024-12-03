# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solucionmatrizDMlGUu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 230)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 401, 301))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 131, 36))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 51, 36))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 51, 36))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 51, 36))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 180, 51, 36))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.solX1 = QLabel(self.frame)
        self.solX1.setObjectName(u"solX1")
        self.solX1.setGeometry(QRect(60, 60, 301, 36))
        self.solX1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.solX2 = QLabel(self.frame)
        self.solX2.setObjectName(u"solX2")
        self.solX2.setGeometry(QRect(60, 100, 301, 36))
        self.solX2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.solX3 = QLabel(self.frame)
        self.solX3.setObjectName(u"solX3")
        self.solX3.setGeometry(QRect(60, 140, 301, 36))
        self.solX3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.solX4 = QLabel(self.frame)
        self.solX4.setObjectName(u"solX4")
        self.solX4.setGeometry(QRect(60, 180, 301, 36))
        self.solX4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label.setVisible(True)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.retranslateUi(Form)
        self.mostrar_solucion()
        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def set_solucion(self, solucion):
        Ui_Form.solucion = solucion
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u" Soluci\u00f3n:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"X1:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"X2:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"X3:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"X4:", None))
        self.solX1.setText("")
        self.solX2.setText("")
        self.solX3.setText("")
        self.solX4.setText("")
    # retranslateUi
    def mostrar_solucion(self):
        case = len(Ui_Form.solucion)
        if case == 1:
            self.solX1.setText(str(Ui_Form.solucion[0]))
            self.label_2.setVisible(True)
        elif case == 2:
            self.solX1.setText(str(Ui_Form.solucion[0]))
            self.solX2.setText(str(Ui_Form.solucion[1]))
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)
        elif case == 3:
            self.solX1.setText(str(Ui_Form.solucion[0]))
            self.solX2.setText(str(Ui_Form.solucion[1]))
            self.solX3.setText(str(Ui_Form.solucion[2]))
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)
            self.label_4.setVisible(True)
        elif case == 4:
            self.solX1.setText(str(Ui_Form.solucion[0]))
            self.solX2.setText(str(Ui_Form.solucion[1]))
            self.solX3.setText(str(Ui_Form.solucion[2]))
            self.solX4.setText(str(Ui_Form.solucion[3]))
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)
            self.label_4.setVisible(True)
            self.label_5.setVisible(True)
#Main method
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())