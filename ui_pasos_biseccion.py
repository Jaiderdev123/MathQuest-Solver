# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pasos_biseccionaugcFH.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget, QDialog)
import iconos

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 361)
        self.Form = Form
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 771, 361))
        self.frame.setStyleSheet(u"background-color: rgb(24, 18, 43);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tablaIteraciones = QTableWidget(self.frame)
        if (self.tablaIteraciones.columnCount() < 8):
            self.tablaIteraciones.setColumnCount(8)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tablaIteraciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaIteraciones.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tablaIteraciones.setObjectName(u"tablaIteraciones")
        self.tablaIteraciones.setGeometry(QRect(10, 50, 741, 192))
        self.tablaIteraciones.setStyleSheet(u"QHeaderView::section { background-color: #635985; \n"
"color: white;             \n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"}\n"
"QTableWidget{\n"
"color: white;\n"
"background-color: #635985; \n"
"font-weight: bold;\n"
"font-size: 10px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: black;\n"
"color: white;  \n"
"}\n"
" ")
        self.tablaIteraciones.horizontalHeader().setVisible(True)
        self.tablaIteraciones.horizontalHeader().setCascadingSectionResizes(False)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 260, 71, 31))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Segoe UI Black\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.bt_anterior = QPushButton(self.frame)
        self.bt_anterior.setObjectName(u"bt_anterior")
        self.bt_anterior.setGeometry(QRect(640, 280, 41, 51))
        self.bt_anterior.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        icon = QIcon()
        icon.addFile(u":/icons/volver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_anterior.setIcon(icon)
        self.bt_anterior.setIconSize(QSize(40, 40))
        self.bt_siguiente = QPushButton(self.frame)
        self.bt_siguiente.setObjectName(u"bt_siguiente")
        self.bt_siguiente.setGeometry(QRect(700, 280, 41, 51))
        self.bt_siguiente.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        icon1 = QIcon()
        icon1.addFile(u":/icons/siguiente.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_siguiente.setIcon(icon1)
        self.bt_siguiente.setIconSize(QSize(40, 50))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 2, 151, 36))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 17pt \"Segoe UI Black\";")
        self.bt_volver = QPushButton(self.frame)
        self.bt_volver.setObjectName(u"bt_volver")
        self.bt_volver.setGeometry(QRect(713, 0, 41, 51))
        self.bt_volver.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/regresar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_volver.setIcon(icon2)
        self.bt_volver.setIconSize(QSize(40, 40))
        self.ecuacionDP = QLineEdit(self.frame)
        self.ecuacionDP.setObjectName(u"ecuacionDP")
        self.ecuacionDP.setGeometry(QRect(164, 8, 521, 31))
        self.ecuacionDP.setStyleSheet(u"background-color: white;\n"
"font: 900 14pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"color: black")
        self.ecuacionDP.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.pasos_descripcion = QTextEdit(self.frame)
        self.pasos_descripcion.setObjectName(u"pasos")
        self.pasos_descripcion.setGeometry(QRect(93, 253, 541, 101))
        self.pasos_descripcion.setStyleSheet(u"background-color: rgb(57, 48, 83);\n"
"font: 900 10pt \"Segoe UI Black\";\n"
"color: white;\n"
"")

        self.retranslateUi(Form)
        self.bt_siguiente.clicked.connect(self.siguiente)
        self.bt_anterior.clicked.connect(self.anterior)
        self.bt_volver.clicked.connect(self.Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def llenar_tabla(self, pasos, ecuacionDP, iteration):
        self.pasos = pasos
        self.ecuacionDP_received = ecuacionDP
        self.iteration = iteration
        self.ecuacionDP.setText(self.ecuacionDP_received)
        print(f"Current iteration: {self.iteration}")
        print(f"Data at iteration: {self.pasos[self.iteration].number}")
        if not self.pasos or self.iteration < 0 or self.iteration >= len(self.pasos):
            print(f"Invalid iteration: {self.iteration} or pasos is empty")
            return
        self.tablaIteraciones.clearContents()
        self.tablaIteraciones.setRowCount(0)
        self.tablaIteraciones.setRowCount(len(self.pasos))
        self.tablaIteraciones.setColumnCount(8)
        self.tablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        # Update equation and description
        self.ecuacionDP.setText(self.ecuacionDP_received)
        # self.ui.ecuacionDP.setReadOnly(True)
        self.pasos_descripcion.setText(self.pasos[self.iteration].descripcion)

        # Update label for the step
        self.label_6.setText(f"Paso {self.iteration + 1}:")

        # Column widths
        column_widths = [90, 90, 90, 90, 90, 90, 90, 90]
        for i, width in enumerate(column_widths):
            self.tablaIteraciones.setColumnWidth(i, width)

    # Fill table with data up to the current iteration
        for i in range(self.iteration + 1):
            print(f"Filling row: {i}")
            self.tablaIteraciones.setItem(i, 0, QTableWidgetItem(str(self.pasos[i].a)))
            self.tablaIteraciones.setItem(i, 1, QTableWidgetItem(str(self.pasos[i].b)))
            self.tablaIteraciones.setItem(i, 2, QTableWidgetItem(str(self.pasos[i].xr)))
            self.tablaIteraciones.setItem(i, 3, QTableWidgetItem(str(self.pasos[i].f_a)))
            self.tablaIteraciones.setItem(i, 4, QTableWidgetItem(str(self.pasos[i].f_b)))
            self.tablaIteraciones.setItem(i, 5, QTableWidgetItem(str(self.pasos[i].f_xr)))
            self.tablaIteraciones.setItem(i, 6, QTableWidgetItem(str(self.pasos[i].fa_fxr)))
            self.tablaIteraciones.setItem(i, 7, QTableWidgetItem(str(self.pasos[i].error)+" %"))

        # Update the table view
        self.tablaIteraciones.viewport().update()

    def siguiente(self):
        if self.iteration < len(self.pasos) - 1:
            self.iteration += 1
            self.llenar_tabla(self.pasos, self.ecuacionDP_received, self.iteration)
            print(f"Adelantando a iteracion {self.iteration}")
        else:
            self.bt_siguiente.setDisabled(True)
            self.Form.close()

    def anterior(self):
        if self.iteration > 0:
            self.iteration -= 1
            self.llenar_tabla(self.pasos, self.ecuacionDP_received, self.iteration)
            print(f"Retrocediendo a iteracion {self.iteration}")
        else:
            self.bt_anterior.setDisabled(True)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tablaIteraciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem1 = self.tablaIteraciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"b", None));
        ___qtablewidgetitem2 = self.tablaIteraciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Xr", None));
        ___qtablewidgetitem3 = self.tablaIteraciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"f(a)", None));
        ___qtablewidgetitem4 = self.tablaIteraciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"f(b)", None));
        ___qtablewidgetitem5 = self.tablaIteraciones.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"f(Xr)", None));
        ___qtablewidgetitem6 = self.tablaIteraciones.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"f(a)*f(Xr)", None));
        ___qtablewidgetitem7 = self.tablaIteraciones.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"E", None));

        self.label_6.setText(QCoreApplication.translate("Form", u"Paso 1: ", None))
        self.bt_anterior.setText("")
        self.bt_siguiente.setText("")
        self.label.setText(QCoreApplication.translate("Form", u" Soluci\u00f3n de:", None))
        self.bt_volver.setText("")
        self.ecuacionDP.setText("")
        self.pasos_descripcion.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI Black'; font-size:10pt; font-weight:900; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

class Widget(QWidget):
    def __init__(self, pasos, ecuacionDP, iteration):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.pasos = pasos
        self.ecuacionDP = ecuacionDP
        self.ui.ecuacionDP.setText(self.ecuacionDP)
        self.iteration = iteration

        self.ui.bt_siguiente.clicked.connect(self.siguiente)
        self.ui.bt_anterior.clicked.connect(self.anterior)
        self.ui.bt_volver.clicked.connect(self.close)

        self.llenar_tabla()

    def llenar_tabla(self):
        print(f"Current iteration: {self.iteration}")
        print(f"Data at iteration: {self.pasos[self.iteration].number}")
        if not self.pasos or self.iteration < 0 or self.iteration >= len(self.pasos):
            print(f"Invalid iteration: {self.iteration} or pasos is empty")
            return
        self.ui.tablaIteraciones.clearContents()
        self.ui.tablaIteraciones.setRowCount(0)
        self.ui.tablaIteraciones.setRowCount(len(self.pasos))
        self.ui.tablaIteraciones.setColumnCount(8)
        self.ui.tablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        # Update equation and description
        self.ui.ecuacionDP.setText(self.ecuacionDP)
        # self.ui.ecuacionDP.setReadOnly(True)
        self.ui.pasos.setText(self.pasos[self.iteration].descripcion)

        # Update label for the step
        self.ui.label_6.setText(f"Paso {self.iteration + 1}:")

        # Column widths
        column_widths = [90, 90, 90, 90, 90, 90, 90, 90]
        for i, width in enumerate(column_widths):
            self.ui.tablaIteraciones.setColumnWidth(i, width)

    # Fill table with data up to the current iteration
        for i in range(self.iteration + 1):
            print(f"Filling row: {i}")
            self.ui.tablaIteraciones.setItem(i, 0, QTableWidgetItem(str(self.pasos[i].a)))
            self.ui.tablaIteraciones.setItem(i, 1, QTableWidgetItem(str(self.pasos[i].b)))
            self.ui.tablaIteraciones.setItem(i, 2, QTableWidgetItem(str(self.pasos[i].xr)))
            self.ui.tablaIteraciones.setItem(i, 3, QTableWidgetItem(str(self.pasos[i].f_a)))
            self.ui.tablaIteraciones.setItem(i, 4, QTableWidgetItem(str(self.pasos[i].f_b)))
            self.ui.tablaIteraciones.setItem(i, 5, QTableWidgetItem(str(self.pasos[i].f_xr)))
            self.ui.tablaIteraciones.setItem(i, 6, QTableWidgetItem(str(self.pasos[i].fa_fxr)))
            self.ui.tablaIteraciones.setItem(i, 7, QTableWidgetItem(str(self.pasos[i].error)))

        # Update the table view
        self.ui.tablaIteraciones.viewport().update()

    def siguiente(self):
        # if self.iteration < len(self.pasos) - 1:
        #     self.iteration += 1
        #     self.llenar_tabla()
        #     print(f"Adelantando a iteracion {self.iteration}")
        # else:
        #     print("No more steps ahead")
        self.ui.ecuacionDP.setText("test")

    def anterior(self):
        if self.iteration > 0:
            self.iteration -= 1
            self.llenar_tabla()
            print(f"Retrocediendo a iteracion {self.iteration}")
        else:
            print("No more steps back")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Widget(None, None)
    window.show()
    sys.exit(app.exec())