from PySide6.QtWidgets import QApplication, QDialog, QMenu, QLineEdit
from calculadora_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QShortcut, QKeySequence, QFont, QFontDatabase, QDoubleValidator
from PySide6.QtCore import Qt, QLocale, QTimer
import sys
import os



#setup janela
app = QApplication([])
janela = QDialog()
ui = Ui_Dialog()
ui.setupUi(janela)
janela.setWindowTitle("Calculadora")
janela.setWindowIcon(QIcon("icon.ico"))
janela.setStyleSheet("background-color: #f0f0f0;") 

ui.combo_distancia_1.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_distancia_1.view().setStyleSheet("""
    QListView {
        background-color: white;
        border: 1px solid #ddd;
        outline: 0;
    }
    QListView::item {
        padding: 5px;
        outline: 0 ;                                  
    }
    QListView::item:selected {
        background-color: #ff7052;
        color: white;
    }
""")


ui.combo_distancia_2.view().setStyleSheet("""
    QListView {
        background-color: white;
        border: 1px solid #ddd;
        outline: 0;
    }
    QListView::item {
        padding: 5px;
    }
    QListView::item:selected {
        background-color: #ff7052;
        color: white;
    }
""")
ui.combo_distancia_2.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")

validator = QDoubleValidator()
validator.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
ui.distancia_1.setValidator(validator)
ui.distancia_2.setValidator(validator)

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
convertendo = False
ajustando_texto = False
menu = ""

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
        if float(segundo_valor) == 0 :
            ui.fonte_display.setText("ERRO")
            return 
        else :
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
    if operador == "":
        return
    calcular()
    resultado_mostrado = True
    texto_atual = ui.fonte_display.text()
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


def abrir_menu():
    global menu
    menu = QMenu(janela)
    menu.setStyleSheet("""
    QMenu {
        background-color: #f0f0f0;
        border: 2px solid #cccccc;
        border-radius: 8px;
        padding: 5px;
    }
    QMenu::item {
        padding: 8px 25px;
        border-radius: 5px;
        color: #333;
    }
    QMenu::item:selected {
    background-color: #ff5032;  /* laranja/vermelho como CE */
    color: white;
}
""")
    menu.addAction("Distâncias", ir_para_distancias)
    menu.addAction("Calculadora padrão", ir_para_calculadora)
    menu.exec(ui.toolButton_1.mapToGlobal(ui.toolButton_1.rect().bottomLeft()))


conversoes_distancia = {
    "Metros": 1,
    "Quilómetros": 1000,
    "Centímetros": 0.01,
    "Milhas": 1609.34,
    "Polegadas": 0.0254,
    "Pés": 0.3048,
    "Jardas": 0.9144,
    "Milímetros": 0.001
}

def converter_distancia1():
    global convertendo
    if convertendo:  
        return
    
    texto_distancia1 = ui.distancia_1.text()
    
    if texto_distancia1.startswith("0") and len(texto_distancia1) > 1 and texto_distancia1[1] not in [".", ","]:
        texto = texto_distancia1.lstrip("0") 
        ui.distancia_1.setText(texto)
        texto_distancia1 = texto
    
    texto_limpo = texto_distancia1.replace(" ", "").replace(",", ".")
    
    try:
        valor_distancia1 = float(texto_limpo)
    except:
        return
    
    unidade1 = ui.combo_distancia_1.currentText()
    unidade2 = ui.combo_distancia_2.currentText()
    
    convertendo = True
    em_metros = valor_distancia1 * conversoes_distancia[unidade1]
    resultado = em_metros / conversoes_distancia[unidade2]
    resultado = round(resultado, 4)
    
    texto_formatado = formatar_numero(resultado)
    ui.distancia_2.setText(texto_formatado)
    
    convertendo = False 

    
def converter_distancia2():
    global convertendo
    if convertendo:  
        return
    
    texto_distancia2 = ui.distancia_2.text()

    if texto_distancia2.startswith("0") and len(texto_distancia2) > 1 and texto_distancia2[1] not in [".", ","]:
        texto = texto_distancia2.lstrip("0") 
        ui.distancia_2.setText(texto)
        texto_distancia2 = texto
    
    texto_limpo = texto_distancia2.replace(" ", "").replace(",", ".")
    
    try:
        valor_distancia2 = float(texto_limpo)
    except:
        return
    
    unidade1 = ui.combo_distancia_1.currentText()
    unidade2 = ui.combo_distancia_2.currentText()
    
    convertendo = True
    em_metros = valor_distancia2 * conversoes_distancia[unidade2]
    resultado = em_metros / conversoes_distancia[unidade1]
    resultado = round(resultado, 4)
    
    texto_formatado = formatar_numero(resultado)
    ui.distancia_1.setText(texto_formatado)
    
    convertendo = False


def formatar_numero(numero):
    numero = round(numero, 4)
    
    if numero % 1 == 0:
        return f"{int(numero):,}".replace(",", " ")
    else:
        texto = f"{numero:,.4f}"  
        texto = texto.replace(",", " ")    # milhares com espaço
        texto = texto.replace(".", ",")     # decimal com vírgula
        return texto.rstrip("0").rstrip(",")  # remove zeros à direita


def substituir_ponto_1():
    global ajustando_texto
    if ajustando_texto:
        return
    
    texto = ui.distancia_1.text()
    
    if "," in texto and "." in texto:
        ajustando_texto = True
        ui.distancia_1.setText(texto.replace(".", ""))
        ajustando_texto = False
        return
    
    if "." in texto and "," not in texto:
        ajustando_texto = True
        novo_texto = texto.replace(".", ",")
        ui.distancia_1.setText(novo_texto)
        ajustando_texto = False


def substituir_ponto_2():
    global ajustando_texto
    if ajustando_texto:
        return
    
    texto = ui.distancia_2.text()
    
    if "," in texto and "." in texto:
        ajustando_texto = True
        ui.distancia_2.setText(texto.replace(".", ""))
        ajustando_texto = False
        return
    
    if "." in texto and "," not in texto:
        ajustando_texto = True
        novo_texto = texto.replace(".", ",")
        ui.distancia_2.setText(novo_texto)
        ajustando_texto = False

def numeros_distancia(num):

    campo_ativo = app.focusWidget()
    if not isinstance(campo_ativo, QLineEdit):
        return
    
    texto_atual = campo_ativo.text()
    
    if texto_atual == "0":
        campo_ativo.setText(str(num))
    else:
        campo_ativo.setText(texto_atual + str(num))

def apagar_tudo_dist ():
    global convertendo, ajustando_texto
    ui.distancia_1.setText("0")
    ui.distancia_2.setText("0")
    convertendo = False
    ajustando_texto = False


def apagar_dist():
    campo_ativo = app.focusWidget()
    texto_atual = campo_ativo.text()
    campo_ativo.setText(texto_atual [:-1] )

def ir_para_calculadora():
    ui.stackedWidget.setCurrentIndex(0)
    
def ir_para_distancias():
    ui.stackedWidget.setCurrentIndex(1)
    
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
ui.operador_mais.clicked.connect (lambda:operacao("+"))
ui.operador_menos.clicked.connect(lambda:operacao("-"))
ui.operador_dividir.clicked.connect(lambda:operacao("/"))
ui.operador_multiplicar.clicked.connect(lambda:operacao("*"))
ui.botao_resultado.clicked.connect(resultado)
ui.botao_apagar_tudo.clicked.connect(limpar_tudo)
ui.operador_percentagem.clicked.connect(percentagem) 
ui.botao_sinal.clicked.connect(sinal)
ui.distancia_1.textChanged.connect(converter_distancia1)
ui.distancia_1.textChanged.connect(substituir_ponto_1)
ui.distancia_2.textChanged.connect(converter_distancia2)
ui.distancia_2.textChanged.connect(substituir_ponto_2)
ui.combo_distancia_1.currentIndexChanged.connect(converter_distancia1)
ui.combo_distancia_2.currentIndexChanged.connect(converter_distancia1)
ui.numero_1_dist.clicked.connect(lambda: numeros_distancia(1))
ui.numero_2_dist.clicked.connect(lambda: numeros_distancia(2))
ui.numero_3_dist.clicked.connect(lambda: numeros_distancia(3))
ui.numero_4_dist.clicked.connect(lambda: numeros_distancia(4))
ui.numero_5_dist.clicked.connect(lambda: numeros_distancia(5))
ui.numero_6_dist.clicked.connect(lambda: numeros_distancia(6))
ui.numero_7_dist.clicked.connect(lambda: numeros_distancia(7))
ui.numero_8_dist.clicked.connect(lambda: numeros_distancia(8))
ui.numero_9_dist.clicked.connect(lambda: numeros_distancia(9))
ui.numero_0_dist.clicked.connect(lambda: numeros_distancia(0))
ui.botao_apagar_dist.clicked.connect(apagar_dist)
ui.botao_apagar_tudo_dist.clicked.connect(apagar_tudo_dist)
ui.toolButton_1.clicked.connect(abrir_menu)
ui.toolButton_0.clicked.connect(abrir_menu)

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
QShortcut(QKeySequence("+"), janela).activated.connect(lambda:operacao("+"))
QShortcut(QKeySequence("-"), janela).activated.connect(lambda:operacao("-"))
QShortcut(QKeySequence("/"), janela).activated.connect(lambda:operacao("/"))
QShortcut(QKeySequence("*"), janela).activated.connect(lambda:operacao("*"))
QShortcut(QKeySequence("backspace"), janela).activated.connect(apagar)
QShortcut(QKeySequence("."), janela).activated.connect(decimal)
QShortcut(QKeySequence("Delete"), janela).activated.connect(limpar_tudo)
QShortcut(QKeySequence("Delete"), janela).activated.connect(apagar_tudo_dist)

janela.show()
app.exec()