from PySide6.QtWidgets import QApplication, QDialog
from calculadora_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QShortcut, QKeySequence, QFont, QFontDatabase
from PySide6.QtCore import Qt
import sys
import os



#setup janela
app = QApplication([])
janela = QDialog()
janela.setWindowTitle("Calculadora")
ui = Ui_Dialog()
ui.setupUi(janela)
janela.setWindowIcon(QIcon("icon.ico"))
janela.setStyleSheet("background-color: #f0f0f0;") 

def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)

if getattr(sys, 'frozen', False):
    # Executando como .exe
    base_path = sys._MEIPASS
else:
    # Executando como script Python
    base_path = os.path.dirname(__file__)

janela.setWindowIcon(QIcon(resource_path("icon.ico")))


# Aplicar fonte ao display
fonte_id = QFontDatabase.addApplicationFont(resource_path("DS-DIGIT.ttf"))
familias = QFontDatabase.applicationFontFamilies(fonte_id)
nome_fonte = familias[0]
fonte = QFont(nome_fonte)
ui.fonte_display.setStyleSheet("font-size: 72px;")
fonte.setWeight(QFont.Bold)
ui.fonte_display.setFont(fonte)
ui.fonte_display.setAlignment(Qt.AlignRight)
ui.fonte_display.setText("0")

print(f"Fonte no display: {ui.fonte_display.font().family()}")

#variaveis globais
valor_atual = 0
operador = ""
resultado = 0
resultado_mostrado = False
segundo_valor = ""
texto_atual = ""

#Operacoes

def calcular():
    global valor_atual, operador
    segundo_valor = ui.fonte_display.text()
    
    if operador == "+":
        resultado = float(valor_atual) + float(segundo_valor)
    elif operador == "-":
        resultado = float(valor_atual) - float(segundo_valor)
    elif operador == "*":
        resultado = float(valor_atual) * float(segundo_valor)
    elif operador == "/":
        resultado = float(valor_atual) / float(segundo_valor)
    else:
        return  
    
    resultado = round(resultado, 10)

    if resultado % 1 == 0:
        ui.fonte_display.setText(str(int(resultado)))
    else:
        ui.fonte_display.setText(str(resultado))
    
    valor_atual = resultado
    return resultado

def adicao() :
    global valor_atual, operador, resultado, resultado_mostrado,segundo_valor,  texto_atual
    
    if operador != "":
        calcular() 
        operador = "+"
        resultado_mostrado = True
    else :

             valor_atual = ui.fonte_display.text()
             ui.fonte_display.setText("0")
             texto_atual = "0"
             operador = "+"
             resultado_mostrado = False
             print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
            
            

def subtracao() :
    global valor_atual, operador, resultado, resultado_mostrado, texto_atual
    if operador != "":
        
        calcular() 
        resultado_mostrado = True
        operador = "-"
        print(f" o operador é {operador} e o resultado mostrado {resultado_mostrado}")
        print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
    else :
            valor_atual = ui.fonte_display.text()
            ui.fonte_display.setText("0")
            operador = "-"
            resultado_mostrado = False


def multiplicacao() :
    global valor_atual, operador, resultado,resultado_mostrado, texto_atual 
    if operador != "":
        calcular() 
        operador = "*"
        resultado_mostrado = True
        print(f" o operador é {operador} e o resultado mostrado {resultado_mostrado}")
        print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
    else :
            valor_atual = ui.fonte_display.text()
            ui.fonte_display.setText("0")
            operador = "*"
            resultado_mostrado = False

def divisao() :
    global valor_atual, operador, resultado,resultado_mostrado, texto_atual
    if operador != "":
        calcular() 
        operador = "/"
        resultado_mostrado = True
        print(f" o operador é {operador} e o resultado mostrado {resultado_mostrado}")
        print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
    else :
            valor_atual = ui.fonte_display.text()
            ui.fonte_display.setText("0")
            operador = "/"
            resultado_mostrado = False

def percentagem() :
    global valor_atual, segundo_valor, texto_atual
    if operador != "" : 
        texto_atual = ui.fonte_display.text() 
        segundo_valor = float(valor_atual) * (float(texto_atual) / 100)
        if  segundo_valor % 1 == 0 : 
            segundo_valor= int(segundo_valor)
            ui.fonte_display.setText(str(segundo_valor))
            print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
        else : 
            ui.fonte_display.setText(str(segundo_valor))
    else : 
        pass
#Numeros
def numeros(num) : 
    global resultado_mostrado, operador, texto_atual, segundo_valor, valor_atual
    if ui.fonte_display.text() == "0" :
        print(f"[ANTES CLEAR] display = '{ui.fonte_display.text()}'")
        ui.fonte_display.clear()
        print(f"[DEPOIS CLEAR] display = '{ui.fonte_display.text()}'")
        ui.fonte_display.setText(str(num))
        print(f"[DEPOIS setText] display = '{ui.fonte_display.text()}'")
        texto_atual = ui.fonte_display.text()
        print(f"[FINAL] texto_atual = '{texto_atual}'")
        print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
        
    else :
         
         
        if resultado_mostrado:
            ui.fonte_display.setText(str(num))
            texto_atual = ui.fonte_display.text() 
            resultado_mostrado = False
            print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
        else:
            ui.fonte_display.setText(texto_atual + str(num))
            texto_atual = ui.fonte_display.text()
            print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
            print(f"resultado_mostrado = {resultado_mostrado}, num = {num}")                        
        
def sinal () : 
    global texto_atual
    texto_atual = float(ui.fonte_display.text())
    if texto_atual % 1 == 0:
        sinal = int(texto_atual) * -1
    else:
        sinal = float(texto_atual) * -1

    ui.fonte_display.setText(str(sinal))
    print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )


def resultado() :
    global valor_atual, operador, resultado_mostrado, texto_atual
    segundo_valor = ui.fonte_display.text()
    print(f"[RESULTADO] valor_atual = {valor_atual}, segundo_valor = {segundo_valor}")
    if operador == "+" :
        resultado = float(valor_atual) + float(segundo_valor)
        resultado = round(resultado, 10)
        if resultado % 1 == 0:  
            ui.fonte_display.setText(str(int(resultado)))
            resultado_mostrado = True
            operador = ""
            print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
        else:
            ui.fonte_display.setText(str(resultado))
            resultado_mostrado = True
            operador = ""
    elif operador == "-" :
        resultado = float(valor_atual) - float(segundo_valor)
        resultado = round(resultado, 10)
        if resultado % 1 == 0:  
            ui.fonte_display.setText(str(int(resultado)))
            resultado_mostrado = True
            operador = ""
        else:
            ui.fonte_display.setText(str(resultado))
            resultado_mostrado = True
            operador = ""
    elif operador == "*" :
        resultado = float(valor_atual) * float(segundo_valor)
        resultado = round(resultado, 10)
        if resultado % 1 == 0:  
            ui.fonte_display.setText(str(int(resultado)))
            resultado_mostrado = True
            operador = ""
        else:
            ui.fonte_display.setText(str(resultado))
            resultado_mostrado = True
            operador = ""
    elif operador == "/" :
        resultado = float(valor_atual) / float(segundo_valor)
        resultado = round(resultado, 10)
        if resultado % 1 == 0:  
            ui.fonte_display.setText(str(int(resultado)))
            resultado_mostrado = True
            operador = ""
        else:
            ui.fonte_display.setText(str(resultado))
            resultado_mostrado = True
            operador = ""
    

def limpar_tudo () :
    global operador, valor_atual, segundo_valor, texto_atual,resultado_mostrado
    ui.fonte_display.setText("0")
    operador = ""
    valor_atual = "0"
    segundo_valor = "0"
    texto_atual = "0"
    ecra = ui.fonte_display.text()
    print(f"o primeiro valor é {valor_atual} e o segundo é {segundo_valor}")
    print(f"o texto atual é {ecra}")
    resultado_mostrado = False

def apagar () :
    global texto_atual
    texto_atual = ui.fonte_display.text() 
    ui.fonte_display.setText(texto_atual [:-1] )
    texto_atual= ui.fonte_display.text()
    
    print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )

    


def decimal () :
    global texto_atual, valor_atual, segundo_valor,  resultado_mostrado
    texto_atual = ui.fonte_display.text()
    if "." not in texto_atual :
        ui.fonte_display.setText(str(texto_atual) + str("."))
        texto_atual = ui.fonte_display.text()
        print(f"valor atual é {valor_atual}\n o segundo valor é {segundo_valor}\n  e o texto no ecra é {texto_atual} " )
        resultado_mostrado =   False
    else :
        pass                            

ui.botao_resultado.setDefault(True)

#conexões
ui.numero_1.clicked.connect(lambda: numeros(1))
ui.numero_2.clicked.connect(lambda: numeros(2))
ui.numero_3.clicked.connect(lambda: numeros(3))
ui.numero_4.clicked.connect(lambda: numeros(4))
ui.numero_5.clicked.connect(lambda: numeros(5))
ui.numero_6.clicked.connect(lambda: numeros(6))
ui.numero_7.clicked.connect(lambda: numeros(7))
ui.numero_8.clicked.connect(lambda: numeros(8))
ui.numero_9.clicked.connect(lambda: numeros(9))
ui.numero_0.clicked.connect(lambda: numeros(0))
ui.botao_apagar.clicked.connect(apagar)
ui.botao_decimal.clicked.connect(decimal)
ui.operador_mais.clicked.connect (adicao)
ui.operador_menos.clicked.connect(subtracao)
ui.operador_dividir.clicked.connect(divisao)
ui.operador_multiplicar.clicked.connect(multiplicacao)
ui.botao_resultado.clicked.connect(resultado)
ui.botao_apagar_tudo.clicked.connect(limpar_tudo)
ui.operador_percentagem.clicked.connect(percentagem) 
ui.botao_sinal.clicked.connect(sinal)

QShortcut(QKeySequence("1"), janela).activated.connect(lambda: numeros(1))
QShortcut(QKeySequence("2"), janela).activated.connect(lambda: numeros(2))
QShortcut(QKeySequence("3"), janela).activated.connect(lambda:numeros(3))
QShortcut(QKeySequence("4"), janela).activated.connect(lambda:numeros(4))
QShortcut(QKeySequence("5"), janela).activated.connect(lambda:numeros(5))
QShortcut(QKeySequence("6"), janela).activated.connect(lambda:numeros(6))
QShortcut(QKeySequence("7"), janela).activated.connect(lambda:numeros(7))
QShortcut(QKeySequence("8"), janela).activated.connect(lambda:numeros(8))
QShortcut(QKeySequence("9"), janela).activated.connect(lambda:numeros(9))
QShortcut(QKeySequence("0"), janela).activated.connect(lambda:numeros(0))
QShortcut(QKeySequence("+"), janela).activated.connect(adicao)
QShortcut(QKeySequence("-"), janela).activated.connect(subtracao)
QShortcut(QKeySequence("/"), janela).activated.connect(divisao)
QShortcut(QKeySequence("*"), janela).activated.connect(multiplicacao)
QShortcut(QKeySequence("backspace"), janela).activated.connect(apagar)
QShortcut(QKeySequence("."), janela).activated.connect(decimal)
QShortcut(QKeySequence("Delete"), janela).activated.connect(limpar_tudo)

janela.show()
app.exec()