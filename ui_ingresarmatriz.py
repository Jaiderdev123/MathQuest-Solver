# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingresarmatrizWnbBum.ui'
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
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import iconos_rc

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
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);")
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
        self.tablaMatriz.setGeometry(QRect(40, 130, 561, 192))
        self.tablaMatriz.setStyleSheet(u"QHeaderView::section { background-color: #635985; \n"
"color: white;             \n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QTableWidget{\n"
"color: white;\n"
"background-color: #635985; \n"
"font-weight: bold;\n"
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
        self.resolverGauss_2 = QPushButton(self.frame)
        self.resolverGauss_2.setObjectName(u"resolverGauss_2")
        self.resolverGauss_2.setGeometry(QRect(280, 330, 121, 31))
        self.resolverGauss_2.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.resolverGauss_3 = QPushButton(self.frame)
        self.resolverGauss_3.setObjectName(u"resolverGauss_3")
        self.resolverGauss_3.setGeometry(QRect(410, 330, 91, 31))
        self.resolverGauss_3.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.resolverGauss_4 = QPushButton(self.frame)
        self.resolverGauss_4.setObjectName(u"resolverGauss_4")
        self.resolverGauss_4.setGeometry(QRect(510, 330, 91, 31))
        self.resolverGauss_4.setStyleSheet(u"background-color:rgb(99, 89, 133);\n"
"font: 900 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

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
        self.resolverGauss_2.setText(QCoreApplication.translate("MainWindow", u"Gauss-Jordan", None))
        self.resolverGauss_3.setText(QCoreApplication.translate("MainWindow", u"Cramer", None))
        self.resolverGauss_4.setText(QCoreApplication.translate("MainWindow", u"Inversa", None))
    # retranslateUi

