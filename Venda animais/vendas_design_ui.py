# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vendas_design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(479, 352)
        self.label_titulo = QLabel(Dialog)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(10, 10, 241, 31))
        self.Tem_experiencia = QLabel(Dialog)
        self.Tem_experiencia.setObjectName(u"Tem_experiencia")
        self.Tem_experiencia.setGeometry(QRect(20, 110, 121, 21))
        self.Tem_espaco = QLabel(Dialog)
        self.Tem_espaco.setObjectName(u"Tem_espaco")
        self.Tem_espaco.setGeometry(QRect(20, 170, 121, 21))
        self.mostrar_resultado = QTextEdit(Dialog)
        self.mostrar_resultado.setObjectName(u"mostrar_resultado")
        self.mostrar_resultado.setGeometry(QRect(170, 250, 231, 81))
        self.Botao_verificar = QPushButton(Dialog)
        self.Botao_verificar.setObjectName(u"Botao_verificar")
        self.Botao_verificar.setGeometry(QRect(10, 250, 141, 41))
        self.botao_opcoes = QPushButton(Dialog)
        self.botao_opcoes.setObjectName(u"botao_opcoes")
        self.botao_opcoes.setGeometry(QRect(10, 300, 141, 31))
        self.foto = QLabel(Dialog)
        self.foto.setObjectName(u"foto")
        self.foto.setGeometry(QRect(220, 60, 171, 151))
        self.foto.setMouseTracking(False)
        self.foto.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
        self.foto.setFrameShape(QFrame.NoFrame)
        self.foto.setFrameShadow(QFrame.Plain)
        self.foto.setLineWidth(0)
        self.foto.setMidLineWidth(0)
        self.foto.setTextFormat(Qt.RichText)
        self.foto.setPixmap(QPixmap(u"image.jpg"))
        self.foto.setScaledContents(True)
        self.foto.setWordWrap(False)
        self.botao_limpar = QPushButton(Dialog)
        self.botao_limpar.setObjectName(u"botao_limpar")
        self.botao_limpar.setGeometry(QRect(410, 280, 61, 31))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 131, 61))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}")
        self.sim_licenca = QRadioButton(self.groupBox)
        self.sim_licenca.setObjectName(u"sim_licenca")
        self.sim_licenca.setGeometry(QRect(10, 30, 82, 17))
        self.nao_licenca = QRadioButton(self.groupBox)
        self.nao_licenca.setObjectName(u"nao_licenca")
        self.nao_licenca.setGeometry(QRect(80, 30, 82, 17))
        self.Tem_licenca = QLabel(self.groupBox)
        self.Tem_licenca.setObjectName(u"Tem_licenca")
        self.Tem_licenca.setGeometry(QRect(10, 0, 81, 21))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 131, 41))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}")
        self.sim_experiencia = QRadioButton(self.groupBox_2)
        self.sim_experiencia.setObjectName(u"sim_experiencia")
        self.sim_experiencia.setGeometry(QRect(10, 10, 82, 17))
        self.sim_experiencia.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}")
        self.nao_experiencia = QRadioButton(self.groupBox_2)
        self.nao_experiencia.setObjectName(u"nao_experiencia")
        self.nao_experiencia.setGeometry(QRect(80, 10, 82, 17))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 200, 131, 41))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}")
        self.sim_espaco = QRadioButton(self.groupBox_3)
        self.sim_espaco.setObjectName(u"sim_espaco")
        self.sim_espaco.setGeometry(QRect(10, 0, 82, 17))
        self.nao_espaco = QRadioButton(self.groupBox_3)
        self.nao_espaco.setObjectName(u"nao_espaco")
        self.nao_espaco.setGeometry(QRect(80, 0, 82, 17))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        Dialog.setWindowFilePath("")
        self.label_titulo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Posso Vender animal?</span></p></body></html>", None))
        self.Tem_experiencia.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">T\u00eam experiencia?</span></p></body></html>", None))
        self.Tem_espaco.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">T\u00eam espa\u00e7o?</span></p></body></html>", None))
        self.Botao_verificar.setText(QCoreApplication.translate("Dialog", u"Verificar", None))
        self.botao_opcoes.setText(QCoreApplication.translate("Dialog", u"Ver op\u00e7\u00f5es disponiveis", None))
        self.foto.setText("")
        self.botao_limpar.setText(QCoreApplication.translate("Dialog", u"Limpar", None))
        self.groupBox.setTitle("")
        self.sim_licenca.setText(QCoreApplication.translate("Dialog", u"Siim", None))
        self.nao_licenca.setText(QCoreApplication.translate("Dialog", u"N\u00e3o", None))
        self.Tem_licenca.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">T\u00eam licen\u00e7a?</span></p></body></html>", None))
        self.groupBox_2.setTitle("")
        self.sim_experiencia.setText(QCoreApplication.translate("Dialog", u"Siim", None))
        self.nao_experiencia.setText(QCoreApplication.translate("Dialog", u"N\u00e3o", None))
        self.groupBox_3.setTitle("")
        self.sim_espaco.setText(QCoreApplication.translate("Dialog", u"Siim", None))
        self.nao_espaco.setText(QCoreApplication.translate("Dialog", u"N\u00e3o", None))
    # retranslateUi

