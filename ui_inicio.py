# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iniciowOlXKZ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import iconos
import ui_ingresarmatriz
import ui_ingresarecuacion
import ui_ingresarintegral
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 679)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 691, 661))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(0, 20, 691, 61))
        self.titulo.setLayoutDirection(Qt.LeftToRight)
        self.titulo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Night Machine\";")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 110, 691, 61))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Segoe UI Black\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.ecuaciones = QPushButton(self.frame)
        self.ecuaciones.setObjectName(u"ecuaciones")
        self.ecuaciones.setGeometry(QRect(290, 200, 111, 101))
        self.ecuaciones.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/fx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ecuaciones.setIcon(icon)
        self.ecuaciones.setIconSize(QSize(100, 100))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 300, 691, 41))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 14pt \"Segoe UI Black\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 440, 691, 41))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 14pt \"Segoe UI Black\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.matrices = QPushButton(self.frame)
        self.matrices.setObjectName(u"matrices")
        self.matrices.setGeometry(QRect(290, 340, 111, 101))
        self.matrices.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/matrices.png", QSize(), QIcon.Normal, QIcon.Off)
        self.matrices.setIcon(icon1)
        self.matrices.setIconSize(QSize(100, 100))
        self.integrales = QPushButton(self.frame)
        self.integrales.setObjectName(u"integrales")
        self.integrales.setGeometry(QRect(290, 480, 111, 101))
        self.integrales.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/integral.png", QSize(), QIcon.Normal, QIcon.Off)
        self.integrales.setIcon(icon2)
        self.integrales.setIconSize(QSize(100, 100))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 580, 691, 41))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 14pt \"Segoe UI Black\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ecuaciones.clicked.connect(self.abrirEcuaciones)
        self.matrices.clicked.connect(self.abrirMatrices)
        self.integrales.clicked.connect(self.abrirIntegrales)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"MathQuest Solver", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione el tipo de operacion:", None))
        self.ecuaciones.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Calcular raices de ecuaciones", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resolver sistemas de ecuaciones (matrices)", None))
        self.matrices.setText("")
        self.integrales.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Resolver integrales", None))
    # retranslateUi
 
    def abrirMatrices(self):
        self.ventana = QMainWindow()
        self.ui = ui_ingresarmatriz.Ui_MainWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    def abrirEcuaciones(self):
        self.ventana = ui_ingresarecuacion.MainWindow()
        self.ui = ui_ingresarecuacion.Ui_MainWindow()
        self.ventana.show()

    def abrirIntegrales(self):
        self.ventana = ui_ingresarintegral.MainWindow()
        self.ui = ui_ingresarintegral.Ui_MainWindow()
        self.ventana.show()

#Main method
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())