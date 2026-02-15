from PySide6.QtWidgets import QApplication, QDialog, QTextEdit, QListWidgetItem, QMessageBox, QInputDialog, QWidget, QMainWindow
from to_do_list_ui import Ui_Dialog
from PySide6.QtGui import QIcon, QPixmap, QColor   
from PySide6.QtCore import QTimer, Qt
import json
import os
import sys

if getattr(sys, 'frozen', False):
    # Rodando como .exe
    pasta_base = sys._MEIPASS
else:
    # Rodando como script Python
    pasta_base = os.path.dirname(os.path.abspath(__file__))

#Botão Apagar
def clique_apagar():
    linha_selecionada = ui.lista_tarefas.currentRow()
    if linha_selecionada >= 0:
        ui.lista_tarefas.takeItem(linha_selecionada)
        guardar_tarefas()
    else:
        janela_erro = QDialog()
        janela_erro.setWindowTitle("Erro ao apagar tarefa")
        erro = QTextEdit(janela_erro)
        erro.setReadOnly(True)
        erro.setText("⚠️ Nenhuma tarefa selecionada para apagar!")
        erro.resize(300, 50)
        janela_erro.resize(300,50)
        janela_erro.exec()
        
#Completar/anular
def checkbox_changed(item):
    if item.checkState() == Qt.Checked:
        item.setData(Qt.UserRole, True) #Guardar dados
        completa = item.data(Qt.UserRole) #Recuperar dados
        print(f"✅ Tarefa {item.text()} marcada como completa com status: {completa}")
        item.setForeground(QColor(0, 150, 0))
        guardar_tarefas()
    else :
        item.setData(Qt.UserRole, False)
        completa = item.data(Qt.UserRole)
        print(f"✅ Tarefa {item.text()} marcada como completa com status: {completa}")
        item.setForeground(QColor(0, 0, 0))
        guardar_tarefas()

#Botão apagar tudo
def apagar_tudo():
       
    # PRIMEIRO: Verifica se tem tarefas
       if ui.lista_tarefas.count() == 0:
        ui.label_erro.setText("⚠️ Nenhuma tarefa para apagar!")
        QTimer.singleShot(3000, lambda: ui.label_erro.clear())
        return
    # SEGUNDO: Pergunta ao utilizador se tem a certeza
       resposta = QMessageBox.question( janela,
        "Confirmar",
        "Apagar TODAS as tarefas?",
    )
    
       if resposta == QMessageBox.Yes:
        ui.lista_tarefas.clear()
        ui.label_erro.clear()
        guardar_tarefas()
        
        
#Botão Adicionar
def adicionar_tarefa():

    tarefa = ui.input_tarefa.text()
    if not tarefa:
        ui.label_erro.setText("⚠️ Insira uma tarefa!")
        QTimer.singleShot(4000, lambda: ui.label_erro.clear())
    else:
        item = QListWidgetItem(tarefa)
        item.setData(Qt.UserRole, False)  # Guardar estado de completado
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        ui.lista_tarefas.addItem(item)
        print(f"✅ Tarefa '{tarefa}' adicionada com status: {item.data(Qt.UserRole)}")
        guardar_tarefas()

        ui.input_tarefa.clear()
        ui.label_erro.clear()  

#Botao Editar       
def botao_editar():    
    linha_selecionada = ui.lista_tarefas.currentRow()
    if linha_selecionada >= 0 : 
        item = ui.lista_tarefas.item(linha_selecionada)
        texto_atual = item.text()
        novo_texto = QInputDialog.getText(
            janela,
            "Editar Tarefa",
            "Novo texto para a tarefa:",
            text=texto_atual
        )
        print(f" outra variavel aqui {novo_texto[1]}")
        if novo_texto:  # Se o usuário clicou em OK e não cancelou
            item.setText(novo_texto[0])  # Atualiza o texto do item
            guardar_tarefas()

def guardar_tarefas():
    tarefas = []
    total = ui.lista_tarefas.count()
    for i in range (total):
        item = ui.lista_tarefas.item(i)
        tarefa_dict = {
            "texto": item.text(),
            "completa": item.data(Qt.UserRole)
        }
        tarefas.append(tarefa_dict)

    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as f:
            tarefas = json.load(f)
            for tarefa in tarefas:
                item = QListWidgetItem(tarefa["texto"])
                item.setData(Qt.UserRole, tarefa["completa"])
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Checked if tarefa["completa"] else Qt.Unchecked)
                if tarefa["completa"]:
                    item.setForeground(QColor(0, 150, 0))
                ui.lista_tarefas.addItem(item)
    except FileNotFoundError:
        pass 



app = QApplication([])
janela = QMainWindow()
janela.setWindowTitle("Lista de Tarefas")    
ui = Ui_Dialog()
ui.setupUi(janela)
janela.setWindowTitle("Lista de Tarefas")
janela.setWindowIcon(QIcon("Icon.ico"))


janela.setWindowIcon(QIcon(os.path.join(pasta_base, "Icon.ico")))
  

for i in range(ui.lista_tarefas.count()):
    item = ui.lista_tarefas.item(i)
    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
    item.setCheckState(Qt.Unchecked)


ui.botao_adicionar.clicked.connect(adicionar_tarefa)
ui.botao_apagar.clicked.connect(clique_apagar)
ui.apagar_tudo.clicked.connect(apagar_tudo)
ui.lista_tarefas.itemChanged.connect(checkbox_changed)
ui.editar_tarefa.clicked.connect(botao_editar)
ui.input_tarefa.returnPressed.connect(adicionar_tarefa)

carregar_tarefas()
janela.show()
app.exec()