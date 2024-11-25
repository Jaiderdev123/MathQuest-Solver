# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicioeadxAV.ui'
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
import iconos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 691, 611))
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
        self.label_4.setGeometry(QRect(0, 480, 691, 41))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 14pt \"Segoe UI Black\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.matrices = QPushButton(self.frame)
        self.matrices.setObjectName(u"matrices")
        self.matrices.setGeometry(QRect(290, 380, 111, 101))
        self.matrices.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/matrices.png", QSize(), QIcon.Normal, QIcon.Off)
        self.matrices.setIcon(icon1)
        self.matrices.setIconSize(QSize(100, 100))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

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
    # retranslateUi

