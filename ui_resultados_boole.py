#Iimportamos las librerias necesarias
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget, QVBoxLayout)

class Ui_ResultadosBoole(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("ResultadosBoole")
        Dialog.resize(400, 300)
        
        self.verticalLayout = QVBoxLayout(Dialog)
        
        # Label para mostrar h
        self.h_label = QLabel(Dialog)
        self.h_label.setStyleSheet("font: 12pt;")
        self.verticalLayout.addWidget(self.h_label)
        
        # Label para mostrar puntos
        self.puntos_label = QLabel(Dialog)
        self.puntos_label.setStyleSheet("font: 12pt;")
        self.verticalLayout.addWidget(self.puntos_label)
        
        # Label para mostrar resultado
        self.resultado_label = QLabel(Dialog)
        self.resultado_label.setStyleSheet("font: 14pt bold;")
        self.verticalLayout.addWidget(self.resultado_label)