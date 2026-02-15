from PySide6.QtWidgets import QApplication, QDialog
from calculadora_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QShortcut, QKeySequence, QFont, QFontDatabase
from PySide6.QtCore import Qt
import sys
import os


def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)


# Setup janela
app = QApplication([])
janela = QDialog()
ui = Ui_Dialog()
ui.setupUi(janela)
janela.setWindowTitle("Calculadora")
janela.setWindowIcon(QIcon(resource_path("icon.ico")))
janela.setStyleSheet("background-color: #f0f0f0;")

# Aplicar fonte ao display
fonte_id = QFontDatabase.addApplicationFont(resource_path("DS-DIGIT.ttf"))
if fonte_id != -1:
    familias = QFontDatabase.applicationFontFamilies(fonte_id)
    fonte = QFont(familias[0])
else:
    fonte = QFont("Arial")

ui.fonte_display.setStyleSheet("font-size: 72px;")
fonte.setWeight(QFont.Bold)
ui.fonte_display.setFont(fonte)
ui.fonte_display.setAlignment(Qt.AlignRight)
ui.fonte_display.setText("0")

# Variáveis globais
valor_atual = 0
operador = ""
resultado_mostrado = False
texto_atual = ""


# Funções auxiliares
def mostrar_resultado(valor):
    """Mostra o valor no display, inteiro se possível."""
    valor = round(valor, 10)
    if valor % 1 == 0:
        ui.fonte_display.setText(str(int(valor)))
    else:
        ui.fonte_display.setText(str(valor))


def calcular():
    global valor_atual
    segundo_valor = ui.fonte_display.text()

    if operador == "+":
        res = float(valor_atual) + float(segundo_valor)
    elif operador == "-":
        res = float(valor_atual) - float(segundo_valor)
    elif operador == "*":
        res = float(valor_atual) * float(segundo_valor)
    elif operador == "/":
        if float(segundo_valor) == 0:
            ui.fonte_display.setText("Erro")
            return
        res = float(valor_atual) / float(segundo_valor)
    else:
        return

    mostrar_resultado(res)
    valor_atual = res


def operacao(op):
    global valor_atual, operador, resultado_mostrado, texto_atual
    if operador != "":
        calcular()
        resultado_mostrado = True
    else:
        valor_atual = ui.fonte_display.text()
        ui.fonte_display.setText("0")
        texto_atual = "0"
        resultado_mostrado = False
    operador = op


def percentagem():
    global valor_atual
    if operador != "":
        texto_atual = ui.fonte_display.text()
        resultado = float(valor_atual) * (float(texto_atual) / 100)
        mostrar_resultado(resultado)


def numeros(num):
    global resultado_mostrado, texto_atual
    if ui.fonte_display.text() == "0":
        ui.fonte_display.setText(str(num))
        texto_atual = str(num)
    elif resultado_mostrado:
        ui.fonte_display.setText(str(num))
        texto_atual = str(num)
        resultado_mostrado = False
    else:
        ui.fonte_display.setText(texto_atual + str(num))
        texto_atual = ui.fonte_display.text()


def sinal():
    global texto_atual
    valor = float(ui.fonte_display.text())
    valor = valor * -1
    if valor % 1 == 0:
        ui.fonte_display.setText(str(int(valor)))
    else:
        ui.fonte_display.setText(str(valor))
    texto_atual = ui.fonte_display.text()


def resultado():
    global valor_atual, operador, resultado_mostrado, texto_atual
    if operador == "":
        return
    calcular()
    resultado_mostrado = True
    texto_atual = ui.fonte_display.text()
    operador = ""


def limpar_tudo():
    global operador, valor_atual, texto_atual, resultado_mostrado
    ui.fonte_display.setText("0")
    operador = ""
    valor_atual = 0
    texto_atual = ""
    resultado_mostrado = False


def apagar():
    global texto_atual
    texto_atual = ui.fonte_display.text()[:-1]
    if texto_atual == "" or texto_atual == "-":
        texto_atual = "0"
    ui.fonte_display.setText(texto_atual)


def decimal():
    global texto_atual, resultado_mostrado
    texto_atual = ui.fonte_display.text()
    if "." not in texto_atual:
        ui.fonte_display.setText(texto_atual + ".")
        texto_atual = ui.fonte_display.text()
        resultado_mostrado = False


# Botão resultado com Enter
ui.botao_resultado.setDefault(True)

# Tirar foco dos outros botões
for botao in [ui.numero_0, ui.numero_1, ui.numero_2, ui.numero_3,
              ui.numero_4, ui.numero_5, ui.numero_6, ui.numero_7,
              ui.numero_8, ui.numero_9, ui.botao_apagar, ui.botao_decimal,
              ui.operador_mais, ui.operador_menos, ui.operador_dividir,
              ui.operador_multiplicar, ui.botao_apagar_tudo,
              ui.operador_percentagem, ui.botao_sinal]:
    botao.setFocusPolicy(Qt.NoFocus)

# Conexões botões
ui.numero_0.clicked.connect(lambda: numeros(0))
ui.numero_1.clicked.connect(lambda: numeros(1))
ui.numero_2.clicked.connect(lambda: numeros(2))
ui.numero_3.clicked.connect(lambda: numeros(3))
ui.numero_4.clicked.connect(lambda: numeros(4))
ui.numero_5.clicked.connect(lambda: numeros(5))
ui.numero_6.clicked.connect(lambda: numeros(6))
ui.numero_7.clicked.connect(lambda: numeros(7))
ui.numero_8.clicked.connect(lambda: numeros(8))
ui.numero_9.clicked.connect(lambda: numeros(9))
ui.botao_apagar.clicked.connect(apagar)
ui.botao_decimal.clicked.connect(decimal)
ui.operador_mais.clicked.connect(lambda: operacao("+"))
ui.operador_menos.clicked.connect(lambda: operacao("-"))
ui.operador_dividir.clicked.connect(lambda: operacao("/"))
ui.operador_multiplicar.clicked.connect(lambda: operacao("*"))
ui.botao_resultado.clicked.connect(resultado)
ui.botao_apagar_tudo.clicked.connect(limpar_tudo)
ui.operador_percentagem.clicked.connect(percentagem)
ui.botao_sinal.clicked.connect(sinal)

# Atalhos de teclado
for tecla, func in [("1", lambda: numeros(1)), ("2", lambda: numeros(2)),
                     ("3", lambda: numeros(3)), ("4", lambda: numeros(4)),
                     ("5", lambda: numeros(5)), ("6", lambda: numeros(6)),
                     ("7", lambda: numeros(7)), ("8", lambda: numeros(8)),
                     ("9", lambda: numeros(9)), ("0", lambda: numeros(0)),
                     ("+", lambda: operacao("+")), ("-", lambda: operacao("-")),
                     ("/", lambda: operacao("/")), ("*", lambda: operacao("*")),
                     ("backspace", apagar), (".", decimal), ("Delete", limpar_tudo)]:
    QShortcut(QKeySequence(tecla), janela).activated.connect(func)

janela.show()
app.exec()