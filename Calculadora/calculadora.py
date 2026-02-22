from PySide6.QtWidgets import QApplication, QDialog, QMenu, QLineEdit
from calculadora_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QShortcut, QKeySequence, QFont, QFontDatabase, QDoubleValidator, QPixmap
from PySide6.QtCore import Qt, QLocale, QEvent, QObject, QDate, QTimer
import sys
import os
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta
import locale
import requests
import json

class FiltroFoco(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            if obj in (ui.valor_origem, ui.valor_destino):
                converter_moedas()
            if obj in (ui.combo_moeda_1, ui.combo_moeda_2):
                QTimer.singleShot(0, obj.lineEdit().selectAll)
            else:
                QTimer.singleShot(0, obj.selectAll)

        return super().eventFilter(obj, event)

#setup janela
app = QApplication([])
janela = QDialog()
ui = Ui_Dialog()
ui.setupUi(janela)
filtro = FiltroFoco()
ui.combo_moeda_1.installEventFilter(filtro)
ui.combo_moeda_2.installEventFilter(filtro)
ui.combo_moeda_1.lineEdit().installEventFilter(filtro)
ui.combo_moeda_2.lineEdit().installEventFilter(filtro)
janela.setWindowTitle("Calculadora")
janela.setWindowIcon(QIcon("icon.ico"))
janela.setStyleSheet("background-color: #f0f0f0;") 
janela.resize(300, 440)

ui.label_dias.setText("")
ui.label_erro.setVisible(False)
ui.label_resultado.setVisible(False)
ui.label_dias.setVisible(False)
ui.label_horas.setVisible(False)
ui.label_semanas.setVisible(False)
ui.label_final.setVisible(False)

ui.simbolo_origem.setText("€")
ui.simbolo_destino.setText("$")

class FiltroVirgula(QObject):
    def __init__(self, campo):
        super().__init__(campo)
        self.campo = campo
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Period:

            if "," in self.campo.text():
                return True
            
            self.campo.insert(",")
            return True
        return False
    
filtro1 = FiltroVirgula(ui.distancia_1)
ui.distancia_1.installEventFilter(filtro1)
filtro2 = FiltroVirgula(ui.distancia_2)
ui.distancia_2.installEventFilter(filtro2)

filtro3 = FiltroVirgula(ui.temperatura_1)
ui.temperatura_1.installEventFilter(filtro3)
filtro4 = FiltroVirgula(ui.temperatura_2)
ui.temperatura_2.installEventFilter(filtro4)

filtro5 = FiltroVirgula(ui.tempo_1)
ui.tempo_1.installEventFilter(filtro5)
filtro6 = FiltroVirgula(ui.tempo_2)
ui.tempo_2.installEventFilter(filtro6)

filtro_moeda_1 = FiltroVirgula(ui.valor_origem)
ui.valor_origem.installEventFilter(filtro_moeda_1)
filtro_moeda_2 = FiltroVirgula(ui.valor_destino)
ui.valor_destino.installEventFilter(filtro_moeda_2)

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


ui.combo_temp_1.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_temp_1.view().setStyleSheet("""
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

ui.combo_temp_2.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_temp_2.view().setStyleSheet("""
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


ui.combo_tempo_1.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_tempo_1.view().setStyleSheet("""
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

ui.combo_tempo_2.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_tempo_2.view().setStyleSheet("""
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


ui.combo_datas_1.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_datas_1.view().setStyleSheet("""
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

ui.combo_datas_2.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_datas_2.view().setStyleSheet("""
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


ui.combo_moeda_2.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_moeda_2.view().setStyleSheet("""
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

ui.combo_moeda_1.view().window().setStyleSheet("""
    QWidget {
        background-color: white;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
""")
ui.combo_moeda_1.view().setStyleSheet("""
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


validator = QDoubleValidator()
validator.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
ui.distancia_1.setValidator(validator)
ui.distancia_2.setValidator(validator)
ui.temperatura_1.setValidator(validator)
ui.temperatura_2.setValidator(validator)
ui.tempo_1.setValidator(validator)
ui.tempo_2.setValidator(validator)
ui.valor_origem.setValidator(validator)
ui.valor_destino.setValidator(validator)



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


caminho_seta = resource_path("arrow.png").replace("\\", "/")
caminho_calen = resource_path("calendar.png").replace("\\", "/")

estilo_combo = f"""
    QComboBox {{
        background-color: white;
        color: #333;
        font-size: 11px;
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 5px 10px;
    }}
    QComboBox::drop-down {{
        border: none;
        width: 25px;
    }}
    QComboBox::down-arrow {{
        image: url({caminho_seta});
        width: 10px;
        height: 10px;
    }}
"""

estilo_dateedit = f"""
    QDateEdit {{
        background-color: white;
        color: black;
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 5px 8px;
        font-size: 14px;
        height: 35px;
    }}
    
    QDateEdit:hover {{
        border: 2px solid #ff8c42;
    }}
    
    QDateEdit:focus {{
        border: 2px solid #ff8c42;
    }}
    
    QDateEdit::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: right center;
        width: 25px;
        border: none;
    }}
    
    QDateEdit::down-arrow {{
        image: url({caminho_calen});
        width: 16px;
        height: 16px;
    }}
"""

ui.combo_distancia_1.setStyleSheet(estilo_combo)
ui.combo_distancia_2.setStyleSheet(estilo_combo)
ui.combo_temp_1.setStyleSheet(estilo_combo)
ui.combo_temp_2.setStyleSheet(estilo_combo)
ui.combo_tempo_1.setStyleSheet(estilo_combo)
ui.combo_tempo_2.setStyleSheet(estilo_combo)
ui.combo_datas_1.setStyleSheet(estilo_combo)
ui.combo_datas_2.setStyleSheet(estilo_combo)
ui.combo_moeda_2.setStyleSheet(estilo_combo)
ui.combo_moeda_1.setStyleSheet(estilo_combo)
ui.date_edit_1.setStyleSheet(estilo_dateedit)
ui.date_edit_2.setStyleSheet(estilo_dateedit)
ui.date_edit_3.setStyleSheet(estilo_dateedit)



def estilizar_calendario_dateedit(date_edit):
    """Aplica estilo BRANCO/LARANJA ao calendário popup"""
    calendario = date_edit.calendarWidget()
    
    calendario.setStyleSheet("""
        QCalendarWidget {
            background-color: white;
        }
        
        /* Navegação (topo com mês/ano) */
        QCalendarWidget QToolButton {
            color: black;
            background-color: #f0f0f0;
            border: none;
            border-radius: 4px;
            padding: 5px;
            margin: 2px;
        }
        
        QCalendarWidget QToolButton:hover {
            background-color: #ff8c42;
            color: white;
        }
        
        /* Spinbox do ano */
        QCalendarWidget QSpinBox {
            background-color: #f0f0f0;
            color: black;
            selection-background-color: #ff8c42;
            selection-color: white;
            border: 1px solid #ddd;
        }
        
        /* Menu dropdown */
        QCalendarWidget QMenu {
            background-color: white;
            color: black;
        }
        
        /* Grid dos dias */
        QCalendarWidget QTableView {
            background-color: white;
            color: black;
            selection-background-color: #ff8c42;
            selection-color: white;
            border: none;
            gridline-color: #e0e0e0;
        }
        
        /* Header dias da semana */
        QCalendarWidget QWidget#qt_calendar_navigationbar {
            background-color: #f5f5f5;
        }
        
        /* Dias do mês atual */
        QCalendarWidget QAbstractItemView:enabled {
            color: black;
        }
        
        /* Dias de outros meses */
        QCalendarWidget QAbstractItemView:disabled {
            color: #cccccc;
        }
    """)

estilizar_calendario_dateedit(ui.date_edit_2) 
estilizar_calendario_dateedit(ui.date_edit_1)





ui.label_2.setPixmap(QPixmap(resource_path("construcao.png")))

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
taxas_globais = {}
widget = QApplication.focusWidget()
foco_origem = True
foco_destino = False
ficheiro_taxas = "taxas.json"
dados = {}

estilo_spinbox = """
    QSpinBox {
        background-color: white;
        color: #333;
        font-size: 14px;
        selection-background-color: #ff8c42;
        selection-color: white;
    }  
"""
estilo_radiobutton = """
    QRadioButton::indicator {
        width: 11px;
        height: 11px;
        border-radius: 7px;  /* Círculo perfeito! */
    }

    QRadioButton::indicator:checked {
        background-color: #ff8c42;
        border: 2px solid #ff8c42;
    }

    QRadioButton::indicator:unchecked {
        background-color: white;
        border: 2px solid #ccc;
    }
"""

ui.radio_adicionar.setStyleSheet(estilo_radiobutton)
ui.radio_subtrair.setStyleSheet(estilo_radiobutton)


ui.radio_adicionar.setStyleSheet(estilo_radiobutton)
ui.radio_subtrair.setStyleSheet(estilo_radiobutton)
ui.spinbox_meses.setStyleSheet(estilo_spinbox)
ui.spinbox_dias.setStyleSheet(estilo_spinbox)
ui.spinbox_anos.setStyleSheet(estilo_spinbox)

ui.combo_moeda_1.completer().setFilterMode(Qt.MatchContains)
ui.combo_moeda_2.completer().setFilterMode(Qt.MatchContains)


ui.simbolo_destino.setText("€")

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
    menu.addAction("Calculadora padrão", ir_para_calculadora)
    menu.addAction("Distâncias", ir_para_distancias)
    menu.addAction("Temperatura", ir_para_temperatura)
    menu.addAction("Tempo", ir_para_tempo)
    menu.addAction("Datas", ir_para_datas)
    menu.addAction("Velocidades", ir_para_velocidades)
    menu.addAction("Moedas", ir_para_moedas)
    menu.addAction("Defenicoes", ir_para_defenicoes)
    menu.addAction("Acerca de", ir_para_acerca_de)
    menu.exec(ui.toolButton_1.mapToGlobal(ui.toolButton_1.rect().bottomLeft()))

#Dicionarios
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

conversoes_temperatura = {
    "Celsius": (1, 0),        
    "Fahrenheit": (5/9, -32), 
    "Kelvin": (1, -273.15),   
}

conversoes_tempo = {
    "Milissegundos": 1 / 3_600_000,      # 1 milissegundo = 0.00000027778 horas
    "Microssegundos": 1 / 3_600_000_000, # 1 microssegundo = 0.00000000027778 horas
    "Segundos": 1 / 3_600,                # 1 segundo = 0.00027778 horas
    "Minutos": 1 / 60,                    # 1 minuto = 0.01667 horas
    "Horas": 1,                           # 1 hora = 1 hora
    "Dias": 24,                           # 1 dia = 24 horas
    "Semanas": 168,                       # 1 semana = 168 horas
    "Anos": 8_760                         # 1 ano = 8760 horas (365 dias)
}

#Operações conversão
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


def converter_temperatura1():
    global convertendo
    if convertendo:  
        return
    
    texto_temperatura1 = ui.temperatura_1.text()

    if texto_temperatura1.startswith("0") and len(texto_temperatura1) > 1 and texto_temperatura1[1] not in [".", ","]:
        texto = texto_temperatura1.lstrip("0") 
        ui.temperatura_1.setText(texto)
        texto_temperatura1 = texto

    texto_limpo = texto_temperatura1.replace(" ", "").replace(",", ".")
    try:
        valor_temperatura1 = float(texto_limpo)
    except:
        return
    unidade1 = ui.combo_temp_1.currentText()
    unidade2 = ui.combo_temp_2.currentText()
    convertendo = True
    em_celsius = (valor_temperatura1 + conversoes_temperatura[unidade1][1] ) * conversoes_temperatura[unidade1][0]
    resultado = (em_celsius / conversoes_temperatura[unidade2][0]) - conversoes_temperatura[unidade2][1]    
    resultado = round(resultado, 4)

    texto_formatado = formatar_numero(resultado)
    ui.temperatura_2.setText(texto_formatado)

    convertendo = False

def converter_temperatura2():
    global convertendo
    if convertendo:  
        return

    texto_temperatura2 = ui.temperatura_2.text()

    if texto_temperatura2.startswith("0") and len(texto_temperatura2) > 1 and texto_temperatura2[1] not in [".", ","]:
        texto = texto_temperatura2.lstrip("0") 
        ui.temperatura_2.setText(texto)
        texto_temperatura2 = texto

    texto_limpo = texto_temperatura2.replace(" ", "").replace(",", ".")
    try:
        valor_temperatura2 = float(texto_limpo)
    except:
        return
    unidade1 = ui.combo_temp_1.currentText()
    unidade2 = ui.combo_temp_2.currentText()
    convertendo = True
    em_celsius = (valor_temperatura2 + conversoes_temperatura[unidade2][1] ) * conversoes_temperatura[unidade2][0]
    resultado = (em_celsius / conversoes_temperatura[unidade1][0]) - conversoes_temperatura[unidade1][1]    
    resultado = round(resultado, 4)

    texto_formatado = formatar_numero(resultado)
    ui.temperatura_1.setText(texto_formatado)
    
    convertendo = False


def converter_tempo1():
    global convertendo      
    if convertendo :
        return

    texto_tempo1 = ui.tempo_1.text()

    if texto_tempo1.startswith("0") and len(texto_tempo1) > 1 and texto_tempo1[1] not in [".", ","]:
        texto = texto_tempo1.lstrip("0") 
        ui.tempo_1.setText(texto)
        texto_tempo1 = texto

    texto_limpo = texto_tempo1.replace(" ", "").replace(",", ".")
    try:
        valor_tempo1 = float(texto_limpo)
    except:
        return
    unidade1 = ui.combo_tempo_1.currentText()
    unidade2 = ui.combo_tempo_2.currentText()
    convertendo = True
    em_horas = valor_tempo1 * conversoes_tempo[unidade1]
    resultado = em_horas / conversoes_tempo[unidade2]
    resultado = round(resultado, 4)

    #texto_base_formatado = formatar_numero(valor_tempo1)
    texto_formatado = formatar_numero(resultado)
    ui.tempo_2.setText(texto_formatado)
    #ui.tempo_1.setText(texto_base_formatado)

    
    convertendo = False

def converter_tempo2():
    global convertendo      
    if convertendo :
        return

    texto_tempo2 = ui.tempo_2.text()

    if texto_tempo2.startswith("0") and len(texto_tempo2) > 1 and texto_tempo2[1] not in [".", ","]:
        texto = texto_tempo2.lstrip("0") 
        ui.tempo_2.setText(texto)
        texto_tempo2 = texto

    texto_limpo = texto_tempo2.replace(" ", "").replace(",", ".")
    try:
        valor_tempo2 = float(texto_limpo)
    except:
        return
    unidade1 = ui.combo_tempo_1.currentText()
    unidade2 = ui.combo_tempo_2.currentText()
    convertendo = True
    em_horas = valor_tempo2 * conversoes_tempo[unidade2]
    resultado = em_horas / conversoes_tempo[unidade1]
    resultado = round(resultado, 4)

    texto_formatado = formatar_numero(resultado)
    ui.tempo_1.setText(texto_formatado)
    
    
    convertendo = False

def calcular_datas():
    qdata_inicial = ui.date_edit_1.date()
    qdata_final = ui.date_edit_2.date()
    pdata_inicial = qdata_inicial.toPython()
    pdata_final = qdata_final.toPython()

    diferenca = pdata_final - pdata_inicial
    dias = diferenca.days
    semanas_completas = dias // 7
    dias_restantes = dias % 7
    horas = dias * 24

    if dias == 0:
        ui.label_dias.setText("")
        ui.label_erro.setText("⚠️ As datas selecionadas são idênticas")
        ui.label_erro.setVisible(True)
        QTimer.singleShot(3000, lambda: ui.label_erro.setVisible(False))
        ui.label_resultado.setVisible(False)
        ui.label_dias.setVisible(False)
        ui.label_horas.setVisible(False)
        ui.label_semanas.setVisible(False)
    elif dias < 0:
        ui.label_dias.setText("")
        ui.label_erro.setText("⚠️ A data final deve ser depois da inicial!")
        ui.label_erro.setVisible(True)
        ui.label_resultado.setVisible(False)
        ui.label_dias.setVisible(False)
        ui.label_horas.setVisible(False)
        ui.label_semanas.setVisible(False)
        QTimer.singleShot(3000, lambda: ui.label_erro.setVisible(False))
    elif dias == 1:
        ui.label_erro.setVisible(False)
        ui.label_semanas.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dia")
    elif dias < 7:
        ui.label_erro.setVisible(False)
        ui.label_semanas.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
    elif semanas_completas == 1 and dias_restantes == 0:
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semana")
    elif semanas_completas == 1 and dias_restantes == 1:
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semana e {dias_restantes} dia")
    elif semanas_completas == 1 and dias_restantes > 1:
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semana e {dias_restantes} dias")
    elif semanas_completas > 1 and dias_restantes == 0:
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semanas")
    elif semanas_completas > 1 and dias_restantes == 1:
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semanas e {dias_restantes} dia")
    else: 
        ui.label_erro.setVisible(False)
        ui.label_resultado.setVisible(True)
        ui.label_dias.setVisible(True)
        ui.label_horas.setVisible(True)
        ui.label_semanas.setVisible(True)
        ui.label_horas.setText(f"⏰ {horas} horas")
        ui.label_dias.setText(f"📆 {dias} dias")
        ui.label_semanas.setText(f"📊 {semanas_completas} semanas e {dias_restantes} dias")

def diferenca_datas () :

    try:
        locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')  # Linux/Mac
    except:
        try:
            locale.setlocale(locale.LC_TIME, 'pt_PT')  # Windows
        except:
            locale.setlocale(locale.LC_TIME, 'Portuguese_Portugal')  # Windows alternativo
    qdata_inicial = ui.date_edit_3.date()
    pdata_edit = qdata_inicial.toPython()

    anos = ui.spinbox_anos.value()
    meses = ui.spinbox_meses.value()
    dias = ui.spinbox_dias.value()

    if ui.radio_adicionar.isChecked() :
        nova_data = pdata_edit + relativedelta(years=anos, months=meses, days=dias)
        print(nova_data)
    else :
        nova_data = pdata_edit - relativedelta(years=anos, months=meses, days=dias)

    ui.label_final.setVisible(True)
    data = nova_data.strftime("%A, %d de %B de %Y")
    ui.label_final.setText(f"📅 {data}")

#Moedas

def obter_taxas ():
    global taxas_globais
    API_KEY = "fdfb941ee8c4bdd8b7591a28"
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
    try:
        response = requests.get(url)
        dados = response.json()

        if response.status_code == 200 :

            return dados["conversion_rates"]
        else:
            print(f"Erro! Código: {response.status_code}")
            return None
    except:
        print(f"Erro! Código: {response.status_code}")
        return None  
    
def carregar_taxas() :
    global ficheiro_taxas, dados, taxas_globais
    if os.path.exists(ficheiro_taxas):
        with open (ficheiro_taxas) as f :
            dados = json.load(f)

  
        if dados["data"] == str(date.today()):
            taxas_globais = dados["taxas"]
            print("Taxas carregadas do ficheiro")
            dados["data_hora"] = str(date.today()) + " " + datetime.now().strftime("%H:%M:%S")
            with open(ficheiro_taxas, "w") as f:
                json.dump(dados, f)
        
        return

    atualizar_taxas()

def atualizar_taxas():
    global ficheiro_taxas, dados, taxas_globais 
    taxas = obter_taxas()
    
    if taxas:
        taxas_globais = taxas
        
        dados = {
            "data": str(date.today()),
            "data_hora": str(date.today()) + " " + datetime.now().strftime("%H:%M"),
            "taxas": taxas
        }
        with open(ficheiro_taxas, "w") as f:
            json.dump(dados, f)
        print("Taxas atualizadas da API")

def converter_moedas () :
    global convertendo
    defenir_foco()

    texto_origem = ui.combo_moeda_1.currentText() 
    moeda_origem = texto_origem[:3]

    texto_destino = ui.combo_moeda_2.currentText() 
    moeda_destino = texto_destino[:3]
    print(moeda_destino)

    print(f"Foco origem: {foco_origem}")
    print(f"Foco destino: {foco_destino}")
    print(f"Widget ativo: {widget}")
   
    if foco_origem: 
        print("→ Convertendo origem para destino")
        string_origem = ui.valor_origem.text()
        valor_origem = texto_para_float(ui.valor_origem.text())


        if moeda_origem == "EUR" : 

            valor_conversao = valor_origem * taxas_globais[moeda_destino]
            valor_conversao = round(valor_conversao, 4)
            ui.label_cambio.setText(f"1 {moeda_origem} = {taxas_globais[moeda_destino]} {moeda_destino} ")

        elif moeda_destino == "EUR" : 
            valor_conversao = valor_origem / taxas_globais[moeda_origem]
            valor_conversao = round(valor_conversao, 4)
           
            valor_unitario = 1 / taxas_globais[moeda_origem]
            valor_unitario = round(valor_unitario, 5)
            print (valor_unitario)
            ui.label_cambio.setText(f"1 {moeda_origem} = {valor_unitario} {moeda_destino} ")

        else :
            valor_eur = valor_origem / taxas_globais[moeda_origem]
            valor_conversao = valor_eur * taxas_globais[moeda_destino]
            valor_conversao = round(valor_conversao, 4)
            
            valor_unitario = (1 / taxas_globais[moeda_origem]) * taxas_globais[moeda_destino]
            valor_unitario = round(valor_unitario, 5)
            ui.label_cambio.setText(f"1 {moeda_origem} = {valor_unitario} {moeda_destino} ")

        ui.valor_destino.blockSignals(True)
        valor_conversao = formatar_numero(valor_conversao)
        string_destino = str(valor_conversao)
        ui.valor_destino.setText(string_destino)
        ui.valor_destino.blockSignals(False)

        


    else :
        string_destino = ui.valor_destino.text()
        valor_destino = texto_para_float(ui.valor_destino.text())        
        print("→ Convertendo destino para origem")

        print("→ Convertendo destino para origem")
        if moeda_destino == "EUR" : 

            valor_conversao = valor_destino * taxas_globais[moeda_origem]
            valor_conversao = round(valor_conversao, 4)
            ui.label_cambio.setText(f"1 {moeda_destino} = {taxas_globais[moeda_origem]} {moeda_origem} ")
            
        elif moeda_origem == "EUR" : 
            valor_conversao = valor_destino / taxas_globais[moeda_destino]
            valor_conversao = round(valor_conversao, 4)


            valor_unitario = 1 / taxas_globais[moeda_destino]
            valor_unitario = round(valor_unitario, 5)
            print (valor_unitario)
            ui.label_cambio.setText(f"1 {moeda_destino} = {valor_unitario} {moeda_origem} ")

        else :
            valor_eur = valor_destino / taxas_globais[moeda_destino]
            valor_conversao = valor_eur * taxas_globais[moeda_origem]
            valor_conversao = round(valor_conversao, 4)

            valor_unitario = (1 / taxas_globais[moeda_destino]) * taxas_globais[moeda_origem]
            valor_unitario = round(valor_unitario, 5)
            ui.label_cambio.setText(f"1 {moeda_destino} = {valor_unitario} {moeda_origem} ")

        ui.valor_origem.blockSignals(True)
        valor_conversao = formatar_numero(valor_conversao)
        string_origem = str(valor_conversao)
        ui.valor_origem.setText(string_origem)
        ui.valor_origem.blockSignals(False)
 

def texto_para_float(texto):
    return float(texto.replace(",", ".").replace(" ", ""))


moedas = [
    "EUR - Euro (€)",
    "USD - Dólar Americano ($)",
    "GBP - Libra Esterlina (£)",
    "BRL - Real Brasileiro (R$)",
    "JPY - Iene Japonês (¥)",
    "CHF - Franco Suíço (Fr)",
    "CAD - Dólar Canadiano ($)",
    "AUD - Dólar Australiano ($)",
    "NZD - Dólar Neozelandês ($)",
    "CNY - Yuan Chinês (¥)",
    "INR - Rupia Indiana (₹)",
    "RUB - Rublo Russo (₽)",
    "KRW - Won Sul-Coreano (₩)",
    "MXN - Peso Mexicano ($)",
    "ARS - Peso Argentino ($)",
    "CLP - Peso Chileno ($)",
    "COP - Peso Colombiano ($)",
    "PEN - Sol Peruano (S/.)",
    "UYU - Peso Uruguaio ($U)",
    "PYG - Guarani Paraguaio (Gs)",
    "BOB - Boliviano (Bs.)",
    "ZAR - Rand Sul-Africano (R)",
    "TRY - Lira Turca (₺)",
    "SEK - Coroa Sueca (kr)",
    "NOK - Coroa Norueguesa (kr)",
    "DKK - Coroa Dinamarquesa (kr)",
    "ISK - Coroa Islandesa (kr)",
    "PLN - Zlóti Polaco (zł)",
    "CZK - Coroa Checa (Kč)",
    "HUF - Florim Húngaro (Ft)",
    "RON - Leu Romeno (lei)",
    "BGN - Lev Búlgaro (лв)",
    "HRK - Kuna Croata (kn)",
    "RSD - Dinar Sérvio (din.)",
    "UAH - Hrívnia Ucraniana (₴)",
    "ILS - Shekel Israelita (₪)",
    "SAR - Rial Saudita (﷼)",
    "AED - Dirham dos Emirados Árabes (د.إ)",
    "QAR - Rial do Catar (﷼)",
    "KWD - Dinar Kuwaitiano (KD)",
    "BHD - Dinar do Bahrein (BD)",
    "OMR - Rial Omanense (﷼)",
    "JOD - Dinar Jordano (JD)",
    "EGP - Libra Egípcia (£)",
    "MAD - Dirham Marroquino (د.م.)",
    "TND - Dinar Tunisino (DT)",
    "DZD - Dinar Argelino (دج)",
    "NGN - Naira Nigeriana (₦)",
    "KES - Xelim Queniano (KSh)",
    "GHS - Cedi Ganês (GH₵)",
    "THB - Baht Tailandês (฿)",
    "MYR - Ringgit Malaio (RM)",
    "SGD - Dólar de Singapura (S$)",
    "IDR - Rupia Indonésia (Rp)",
    "PHP - Peso Filipino (₱)",
    "VND - Dong Vietnamita (₫)",
    "HKD - Dólar de Hong Kong (HK$)",
    "TWD - Novo Dólar Taiwanês (NT$)",
    "PKR - Rupia Paquistanesa (₨)",
    "BDT - Taka de Bangladesh (৳)",
    "LKR - Rupia do Sri Lanka (₨)",
    "MMK - Kyat de Mianmar (K)",
    "KZT - Tenge Cazaque (₸)",
    "GEL - Lari Georgiano (₾)",
    "AMD - Dram Arménio (֏)",
    "AZN - Manat Azerbaijano (₼)",
    "BTC - Bitcoin (₿)",
    "XAF - Franco CFA (BEAC) (FCFA)",
    "XOF - Franco CFA (BCEAO) (CFA)",
    "CVE - Escudo Cabo-Verdiano ($)",
    "MZN - Metical Moçambicano (MT)",
    "AOA - Kwanza Angolano (Kz)",
    "AFN - Afghani Afegão (؋)",
    "ALL - Lek Albanês (L)",
    "ANG - Florim das Antilhas Neerlandesas (ƒ)",
    "AWG - Florim de Aruba (ƒ)",
    "BAM - Marco Conversível da Bósnia (KM)",
    "BBD - Dólar de Barbados ($)",
    "BIF - Franco do Burundi (Fr)",
    "BMD - Dólar das Bermudas ($)",
    "BND - Dólar do Brunei ($)",
    "BSD - Dólar das Bahamas ($)",
    "BTN - Ngultrum do Butão (Nu)",
    "BWP - Pula do Botswana (P)",
    "BYN - Rublo Bielorrusso (Br)",
    "BZD - Dólar do Belize ($)",
    "CDF - Franco Congolês (Fr)",
    "CLF - Unidade de Fomento Chilena (UF)",
    "CNH - Yuan Chinês Offshore (¥)",
    "CRC - Colón Costarriquenho (₡)",
    "CUP - Peso Cubano ($)",
    "DJF - Franco do Djibuti (Fr)",
    "DOP - Peso Dominicano ($)",
    "ERN - Nakfa da Eritreia (Nfk)",
    "ETB - Birr Etíope (Br)",
    "FJD - Dólar das Fiji ($)",
    "FKP - Libra das Ilhas Malvinas (£)",
    "FOK - Coroa Feroesa (kr)",
    "GGP - Libra de Guernsey (£)",
    "GIP - Libra de Gibraltar (£)",
    "GMD - Dalasi da Gâmbia (D)",
    "GNF - Franco da Guiné (Fr)",
    "GTQ - Quetzal Guatemalteco (Q)",
    "GYD - Dólar da Guiana ($)",
    "HNL - Lempira Hondurenha (L)",
    "HTG - Gourde Haitiano (G)",
    "IMP - Libra da Ilha de Man (£)",
    "IQD - Dinar Iraquiano (ع.د)",
    "IRR - Rial Iraniano (﷼)",
    "JEP - Libra de Jersey (£)",
    "JMD - Dólar Jamaicano ($)",
    "KGS - Som Quirguiz (с)",
    "KHR - Riel Cambojano (៛)",
    "KID - Dólar de Kiribati ($)",
    "KMF - Franco Comorense (Fr)",
    "KYD - Dólar das Ilhas Caimão ($)",
    "LAK - Kip Laosiano (₭)",
    "LBP - Libra Libanesa (LL)",
    "LRD - Dólar Liberiano ($)",
    "LSL - Loti do Lesoto (L)",
    "LYD - Dinar Líbio (LD)",
    "MDL - Leu Moldavo (L)",
    "MGA - Ariary Malgaxe (Ar)",
    "MKD - Denar Macedónio (ден)",
    "MNT - Tugrik Mongol (₮)",
    "MOP - Pataca Macaense (P)",
    "MRU - Uguia Mauritana (UM)",
    "MUR - Rupia Mauriciana (₨)",
    "MVR - Rufiyaa das Maldivas (ރ.)",
    "MWK - Kwacha Malauiano (MK)",
    "NAD - Dólar Namibiano ($)",
    "NIO - Córdoba Nicaraguense (C$)",
    "NPR - Rupia Nepalesa (₨)",
    "PAB - Balboa Panamenho (B/.)",
    "PGK - Kina Papua-Novaguineana (K)",
    "RWF - Franco Ruandês (Fr)",
    "SBD - Dólar das Ilhas Salomão ($)",
    "SCR - Rupia das Seicheles (₨)",
    "SDG - Libra Sudanesa (LS)",
    "SHP - Libra de Santa Helena (£)",
    "SLE - Leone de Serra Leoa (Le)",
    "SLL - Leone de Serra Leoa Antigo (Le)",
    "SOS - Xelim Somali (Sh)",
    "SRD - Dólar do Suriname ($)",
    "SSP - Libra do Sudão do Sul (£)",
    "STN - Dobra de São Tomé e Príncipe (Db)",
    "SYP - Libra Síria (£)",
    "SZL - Lilangeni da Essuatíni (L)",
    "TJS - Somoni Tajique (SM)",
    "TMT - Manat Turquemeno (T)",
    "TOP - Paʻanga de Tonga (T$)",
    "TTD - Dólar de Trindade e Tobago ($)",
    "TVD - Dólar de Tuvalu ($)",
    "TZS - Xelim Tanzaniano (Sh)",
    "UGX - Xelim Ugandês (Sh)",
    "UZS - Som Uzbeque (S)",
    "VES - Bolívar Venezuelano (Bs.S)",
    "VUV - Vatu de Vanuatu (Vt)",
    "WST - Tālā Samoano (T)",
    "XCD - Dólar do Caribe Oriental ($)",
    "XCG - Florim Caribenho (Cg)",
    "XDR - Direitos de Saque Especiais (SDR)",
    "XPF - Franco CFP (Fr)",
    "YER - Rial Iemenita (﷼)",
    "ZMW - Kwacha Zambiano (ZK)",
    "ZWG - Dólar do Zimbabwe (ZiG)",
    "ZWL - Dólar do Zimbabwe Antigo ($)",
]

ui.combo_moeda_1.addItems(moedas)
ui.combo_moeda_2.addItems(moedas)

def simbolo_moedas ():
    texto_origem = ui.combo_moeda_1.currentText()
    simbolo_origem = texto_origem[texto_origem.find("(") + 1 : texto_origem.find(")")]
    ui.simbolo_origem.setText(simbolo_origem)
    texto_destino = ui.combo_moeda_2.currentText()
    simbolo_destino = texto_destino[texto_destino.find("(") + 1 : texto_destino.find(")")]
    ui.simbolo_destino.setText(simbolo_destino) 

ui.simbolo_origem.setStyleSheet("""
    border: none;
    background: transparent;
    color: #999;
    font-size: 32px;
""")
ui.simbolo_destino.setStyleSheet("""
    border: none;
    background: transparent;
    color: #999;
    font-size: 32px;
""")



def formatar_numero(numero):
    numero = round(numero, 4)
    
    if numero % 1 == 0:
        return f"{int(numero):,}".replace(",", " ")
    else:
        texto = f"{numero:,.4f}"  
        texto = texto.replace(",", " ")    
        texto = texto.replace(".", ",")     
        return texto.rstrip("0").rstrip(",")  


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

def defenir_foco() :
    global foco_destino, foco_origem, widget
    widget = QApplication.focusWidget()
    if widget == ui.valor_origem:
        foco_origem = True
        foco_destino = False 
    elif widget == ui.valor_destino :
        foco_origem = False
        foco_destino = True 

def botao_atualizar (): 
    carregar_taxas()
    ui.label_dataup.setText(f"Atualizado em {dados['data_hora']}")

def apagar_tudo_foco ():
    global convertendo, ajustando_texto
    ui.distancia_1.setText("0")
    ui.distancia_2.setText("0")
    ui.temperatura_1.setText("0")
    ui.temperatura_2.setText("0")
    ui.valor_origem.setText("0")
    ui.valor_destino.setText("0")
    ui.combo_moeda_1.setCurrentIndex(0)
    ui.combo_moeda_2.setCurrentIndex(0)
    convertendo = False
    ajustando_texto = False

def apagar_foco():
    campo_ativo = app.focusWidget()
    texto_atual = campo_ativo.text()
    campo_ativo.setText(texto_atual [:-1] )

def ir_para_calculadora():
    janela.resize(300, 440) 
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(0)
    
def ir_para_distancias():
    janela.resize(300, 440)    
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(1)

def ir_para_temperatura () :
    janela.resize(300, 440)
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(2)

def ir_para_tempo () :
    janela.resize(300, 440)
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(3)

def ir_para_datas () :
    apagar_tudo_foco ()
    janela.resize(300, 440)
    ui.stackedWidget.setCurrentIndex(4)

def ir_para_datas_2 () :
    janela.resize(300, 440)
    
    if ui.combo_datas_1.currentIndex() == 0 :
        return
    else :
        ui.combo_datas_2.blockSignals(True)
        ui.combo_datas_2.setCurrentIndex(0)
        ui.combo_datas_2.blockSignals(False)
        ui.stackedWidget.setCurrentIndex(5)

def ir_para_datas_2_1 () :
    if ui.combo_datas_1.currentIndex() == 0 :
        return
       
    else :
        ui.combo_datas_1.blockSignals(True) 
        ui.combo_datas_1.setCurrentIndex(0)
        ui.combo_datas_1.blockSignals(False)
        ui.stackedWidget.setCurrentIndex(4)
    janela.resize(300, 440)

def ir_para_velocidades () :
    janela.resize(300, 440)
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(6)

def ir_para_moedas () :
    janela.resize(300, 520)
    ui.stackedWidget.setCurrentIndex(7)
    apagar_tudo_foco ()
    carregar_taxas() 
    ui.label_dataup.setText(f"Atualizado em {dados['data_hora']}")
    
    
def ir_para_defenicoes () :
    janela.resize(300, 440)
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(5)

def ir_para_acerca_de () :
    janela.resize(300, 440)
    apagar_tudo_foco ()
    ui.stackedWidget.setCurrentIndex(5)


ui.botao_resultado.setDefault(True)
ui.radio_adicionar.setChecked(True)
ui.date_edit_2.setDate(QDate.currentDate())
ui.date_edit_1.setDate(QDate.currentDate())
ui.date_edit_3.setDate(QDate.currentDate())



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
ui.distancia_1.textChanged.connect(converter_distancia1)
ui.distancia_1.textChanged.connect(substituir_ponto_1)
ui.distancia_2.textChanged.connect(converter_distancia2)
ui.distancia_2.textChanged.connect(substituir_ponto_2)
ui.combo_distancia_1.currentIndexChanged.connect(converter_distancia1)
ui.combo_distancia_2.currentIndexChanged.connect(converter_distancia2)

ui.numero_1_temp.clicked.connect(lambda: numeros_distancia(1))
ui.numero_2_temp.clicked.connect(lambda: numeros_distancia(2))
ui.numero_3_temp.clicked.connect(lambda: numeros_distancia(3))
ui.numero_4_temp.clicked.connect(lambda: numeros_distancia(4))
ui.numero_5_temp.clicked.connect(lambda: numeros_distancia(5))
ui.numero_6_temp.clicked.connect(lambda: numeros_distancia(6))
ui.numero_7_temp.clicked.connect(lambda: numeros_distancia(7))
ui.numero_8_temp.clicked.connect(lambda: numeros_distancia(8))
ui.numero_9_temp.clicked.connect(lambda: numeros_distancia(9))
ui.numero_0_temp.clicked.connect(lambda: numeros_distancia(0))

ui.numero_1_tempo.clicked.connect(lambda: numeros_distancia(1))
ui.numero_2_tempo.clicked.connect(lambda: numeros_distancia(2))
ui.numero_3_tempo.clicked.connect(lambda: numeros_distancia(3))
ui.numero_4_tempo.clicked.connect(lambda: numeros_distancia(4))
ui.numero_5_tempo.clicked.connect(lambda: numeros_distancia(5))
ui.numero_6_tempo.clicked.connect(lambda: numeros_distancia(6))
ui.numero_7_tempo.clicked.connect(lambda: numeros_distancia(7))
ui.numero_8_tempo.clicked.connect(lambda: numeros_distancia(8))
ui.numero_9_tempo.clicked.connect(lambda: numeros_distancia(9))
ui.numero_0_tempo.clicked.connect(lambda: numeros_distancia(0))
ui.tempo_1.textChanged.connect(converter_tempo1)
ui.combo_tempo_1.currentIndexChanged.connect(converter_tempo1)
ui.tempo_2.textChanged.connect(converter_tempo2)
ui.combo_tempo_2.currentIndexChanged.connect(converter_tempo2)

ui.botao_apagar_dist.clicked.connect(apagar_foco)
ui.botao_apagar_temp.clicked.connect(apagar_foco)
ui.botao_apagar_tudo_dist.clicked.connect(apagar_tudo_foco)
ui.botao_apagar_tudo_temp.clicked.connect(apagar_tudo_foco)
ui.toolButton_1.clicked.connect(abrir_menu)
ui.toolButton_0.clicked.connect(abrir_menu)
ui.toolButton_2.clicked.connect(abrir_menu)
ui.toolButton_3.clicked.connect(abrir_menu)
ui.toolButton_4.clicked.connect(abrir_menu)
ui.toolButton_5.clicked.connect(abrir_menu)
ui.toolButton_6.clicked.connect(abrir_menu)
ui.toolButton_7.clicked.connect(abrir_menu)
ui.toolButton_8.clicked.connect(abrir_menu)


ui.botao_update.clicked.connect(botao_atualizar)
ui.valor_origem.textChanged.connect(converter_moedas)
ui.combo_moeda_2.currentIndexChanged.connect(converter_moedas)
ui.valor_destino.textChanged.connect(converter_moedas)
ui.combo_moeda_1.currentIndexChanged.connect(converter_moedas)
ui.combo_moeda_1.currentIndexChanged.connect(simbolo_moedas)
ui.combo_moeda_2.currentIndexChanged.connect(simbolo_moedas)
ui.valor_origem.selectionChanged.connect(converter_moedas)
ui.valor_destino.selectionChanged.connect(converter_moedas)
ui.valor_origem.installEventFilter(filtro)
ui.valor_destino.installEventFilter(filtro)
ui.combo_moeda_1.lineEdit().installEventFilter(filtro)
ui.combo_moeda_2.installEventFilter(filtro)
ui.numero_1_moedas.clicked.connect(lambda: numeros_distancia(1))
ui.numero_2_moedas.clicked.connect(lambda: numeros_distancia(2))
ui.numero_3_moedas.clicked.connect(lambda: numeros_distancia(3))
ui.numero_4_moedas.clicked.connect(lambda: numeros_distancia(4))
ui.numero_5_moedas.clicked.connect(lambda: numeros_distancia(5))
ui.numero_6_moedas.clicked.connect(lambda: numeros_distancia(6))
ui.numero_7_moedas.clicked.connect(lambda: numeros_distancia(7))
ui.numero_8_moedas.clicked.connect(lambda: numeros_distancia(8))
ui.numero_9_moedas.clicked.connect(lambda: numeros_distancia(9))
ui.numero_0_moedas.clicked.connect(lambda: numeros_distancia(0))
ui.botao_apagar_moedas.clicked.connect(apagar_foco)
ui.botao_apagar_tudo_moedas.clicked.connect(apagar_tudo_foco)



ui.date_edit_1.dateChanged.connect(calcular_datas)
ui.date_edit_2.dateChanged.connect(calcular_datas)
ui.combo_datas_1.currentIndexChanged.connect(ir_para_datas_2)
ui.combo_datas_2.currentIndexChanged.connect(ir_para_datas_2_1)
ui.date_edit_3.dateChanged.connect(diferenca_datas)
ui.temperatura_1.textChanged.connect(converter_temperatura1)
ui.combo_temp_1.currentIndexChanged.connect(converter_temperatura1)
ui.temperatura_2.textChanged.connect(converter_temperatura2)
ui.combo_temp_2.currentIndexChanged.connect(converter_temperatura2)
ui.spinbox_dias.valueChanged.connect(diferenca_datas)
ui.spinbox_anos.valueChanged.connect(diferenca_datas)
ui.spinbox_meses.valueChanged.connect(diferenca_datas)
ui.botao_data_atual.clicked.connect(lambda: ui.date_edit_3.setDate(QDate.currentDate()))
ui.botao_data_atual_2.clicked.connect(lambda: ui.date_edit_1.setDate(QDate.currentDate()))



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
QShortcut(QKeySequence("Delete"), janela).activated.connect(apagar_tudo_foco)


janela.show()
app.exec()