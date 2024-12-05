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
    QPalette, QPixmap, QRadialGradient, QTransform, QDoubleValidator)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget, QDialog)
from sympy import (parse_expr, sympify, simplify, evalf, symbols, sstr, N, Rational,sin, cos, 
tan, cot, csc, sec, asin, acos, atan, acot, asin, 
acos, atan, acot, Eq, solve, ln, pi)
from sympy.abc import x
import iconos
import ui_ingresarecuacion
import ui_intervalo_invalido
from ui_pasos_biseccion import Ui_Form, Widget
from ui_solucion_biseccion import Ui_Form_Solucion, WidgetSolucion

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
"font: 900 10pt \"Segoe UI Black\";\n"
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
"font: 900 10pt \"Segoe UI Black\";\n"
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
        self.ecuacionDP = ecuacionDP
        self.ui.ecuacionDP.setText(self.ecuacionDP)
        self.ui.ecuacionDP.setReadOnly(True)
        self.ui.ecuacionDP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #   error_validator = QDoubleValidator(0.0001, 999.0, 4, self)
        #   error_validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        #   self.ui.error.setValidator(error_validator)
        #   
        #   interval_validator = QDoubleValidator(-100000, 100000, 3)
        #   interval_validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        #   self.ui.a_intervalo.setValidator(interval_validator)
        #   self.ui.b_intervalo.setValidator(interval_validator)
        
        self.ui.resolver_bt.clicked.connect(lambda: self.resolver(ecuacion))

    def volver(self):
        self.ventana = ui_ingresarecuacion.MainWindow()
        self.ui = ui_ingresarecuacion.Ui_MainWindow()
        self.ventana.show()
        self.close()

    def resolver(self, ecuacion):
        self.verificar_intervalo(ecuacion)

    def verificar_intervalo(self, ecuacion):
        a = float(self.ui.a_intervalo.text())
        b = float(self.ui.b_intervalo.text())
        if a < b:
            print(f"Ecuacion: {ecuacion}")
            self.function = ecuacion.lhs - ecuacion.rhs
            print(f"Funcion: {self.function}")
            f_a = self.function.subs(x, a)
            f_b = self.function.subs(x, b)
            print(f_a, f_b)
            interval_evaluation = f_a * f_b
            print(f"La solución está en el intervalo [{a}, {b}] ?: {interval_evaluation}")
            if interval_evaluation <= 0:
                if f_a == 0:
                    print(f"La raiz es {a}")
                    # self.ventana = ui_raiz.MainWindow(ecuacion, a)
                    # self.ui = ui_raiz.Ui_MainWindow()
                    # self.ventana.show()
                    # self.close()
                elif f_b == 0:
                    print(f"La raiz es {b}")
                    # self.ventana = ui_raiz.MainWindow(ecuacion, b)
                    # self.ui = ui_raiz.Ui_MainWindow()
                    # self.ventana.show()
                    # self.close()
                else:
                    print("La raíz se encuentra en el intervalo")
                    self.solucion()
                    # self.ventana = ui_resolver_biseccion.MainWindow(ecuacion, a, b)
                    # self.ui = ui_resolver_biseccion.Ui_MainWindow()
                    # self.ventana.show()
                    # self.close()
            else:
                self.ingresar_intervalo = ui_intervalo_invalido.Dialog(True)
                self.ingresar_intervalo.exec()
                self.ui.a_intervalo.setFocus()
        else:
            self.ingresar_intervalo = ui_intervalo_invalido.Dialog(False)
            self.ingresar_intervalo.exec()
            self.ui.a_intervalo.setFocus()

    def solucion(self):
        error_achieved = False
        pasos = []
        iteration = 0
        print("Error deseado actual: ", self.ui.error.text())
        
        while not error_achieved:
            tipo_descripcion = 0
            error = None
            if iteration == 0:
                a = float(self.ui.a_intervalo.text())
                b = float(self.ui.b_intervalo.text())
                
            if iteration > 0:
                if pasos[iteration - 1].fa_fxr < 0:
                    a = pasos[iteration - 1].a
                    b = pasos[iteration - 1].xr
                    tipo_descripcion = 1
                elif pasos[iteration - 1].fa_fxr > 0:
                    a = pasos[iteration - 1].xr
                    b = pasos[iteration - 1].b
                    tipo_descripcion = 2
                else:
                    error_achieved = True
                    descripcion = "Se encontró la solución exacta"
                    break
                error = (abs((b - a) / 2))*100
                error = N(error, 4)
            

            xr = (a + b) / 2
            f_a = self.function.subs(x, a)
            f_b = self.function.subs(x, b)
            f_xr = self.function.subs(x, xr)
            fa_fxr = f_a * f_xr

            

            if iteration == 0:
                print("Escribiendo descripcion para iteración 1")
                descripcion = f"""Se ubica el extremo inferior ({a}) y el superior del intervalo ({b}) en las columnas a y b respectivamente.\n
Luego, se calcula el punto medio entre estos dos puntos con la formula (a+b)/2 y se ubica en la columna Xr. En este caso es {xr}.\n
Ahora, se calcula el valor de la ecuacion en el punto a, b y xr y se ubican en las columnas f(a), f(b) y f(Xr) respectivamente.\n
En este caso, estos valores son {f_a}, {f_b} y {f_xr} respectivamente.\n
Además, se calcula el producto f(a)*f(Xr) y se ubica en la columna f(a)*f(Xr). En este caso es {fa_fxr}.\n
Ya que esta es la primera iteración, no se coloca nada en la columna error.
                """

            if iteration > 0:
                print(f"Escribiendo descripcion para iteración {iteration+1}")
                if tipo_descripcion == 1:
                    descripcion = f"""En este caso, el producto f(a)*f(xr) en la anterior fila es negativo, entonces se ubica el mismo valor de a ({a}) de la fila anterior en la columna a esta fila y el valor de Xr ({xr}) de la anterior fila en la columna b de esta fila.
Luego, se calcula de nuevo el punto medio entre estos dos puntos con la formula (a+b)/2 y se ubica en la columna xr. En este caso es {xr}.\n
Ahora, se calcula el valor de la ecuacion en el punto a, b y xr y se ubican en las columnas f(a), f(b) y f(xr) respectivamente.\n
Para esta fila dichos valores son {f_a}, {f_b} y {f_xr} respectivamente.\n
Nuevamente se calcula el producto f(a)*f(xr) y se ubica en la columna f(a)*f(Xr). En este caso es {fa_fxr}.
Se calcula el error con la formula |b-a|/2 como {(abs((b-a)/2))*100} y se ubica en la columna error. En este caso es {error}
                """

                elif tipo_descripcion == 2:
                    descripcion = f"""En este caso, el producto f(a)*f(xr) en la anterior fila es positivo, entonces se ubica el valor de Xr ({xr}) de la fila anterior en la columna a de esta fila y el mismo valor de b ({b}) de la anterior fila en la columna b de esta fila.
Luego, se calcula de nuevo el punto medio entre estos dos puntos con la formula (a+b)/2 y se ubica en la columna xr. En este caso es {xr}.\n
Ahora, se calcula el valor de la ecuacion en el punto a, b y xr y se ubican en las columnas f(a), f(b) y f(xr) respectivamente.\n
Para esta fila dichos valores son {f_a}, {f_b} y {f_xr} respectivamente.\n
Nuevamente se calcula el producto f(a)*f(xr) y se ubica en la columna f(a)*f(Xr). En este caso es {fa_fxr}.
Se calcula el error con la formula |b-a|/2 como {(abs((b-a)/2))*100} y se ubica en la columna error. En este caso es {error}
                """

            print(f"Iteración actual: {iteration}")

            a = N(a, 7)
            b = N(b, 7) 
            xr = N(xr, 7)
            f_a = N(f_a, 7)
            f_b = N(f_b, 7)
            f_xr = N(f_xr, 7)
            fa_fxr = N(fa_fxr, 7)
            pasos.append(paso(iteration, a, b, xr, f_a, f_b, f_xr, fa_fxr, error, descripcion))
            
            if error != None:
                if error < float(self.ui.error.text()):
                    error_achieved = True
                    descripcion = f"Se alcanzó el error deseado con un error de {error}% en la iteración {iteration+1}"
                    break
            iteration += 1

        self.dialogo = QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.dialogo)
        self.dialogo.setWindowModality(Qt.ApplicationModal)
        self.ui.llenar_tabla(pasos, self.ecuacionDP, 0)
        self.dialogo.finished.connect(lambda: self.show_solution(descripcion, xr, error, iteration))
        self.dialogo.show()

    def show_solution(self, descripcion, xr, error, iteration):
        self.solucion = QDialog()
        self.ui = Ui_Form_Solucion()
        self.ui.setupUi(self.solucion)
        self.ui.llenar_datos(descripcion, str(xr), str(error), str(iteration+1))
        self.solucion.show()

class paso():
    def __init__(self, number, a, b, xr, f_a, f_b, f_xr, fa_fxr, error=None, descripcion=""):
        self.number = number
        self.a = a
        self.b = b
        self.xr = xr
        self.f_a = f_a
        self.f_b = f_b
        self.fa_fxr = fa_fxr
        self.f_xr = f_xr
        self.error = error
        self.descripcion = descripcion
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ecuacion_prueba = Eq(x**2 - 4, 2)
    window = MainWindow(ecuacion_prueba, "x^2-4=2")
    window.show()
    sys.exit(app.exec())