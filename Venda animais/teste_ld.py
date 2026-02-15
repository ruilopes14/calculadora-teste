import sys
import os
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt  # ← ADICIONA ISTO!
from vendas_design_ui import Ui_Dialog

class MinhaJanela(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # === IMAGEM CORRIGIDA (foto + scaled certo) ===
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        
        imagem_path = os.path.join(base_dir, 'image.jpg')  # Nome da tua foto
        pixmap = QPixmap(imagem_path)
        # scaled CORRETO: sem keywords, usa Qt.KeepAspectRatio
        self.ui.foto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.ui.foto.setScaledContents(True)
        # =============================================
        
        # Conecta o botão verificar
        self.ui.Botao_verificar.clicked.connect(self.verificar)
    
    def verificar(self):
        # ... resto igual
        has_license = self.ui.sim_licenca.isChecked()
        has_experience = self.ui.sim_experiencia.isChecked()
        has_space = self.ui.sim_espaco.isChecked()
        
        can_sell_regular = (has_license or has_experience) and has_space
        can_sell_exotic = has_experience and has_license and has_space
        cannot_sell = not(has_license or has_experience) and not(has_space)
        
        resultado = ""
        if can_sell_regular:
            resultado += "✅ Posso vender pet comum: Sim\n"
        else:
            resultado += "❌ Posso vender pet comum: Não\n"
        
        if can_sell_exotic:
            resultado += "✅ Posso vender pet exótico: Sim\n"
        else:
            resultado += "❌ Posso vender pet exótico: Não\n"
        
        if cannot_sell:
            resultado += "⚠️ Não posso vender nenhum pet(mas tenho aqui um luis )"
        
        self.ui.mostrar_resultado.setText(resultado)

if __name__ == '__main__':
    app = QApplication([])
    janela = MinhaJanela()
    janela.show()
    app.exec()
