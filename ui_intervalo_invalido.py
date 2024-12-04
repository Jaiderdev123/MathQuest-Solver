# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intervalo_invalidoPnWaAP.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import iconos

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(386, 238)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-30, 0, 1041, 901))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 361, 61))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.matrices_2 = QPushButton(self.frame)
        self.matrices_2.setObjectName(u"matrices_2")
        self.matrices_2.setGeometry(QRect(170, 160, 111, 51))
        self.matrices_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(99, 89, 133);\n"
"font:20pt \"Yu Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #a49bb0;\n"
"}\n"
"")
        self.matrices_2.setIconSize(QSize(100, 100))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"El intervalo ingresado no es v\u00e1lido", None))
        self.matrices_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

class Dialog(QDialog):
    def __init__(self, no_solution):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if no_solution:
            self.ui.label_2.setText("La solución no se encuentra en el intervalo")
        self.ui.matrices_2.clicked.connect(self.accept)

    def accept(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Dialog(False)
    window.show()
    sys.exit(app.exec())
