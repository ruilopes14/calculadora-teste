from PySide6.QtWidgets import QApplication, QLabel, QDialog, QLCDNumber
from calculadora_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QPixmap, QColor, QShortcut, QKeySequence, QFont, QFontDatabase
from PySide6.QtCore import Qt
import sys
import os



#setup janela
app = QApplication([])
janela = QDialog()
janela.setWindowTitle("Calculadora")
ui = Ui_Dialog()
ui.setupUi(janela)
janela.setWindowTitle("Calculadora")
janela.setWindowIcon(QIcon("Icon.ico"))
fonte = QFont("DS-Digital", 100)

fonte_id = QFontDatabase.addApplicationFont("DS-DIGIT.ttf")  # ou o nome exato do ficheiro

if getattr(sys, 'frozen', False):
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(sys._MEIPASS, 'PySide6', 'plugins', 'platforms')

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Carregar fonte
fonte_path = os.path.join(base_path, "DS-DIGIT.ttf")
fonte_id = QFontDatabase.addApplicationFont(fonte_path)

# Carregar ícone
icon_path = os.path.join(base_path, "Icon.ico")
janela.setWindowIcon(QIcon(icon_path))

# Debug - verifica qual fonte está realmente a usar


#variaveis globais
valor_atual = 0
operador = ""
resultado = 0
resultado_mostrado = False

#Operacoes
def adicao() :
    global valor_atual, operador, resultado, resultado_mostrado
    if operador != "" :
            resultado_mostrado = True
            segundo_valor = ui.lcd_number.value()
            resultado = (valor_atual) + (segundo_valor)
            ui.lcd_number.display((resultado))  
            operador = "+"
            valor_atual = resultado
            print(f" o operador é {operador} e o resultado mostrado {resultado_mostrado}")
            print (f"o primeiro resultado é {valor_atual} e o segundo é {segundo_valor}")
    else :
            valor_atual = ui.lcd_number.value()
            ui.lcd_number.display(0)
            operador = "+"

def subtracao() :
    global valor_atual, operador, resultado, resultado_mostrado 
    if operador != "" :
        resultado_mostrado = True
        segundo_valor = ui.lcd_number.value()
        resultado = (valor_atual) - (segundo_valor)
        ui.lcd_number.display((resultado))  
        operador = "-"
        valor_atual = resultado
    else :        
        valor_atual = ui.lcd_number.value()
        ui.lcd_number.display(0)
        operador = "-"


def multiplicacao() :
    global valor_atual, operador, resultado,resultado_mostrado 
    if operador != "" :
        resultado_mostrado = True
        segundo_valor = ui.lcd_number.value()
        resultado = (valor_atual) * (segundo_valor)
        ui.lcd_number.display((resultado))  
        operador = "*"
        valor_atual = resultado
    else :
        valor_atual = ui.lcd_number.value()
        ui.lcd_number.display(0)
        operador = "*"

def divisao() :
    global valor_atual, operador, resultado,resultado_mostrado 
    if operador != "" :
        resultado_mostrado = True
        segundo_valor = ui.lcd_number.value()
        resultado = (valor_atual) / (segundo_valor)
        ui.lcd_number.display((resultado))  
        operador = "/"
        valor_atual = resultado
    else :
        valor_atual = ui.lcd_number.value()
        ui.lcd_number.display(0)
        operador = "/"

#Botoes numeros 
def num_1() : 
    global resultado_mostrado, operador 
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 1
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 1
        ui.lcd_number.display(numero)
def num_2() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 2
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 2
        ui.lcd_number.display(numero)
def num_3() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 3
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 3
        ui.lcd_number.display(numero) 
def num_4() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 4
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 4
        ui.lcd_number.display(numero)

def num_5() :
    global resultado_mostrado, operador 
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 5
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 5
        ui.lcd_number.display(numero)

def num_6() :
    global resultado_mostrado, operador 
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 6
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 6
        ui.lcd_number.display(numero)

def num_7() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 7
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 7
        ui.lcd_number.display(numero)

def num_8() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 8
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 8
        ui.lcd_number.display(numero)

def num_9() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 9
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 9
        ui.lcd_number.display(numero)

def num_0() : 
    global resultado_mostrado, operador
    if resultado_mostrado :
        ui.lcd_number.display(0) 
        numero = ui.lcd_number.value() * 10 + 0
        ui.lcd_number.display(numero)
        resultado_mostrado = False

    else :
        numero = ui.lcd_number.value() * 10 + 0
        ui.lcd_number.display(numero)

def resultado() :
    global valor_atual, operador 
    segundo_valor = ui.lcd_number.value()
    if operador == "+" :
        resultado = (valor_atual) + (segundo_valor)
        ui.lcd_number.display((resultado))
        operador = ""
    elif operador == "-" :
        resultado = (valor_atual) - (segundo_valor)
        ui.lcd_number.display((resultado))
        operador = ""
    elif operador == "/" :
        resultado = (valor_atual) / (segundo_valor)
        ui.lcd_number.display((resultado))
        operador = ""
    elif operador == "*" :
        resultado = (valor_atual) * (segundo_valor)
        ui.lcd_number.display((resultado))
        operador = ""
    

def limpar_tudo () :
    global operador
    ui.lcd_number.display(0)
    operador = ""

def apagar () :
    apagar_digito = ui.lcd_number.value() // 10
    ui.lcd_number.display(apagar_digito)


def decimal () :
    print("!")

ui.botao_resultado.setDefault(True)

#conexões
ui.numero_1.clicked.connect(num_1)
ui.numero_2.clicked.connect(num_2)
ui.numero_3.clicked.connect(num_3)
ui.numero_4.clicked.connect(num_4)
ui.numero_5.clicked.connect(num_5)
ui.numero_6.clicked.connect(num_6)
ui.numero_7.clicked.connect(num_7)
ui.numero_8.clicked.connect(num_8)
ui.numero_9.clicked.connect(num_9)
ui.numero_0.clicked.connect(num_0)
ui.botao_apagar.clicked.connect(apagar)
ui.botao_decimal.clicked.connect(decimal)
ui.operador_mais.clicked.connect (adicao)
ui.operador_menos.clicked.connect(subtracao)
ui.operador_dividir.clicked.connect(divisao)
ui.operador_multiplicar.clicked.connect(multiplicacao)
ui.botao_resultado.clicked.connect(resultado)
ui.botao_apagar_tudo.clicked.connect(limpar_tudo)
QShortcut(QKeySequence("1"), janela).activated.connect(num_1)
QShortcut(QKeySequence("2"), janela).activated.connect(num_2)
QShortcut(QKeySequence("3"), janela).activated.connect(num_3)
QShortcut(QKeySequence("4"), janela).activated.connect(num_4)
QShortcut(QKeySequence("5"), janela).activated.connect(num_5)
QShortcut(QKeySequence("6"), janela).activated.connect(num_6)
QShortcut(QKeySequence("7"), janela).activated.connect(num_7)
QShortcut(QKeySequence("8"), janela).activated.connect(num_8)
QShortcut(QKeySequence("9"), janela).activated.connect(num_9)
QShortcut(QKeySequence("0"), janela).activated.connect(num_0)
QShortcut(QKeySequence("+"), janela).activated.connect(adicao)
QShortcut(QKeySequence("-"), janela).activated.connect(subtracao)
QShortcut(QKeySequence("/"), janela).activated.connect(divisao)
QShortcut(QKeySequence("*"), janela).activated.connect(multiplicacao)
QShortcut(QKeySequence("backspace"), janela).activated.connect(apagar)
QShortcut(QKeySequence("."), janela).activated.connect(decimal)


janela.show()
app.exec()