# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_do_list.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(648, 482)
        Dialog.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));")
        self.input_tarefa = QLineEdit(Dialog)
        self.input_tarefa.setObjectName(u"input_tarefa")
        self.input_tarefa.setGeometry(QRect(90, 100, 381, 31))
        self.botao_adicionar = QPushButton(Dialog)
        self.botao_adicionar.setObjectName(u"botao_adicionar")
        self.botao_adicionar.setGeometry(QRect(500, 100, 121, 31))
        self.lista_tarefas = QListWidget(Dialog)
        self.lista_tarefas.setObjectName(u"lista_tarefas")
        self.lista_tarefas.setGeometry(QRect(90, 170, 381, 251))
        self.botao_apagar = QPushButton(Dialog)
        self.botao_apagar.setObjectName(u"botao_apagar")
        self.botao_apagar.setGeometry(QRect(500, 320, 121, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 261, 51))
        self.label_erro = QLabel(Dialog)
        self.label_erro.setObjectName(u"label_erro")
        self.label_erro.setGeometry(QRect(100, 70, 341, 31))
        self.erro_completar = QLabel(Dialog)
        self.erro_completar.setObjectName(u"erro_completar")
        self.erro_completar.setGeometry(QRect(100, 150, 311, 16))
        self.apagar_tudo = QPushButton(Dialog)
        self.apagar_tudo.setObjectName(u"apagar_tudo")
        self.apagar_tudo.setGeometry(QRect(500, 370, 121, 31))
        self.editar_tarefa = QPushButton(Dialog)
        self.editar_tarefa.setObjectName(u"editar_tarefa")
        self.editar_tarefa.setGeometry(QRect(500, 190, 121, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.botao_adicionar.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.botao_apagar.setText(QCoreApplication.translate("Dialog", u"Apagar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u2705Lista de Tarefas</span></p></body></html>", None))
        self.label_erro.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:72pt;\"><br/></span></p></body></html>", None))
        self.erro_completar.setText("")
        self.apagar_tudo.setText(QCoreApplication.translate("Dialog", u"Apagar tudo", None))
        self.editar_tarefa.setText(QCoreApplication.translate("Dialog", u"Editar Tarefa", None))
    # retranslateUi

