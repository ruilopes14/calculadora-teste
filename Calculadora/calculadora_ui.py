# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(301, 439)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 301, 431))
        self.calculadora = QWidget()
        self.calculadora.setObjectName(u"calculadora")
        self.numero_6 = QPushButton(self.calculadora)
        self.numero_6.setObjectName(u"numero_6")
        self.numero_6.setGeometry(QRect(150, 220, 71, 51))
        font = QFont()
        font.setBold(True)
        self.numero_6.setFont(font)
        self.numero_6.setFocusPolicy(Qt.NoFocus)
        self.numero_6.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_6.setCheckable(False)
        self.numero_6.setChecked(False)
        self.numero_1 = QPushButton(self.calculadora)
        self.numero_1.setObjectName(u"numero_1")
        self.numero_1.setGeometry(QRect(10, 170, 71, 51))
        self.numero_1.setFont(font)
        self.numero_1.setFocusPolicy(Qt.NoFocus)
        self.numero_1.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.numero_1.setCheckable(False)
        self.numero_1.setChecked(False)
        self.numero_4 = QPushButton(self.calculadora)
        self.numero_4.setObjectName(u"numero_4")
        self.numero_4.setGeometry(QRect(10, 220, 71, 51))
        self.numero_4.setFont(font)
        self.numero_4.setFocusPolicy(Qt.NoFocus)
        self.numero_4.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_4.setCheckable(False)
        self.numero_4.setChecked(False)
        self.numero_5 = QPushButton(self.calculadora)
        self.numero_5.setObjectName(u"numero_5")
        self.numero_5.setGeometry(QRect(80, 220, 71, 51))
        self.numero_5.setFont(font)
        self.numero_5.setFocusPolicy(Qt.NoFocus)
        self.numero_5.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_5.setCheckable(False)
        self.numero_5.setChecked(False)
        self.botao_apagar = QPushButton(self.calculadora)
        self.botao_apagar.setObjectName(u"botao_apagar")
        self.botao_apagar.setGeometry(QRect(220, 270, 71, 51))
        self.botao_apagar.setFont(font)
        self.botao_apagar.setFocusPolicy(Qt.NoFocus)
        self.botao_apagar.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #ff8a80;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}\n"
"font-size: 24px !important;")
        self.botao_apagar.setCheckable(False)
        self.botao_apagar.setChecked(False)
        self.toolButton_0 = QToolButton(self.calculadora)
        self.toolButton_0.setObjectName(u"toolButton_0")
        self.toolButton_0.setGeometry(QRect(10, 10, 21, 31))
        font1 = QFont()
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.toolButton_0.setFont(font1)
        self.toolButton_0.setTabletTracking(False)
        self.toolButton_0.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolButton_0.setStyleSheet(u"QToolButton:hover {\n"
"        color: #000;\n"
"        background-color: #e0e0e0;\n"
"        border-radius: 5px;\n"
"    }")
        self.toolButton_0.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.botao_decimal = QPushButton(self.calculadora)
        self.botao_decimal.setObjectName(u"botao_decimal")
        self.botao_decimal.setGeometry(QRect(150, 320, 71, 51))
        self.botao_decimal.setFont(font)
        self.botao_decimal.setFocusPolicy(Qt.NoFocus)
        self.botao_decimal.setAutoFillBackground(False)
        self.botao_decimal.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.botao_decimal.setCheckable(False)
        self.botao_decimal.setChecked(False)
        self.operador_menos = QPushButton(self.calculadora)
        self.operador_menos.setObjectName(u"operador_menos")
        self.operador_menos.setGeometry(QRect(220, 220, 71, 51))
        self.operador_menos.setFont(font)
        self.operador_menos.setFocusPolicy(Qt.NoFocus)
        self.operador_menos.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.operador_menos.setCheckable(False)
        self.operador_menos.setChecked(False)
        self.fonte_display = QLineEdit(self.calculadora)
        self.fonte_display.setObjectName(u"fonte_display")
        self.fonte_display.setGeometry(QRect(10, 80, 281, 71))
        self.fonte_display.setFont(font)
        self.fonte_display.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.fonte_display.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"    font-size: 48px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}")
        self.fonte_display.setReadOnly(True)
        self.operador_percentagem = QPushButton(self.calculadora)
        self.operador_percentagem.setObjectName(u"operador_percentagem")
        self.operador_percentagem.setGeometry(QRect(150, 370, 71, 51))
        self.operador_percentagem.setFont(font)
        self.operador_percentagem.setFocusPolicy(Qt.NoFocus)
        self.operador_percentagem.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.operador_percentagem.setCheckable(False)
        self.operador_percentagem.setChecked(False)
        self.numero_9 = QPushButton(self.calculadora)
        self.numero_9.setObjectName(u"numero_9")
        self.numero_9.setGeometry(QRect(150, 270, 71, 51))
        self.numero_9.setFont(font)
        self.numero_9.setFocusPolicy(Qt.NoFocus)
        self.numero_9.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_9.setCheckable(False)
        self.numero_9.setChecked(False)
        self.operador_dividir = QPushButton(self.calculadora)
        self.operador_dividir.setObjectName(u"operador_dividir")
        self.operador_dividir.setGeometry(QRect(10, 370, 71, 51))
        self.operador_dividir.setFont(font)
        self.operador_dividir.setFocusPolicy(Qt.NoFocus)
        self.operador_dividir.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.operador_dividir.setCheckable(False)
        self.operador_dividir.setChecked(False)
        self.numero_8 = QPushButton(self.calculadora)
        self.numero_8.setObjectName(u"numero_8")
        self.numero_8.setGeometry(QRect(80, 270, 71, 51))
        self.numero_8.setFont(font)
        self.numero_8.setFocusPolicy(Qt.NoFocus)
        self.numero_8.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_8.setCheckable(False)
        self.numero_8.setChecked(False)
        self.operador_mais = QPushButton(self.calculadora)
        self.operador_mais.setObjectName(u"operador_mais")
        self.operador_mais.setGeometry(QRect(220, 170, 71, 51))
        self.operador_mais.setFont(font)
        self.operador_mais.setFocusPolicy(Qt.NoFocus)
        self.operador_mais.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.operador_mais.setCheckable(False)
        self.operador_mais.setChecked(False)
        self.botao_sinal = QPushButton(self.calculadora)
        self.botao_sinal.setObjectName(u"botao_sinal")
        self.botao_sinal.setGeometry(QRect(80, 370, 71, 51))
        self.botao_sinal.setFont(font)
        self.botao_sinal.setFocusPolicy(Qt.NoFocus)
        self.botao_sinal.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.botao_sinal.setCheckable(False)
        self.botao_sinal.setChecked(False)
        self.numero_0 = QPushButton(self.calculadora)
        self.numero_0.setObjectName(u"numero_0")
        self.numero_0.setGeometry(QRect(80, 320, 71, 51))
        self.numero_0.setFont(font)
        self.numero_0.setFocusPolicy(Qt.NoFocus)
        self.numero_0.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_0.setCheckable(False)
        self.numero_0.setChecked(False)
        self.numero_7 = QPushButton(self.calculadora)
        self.numero_7.setObjectName(u"numero_7")
        self.numero_7.setGeometry(QRect(10, 270, 71, 51))
        self.numero_7.setFont(font)
        self.numero_7.setFocusPolicy(Qt.NoFocus)
        self.numero_7.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_7.setCheckable(False)
        self.numero_7.setChecked(False)
        self.numero_2 = QPushButton(self.calculadora)
        self.numero_2.setObjectName(u"numero_2")
        self.numero_2.setGeometry(QRect(80, 170, 71, 51))
        self.numero_2.setFont(font)
        self.numero_2.setFocusPolicy(Qt.NoFocus)
        self.numero_2.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_2.setCheckable(False)
        self.numero_2.setChecked(False)
        self.botao_apagar_tudo = QPushButton(self.calculadora)
        self.botao_apagar_tudo.setObjectName(u"botao_apagar_tudo")
        self.botao_apagar_tudo.setGeometry(QRect(220, 320, 71, 51))
        self.botao_apagar_tudo.setFont(font)
        self.botao_apagar_tudo.setFocusPolicy(Qt.NoFocus)
        self.botao_apagar_tudo.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(235, 50, 10);;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.botao_apagar_tudo.setCheckable(False)
        self.botao_apagar_tudo.setChecked(False)
        self.botao_resultado = QPushButton(self.calculadora)
        self.botao_resultado.setObjectName(u"botao_resultado")
        self.botao_resultado.setGeometry(QRect(220, 370, 71, 51))
        self.botao_resultado.setFont(font)
        self.botao_resultado.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.botao_resultado.setCheckable(False)
        self.botao_resultado.setChecked(False)
        self.numero_3 = QPushButton(self.calculadora)
        self.numero_3.setObjectName(u"numero_3")
        self.numero_3.setGeometry(QRect(150, 170, 71, 51))
        self.numero_3.setFont(font)
        self.numero_3.setFocusPolicy(Qt.NoFocus)
        self.numero_3.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_3.setCheckable(False)
        self.numero_3.setChecked(False)
        self.operador_multiplicar = QPushButton(self.calculadora)
        self.operador_multiplicar.setObjectName(u"operador_multiplicar")
        self.operador_multiplicar.setEnabled(True)
        self.operador_multiplicar.setGeometry(QRect(10, 320, 71, 51))
        self.operador_multiplicar.setFont(font)
        self.operador_multiplicar.setMouseTracking(False)
        self.operador_multiplicar.setFocusPolicy(Qt.NoFocus)
        self.operador_multiplicar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff5032;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.operador_multiplicar.setCheckable(False)
        self.operador_multiplicar.setChecked(False)
        self.operador_multiplicar.setAutoDefault(True)
        self.operador_multiplicar.setFlat(False)
        self.label_calculadora = QLabel(self.calculadora)
        self.label_calculadora.setObjectName(u"label_calculadora")
        self.label_calculadora.setGeometry(QRect(40, 10, 141, 31))
        self.stackedWidget.addWidget(self.calculadora)
        self.temperaturas = QWidget()
        self.temperaturas.setObjectName(u"temperaturas")
        self.combo_distancia_1 = QComboBox(self.temperaturas)
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.addItem("")
        self.combo_distancia_1.setObjectName(u"combo_distancia_1")
        self.combo_distancia_1.setGeometry(QRect(10, 130, 121, 31))
        font2 = QFont()
        self.combo_distancia_1.setFont(font2)
        self.combo_distancia_1.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 11px;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.distancia_1 = QLineEdit(self.temperaturas)
        self.distancia_1.setObjectName(u"distancia_1")
        self.distancia_1.setGeometry(QRect(10, 60, 281, 61))
        self.distancia_1.setFont(font)
        self.distancia_1.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: #000;\n"
"    font-size: 42px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #ff7052;\n"
"}")
        self.label_distancias = QLabel(self.temperaturas)
        self.label_distancias.setObjectName(u"label_distancias")
        self.label_distancias.setGeometry(QRect(40, 10, 141, 31))
        self.distancia_2 = QLineEdit(self.temperaturas)
        self.distancia_2.setObjectName(u"distancia_2")
        self.distancia_2.setGeometry(QRect(10, 170, 281, 61))
        self.distancia_2.setFont(font)
        self.distancia_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: #000;\n"
"    font-size: 42px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #ff7052;\n"
"}")
        self.combo_distancia_2 = QComboBox(self.temperaturas)
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.addItem("")
        self.combo_distancia_2.setObjectName(u"combo_distancia_2")
        self.combo_distancia_2.setGeometry(QRect(10, 240, 121, 31))
        self.combo_distancia_2.setStyleSheet(u"QComboBox {\n"
"        background-color: white;\n"
"        color: #333;\n"
"        font-size: 11px;\n"
"        border: 2px solid #ddd;\n"
"        border-radius: 8px;\n"
"        padding: 5px 10px;\n"
"    }\n"
"    QComboBox::drop-down {\n"
"        border: none;\n"
"        width: 25px;\n"
"    }\n"
"    QComboBox::down-arrow {\n"
"        image: url(arrow.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"    }")
        self.numero_0_dist = QPushButton(self.temperaturas)
        self.numero_0_dist.setObjectName(u"numero_0_dist")
        self.numero_0_dist.setGeometry(QRect(220, 330, 71, 51))
        self.numero_0_dist.setFont(font)
        self.numero_0_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_0_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_0_dist.setCheckable(False)
        self.numero_0_dist.setChecked(False)
        self.numero_6_dist = QPushButton(self.temperaturas)
        self.numero_6_dist.setObjectName(u"numero_6_dist")
        self.numero_6_dist.setGeometry(QRect(150, 330, 71, 51))
        self.numero_6_dist.setFont(font)
        self.numero_6_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_6_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_6_dist.setCheckable(False)
        self.numero_6_dist.setChecked(False)
        self.numero_7_dist = QPushButton(self.temperaturas)
        self.numero_7_dist.setObjectName(u"numero_7_dist")
        self.numero_7_dist.setGeometry(QRect(10, 380, 71, 51))
        self.numero_7_dist.setFont(font)
        self.numero_7_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_7_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_7_dist.setCheckable(False)
        self.numero_7_dist.setChecked(False)
        self.numero_1_dist = QPushButton(self.temperaturas)
        self.numero_1_dist.setObjectName(u"numero_1_dist")
        self.numero_1_dist.setGeometry(QRect(10, 280, 71, 51))
        self.numero_1_dist.setFont(font)
        self.numero_1_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_1_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_1_dist.setCheckable(False)
        self.numero_1_dist.setChecked(False)
        self.numero_3_dist = QPushButton(self.temperaturas)
        self.numero_3_dist.setObjectName(u"numero_3_dist")
        self.numero_3_dist.setGeometry(QRect(150, 280, 71, 51))
        self.numero_3_dist.setFont(font)
        self.numero_3_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_3_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_3_dist.setCheckable(False)
        self.numero_3_dist.setChecked(False)
        self.numero_9_dist = QPushButton(self.temperaturas)
        self.numero_9_dist.setObjectName(u"numero_9_dist")
        self.numero_9_dist.setGeometry(QRect(150, 380, 71, 51))
        self.numero_9_dist.setFont(font)
        self.numero_9_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_9_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_9_dist.setCheckable(False)
        self.numero_9_dist.setChecked(False)
        self.numero_2_dist = QPushButton(self.temperaturas)
        self.numero_2_dist.setObjectName(u"numero_2_dist")
        self.numero_2_dist.setGeometry(QRect(80, 280, 71, 51))
        self.numero_2_dist.setFont(font)
        self.numero_2_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_2_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_2_dist.setCheckable(False)
        self.numero_2_dist.setChecked(False)
        self.numero_4_dist = QPushButton(self.temperaturas)
        self.numero_4_dist.setObjectName(u"numero_4_dist")
        self.numero_4_dist.setGeometry(QRect(10, 330, 71, 51))
        self.numero_4_dist.setFont(font)
        self.numero_4_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_4_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_4_dist.setCheckable(False)
        self.numero_4_dist.setChecked(False)
        self.numero_8_dist = QPushButton(self.temperaturas)
        self.numero_8_dist.setObjectName(u"numero_8_dist")
        self.numero_8_dist.setGeometry(QRect(80, 380, 71, 51))
        self.numero_8_dist.setFont(font)
        self.numero_8_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_8_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_8_dist.setCheckable(False)
        self.numero_8_dist.setChecked(False)
        self.numero_5_dist = QPushButton(self.temperaturas)
        self.numero_5_dist.setObjectName(u"numero_5_dist")
        self.numero_5_dist.setGeometry(QRect(80, 330, 71, 51))
        self.numero_5_dist.setFont(font)
        self.numero_5_dist.setFocusPolicy(Qt.NoFocus)
        self.numero_5_dist.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: #333;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"}")
        self.numero_5_dist.setCheckable(False)
        self.numero_5_dist.setChecked(False)
        self.botao_apagar_dist = QPushButton(self.temperaturas)
        self.botao_apagar_dist.setObjectName(u"botao_apagar_dist")
        self.botao_apagar_dist.setGeometry(QRect(220, 280, 71, 51))
        self.botao_apagar_dist.setFont(font)
        self.botao_apagar_dist.setFocusPolicy(Qt.NoFocus)
        self.botao_apagar_dist.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #ff8a80;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}\n"
"font-size: 24px !important;")
        self.botao_apagar_dist.setCheckable(False)
        self.botao_apagar_dist.setChecked(False)
        self.botao_apagar_tudo_dist = QPushButton(self.temperaturas)
        self.botao_apagar_tudo_dist.setObjectName(u"botao_apagar_tudo_dist")
        self.botao_apagar_tudo_dist.setGeometry(QRect(220, 380, 71, 51))
        self.botao_apagar_tudo_dist.setFont(font)
        self.botao_apagar_tudo_dist.setFocusPolicy(Qt.NoFocus)
        self.botao_apagar_tudo_dist.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(235, 50, 10);;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    margin: 2px;  /* \u2190 adiciona isto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff7052;\n"
"}")
        self.botao_apagar_tudo_dist.setCheckable(False)
        self.botao_apagar_tudo_dist.setChecked(False)
        self.toolButton_1 = QToolButton(self.temperaturas)
        self.toolButton_1.setObjectName(u"toolButton_1")
        self.toolButton_1.setGeometry(QRect(10, 10, 21, 31))
        self.toolButton_1.setFont(font2)
        self.toolButton_1.setTabletTracking(False)
        self.toolButton_1.setStyleSheet(u"QToolButton:hover {\n"
"        color: #000;\n"
"        background-color: #e0e0e0;\n"
"        border-radius: 5px;\n"
"    }\n"
" ")
        self.stackedWidget.addWidget(self.temperaturas)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)
        self.operador_multiplicar.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.numero_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.numero_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.numero_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.numero_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.botao_apagar.setText(QCoreApplication.translate("Dialog", u"\u27f5", None))
        self.toolButton_0.setText(QCoreApplication.translate("Dialog", u"\u2630", None))
        self.botao_decimal.setText(QCoreApplication.translate("Dialog", u".", None))
        self.operador_menos.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.fonte_display.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.operador_percentagem.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.numero_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.operador_dividir.setText(QCoreApplication.translate("Dialog", u"\u00f7", None))
        self.numero_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.operador_mais.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.botao_sinal.setText(QCoreApplication.translate("Dialog", u"+/-", None))
        self.numero_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.numero_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.numero_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.botao_apagar_tudo.setText(QCoreApplication.translate("Dialog", u"CE", None))
        self.botao_resultado.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.numero_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.operador_multiplicar.setText(QCoreApplication.translate("Dialog", u"\u2715", None))
        self.label_calculadora.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Calculadora</span></p></body></html>", None))
        self.combo_distancia_1.setItemText(0, QCoreApplication.translate("Dialog", u"Metros", None))
        self.combo_distancia_1.setItemText(1, QCoreApplication.translate("Dialog", u"Cent\u00edmetros", None))
        self.combo_distancia_1.setItemText(2, QCoreApplication.translate("Dialog", u"Mil\u00edmetros", None))
        self.combo_distancia_1.setItemText(3, QCoreApplication.translate("Dialog", u"Milhas", None))
        self.combo_distancia_1.setItemText(4, QCoreApplication.translate("Dialog", u"Quil\u00f3metros", None))
        self.combo_distancia_1.setItemText(5, QCoreApplication.translate("Dialog", u"Polegadas", None))
        self.combo_distancia_1.setItemText(6, QCoreApplication.translate("Dialog", u"P\u00e9s", None))

        self.combo_distancia_1.setCurrentText(QCoreApplication.translate("Dialog", u"Metros", None))
        self.distancia_1.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_distancias.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Dist\u00e2ncias</span></p></body></html>", None))
        self.distancia_2.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.combo_distancia_2.setItemText(0, QCoreApplication.translate("Dialog", u"Cent\u00edmetros", None))
        self.combo_distancia_2.setItemText(1, QCoreApplication.translate("Dialog", u"Metros", None))
        self.combo_distancia_2.setItemText(2, QCoreApplication.translate("Dialog", u"Mil\u00edmetros", None))
        self.combo_distancia_2.setItemText(3, QCoreApplication.translate("Dialog", u"Milhas", None))
        self.combo_distancia_2.setItemText(4, QCoreApplication.translate("Dialog", u"Quil\u00f3metros", None))
        self.combo_distancia_2.setItemText(5, QCoreApplication.translate("Dialog", u"Polegadas", None))
        self.combo_distancia_2.setItemText(6, QCoreApplication.translate("Dialog", u"P\u00e9s", None))

        self.numero_0_dist.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.numero_6_dist.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.numero_7_dist.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.numero_1_dist.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.numero_3_dist.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.numero_9_dist.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.numero_2_dist.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.numero_4_dist.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.numero_8_dist.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.numero_5_dist.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.botao_apagar_dist.setText(QCoreApplication.translate("Dialog", u"\u27f5", None))
        self.botao_apagar_tudo_dist.setText(QCoreApplication.translate("Dialog", u"CE", None))
        self.toolButton_1.setText(QCoreApplication.translate("Dialog", u"\u2630", None))
    # retranslateUi

