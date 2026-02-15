from PySide6.QtWidgets import QApplication, QDialog, QTextEdit  
from vendas_design_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QPixmap

import os
import sys

if getattr(sys, 'frozen', False):
    pasta_base = sys._MEIPASS
else:
    pasta_base = os.path.dirname(os.path.abspath(__file__))



#botao verificar
def quando_clicar():
    # Lê as checkboxes

    has_license = ui.sim_licenca.isChecked()
    has_experience = ui.sim_experiencia.isChecked()
    has_space = ui.sim_espaco.isChecked()

    # Lógica
    global can_sell_regular_pet, can_sell_exotic_pet, cannot_sell_any_pet
    can_sell_regular_pet = (has_license or has_experience) and has_space
    can_sell_exotic_pet = (has_experience and has_license and has_space)
    cannot_sell_any_pet = not(has_license or has_experience) or not(has_space)

    # Verifica se todas as perguntas foram respondidas

    licenca_respondida = ui.sim_licenca.isChecked() or ui.nao_licenca.isChecked()
    experiencia_respondida = ui.sim_experiencia.isChecked() or ui.nao_experiencia.isChecked()
    espaco_respondido = ui.sim_espaco.isChecked() or ui.nao_espaco.isChecked()
    
    if not (licenca_respondida and experiencia_respondida and espaco_respondido):
        ui.mostrar_resultado.setText("⚠️ Por favor, responda todas as perguntas!")
        return 
    
    
    
    # Mostrar texto
    resultado = ""  # vazio

    if cannot_sell_any_pet:
        resultado += "❌ Nenhum animal pode ser vendido\n"
    else:
        if can_sell_regular_pet:
            resultado += "🐶Animal normal pode ser vendido\n"
        else:
            resultado += "❌Animal normal não pode ser vendido\n"
    
        if can_sell_exotic_pet:
            resultado += "🦎Animal exótico pode ser vendido\n"
        else:
            resultado += "❌Animal exótico não pode ser vendido\n"
    
    
    
    # Mostra o resultado NO CAMPO DE TEXTO da interface!
    ui.mostrar_resultado.setText(resultado)

#botao limpar
def limpar_resultado():
    ui.mostrar_resultado.clear()

#botao opcoes   
def ver_opcoes():
    janela1 = QDialog()
    text_opcoes = QTextEdit(janela1)
    resultado_opcoes = ""

    if can_sell_regular_pet is None:
        resultado_opcoes = "⚠️ Clique primeiro em Verificar!(O Luis é gayzola)"

    elif can_sell_exotic_pet:
        resultado_opcoes = (
            "🐾 Animais Comuns:\n"
            "  Cão.......................... 350€\n"
            "  Gato......................... 250€\n"
            "  Coelho....................... 120€\n"
            "  Peixes........................ 40€\n"
            "  Hamster...................... 60€\n"
            "  Tartaruga.................... 80€\n\n"
            "🦎 Animais Exóticos:\n"
            "  Cobra...................... 500€\n"
            "  Tarantula.................. 300€\n"
            "  Macaco..................... 800€\n"
            "  Furão...................... 200€\n"
            "  Iguana..................... 400€\n"
            "  Chinchila.................. 150€\n"
        )

    elif can_sell_regular_pet:
        resultado_opcoes = (
            "🐾 Animais Comuns:\n"
            "  Cão.......................... 350€\n"
            "  Gato......................... 250€\n"
            "  Coelho....................... 120€\n"
            "  Peixes........................ 40€\n"
            "  Hamster...................... 60€\n"
            "  Tartaruga.................... 80€\n"
        )

    else:
        resultado_opcoes = "❌ Nenhum animal pode ser vendido."

    text_opcoes.setText(resultado_opcoes)
    text_opcoes.resize(400, 300)
    janela1.setWindowTitle("Opções de Animais e Preços")
    janela1.exec()      

#Variaveis globais
    
# Configuração da aplicação e janela

app = QApplication([])
janela = QDialog()    
ui = Ui_Dialog()
ui.setupUi(janela)

# Nome janela
janela.setWindowTitle("Venda de Animais - Sistema de Verificação")


ui.Botao_verificar.clicked.connect(quando_clicar)
ui.botao_limpar.clicked.connect(limpar_resultado) 
ui.botao_opcoes.clicked.connect(ver_opcoes)

can_sell_regular_pet = None
can_sell_exotic_pet = None
cannot_sell_any_pet = None

# Ícono e imagem (com pasta_base)
janela.setWindowIcon(QIcon(os.path.join(pasta_base, "Icon.ico")))
ui.foto.setPixmap(QPixmap(os.path.join(pasta_base, "image.jpg")))

janela.show()
app.exec()