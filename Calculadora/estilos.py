# ============================================================
# ESTILOS / TEMAS - Calculadora
# ============================================================
# Este ficheiro contém todos os estilos da aplicação.
# Para mudar de tema, chama: aplicar_tema(ui, janela, "claro") ou aplicar_tema(ui, janela, "escuro")
# ============================================================

# --- CORES POR TEMA ---
TEMAS = {
    "claro": {
        # Fundo geral
        "fundo_janela": "#f0f0f0",
        "fundo_widget": "white",
        
        # Texto
        "texto_principal": "#333",
        "texto_secundario": "#555",
        "texto_escuro": "#000",
        "texto_claro": "white",
        "texto_info": "#444",
        
        # Botões numéricos
        "botao_num_fundo": "white",
        "botao_num_texto": "#333",
        "botao_num_borda": "#ddd",
        "botao_num_hover": "#f5f5f5",
        "botao_num_hover_borda": "#ccc",
        
        # Botões operadores (laranja/vermelho)
        "botao_op_fundo": "#ff5032",
        "botao_op_hover": "#ff7052",
        
        # Botão apagar (rosa)
        "botao_apagar_fundo": "#ff8a80",
        "botao_apagar_hover": "#ff7052",
        
        # Botão apagar tudo (vermelho)
        "botao_ce_fundo": "rgb(235, 50, 10)",
        "botao_ce_hover": "#ff7052",
        
        # Botão resultado
        "botao_resultado_fundo": "rgb(255, 170, 127)",
        "botao_resultado_hover": "#ff7052",
        
        # LineEdit (campos de texto)
        "input_fundo": "white",
        "input_texto": "#000",
        "input_borda": "#ddd",
        "input_foco_borda": "#ff7052",
        "input_estilo_borda": "2px solid #ddd",
        "input_estilo_borda_foco": "2px solid #ff7052",
        "input_radius": "border-radius: 8px;",
        
        # Display da calculadora
        "display_fundo": "transparent",
        "display_texto": "#000000",
        "display_borda": "#cccccc",
        
        # ComboBox
        "combo_fundo": "white",
        "combo_texto": "#333",
        "combo_borda": "#ddd",
        "combo_item_selecionado": "#ff7052",
        
        # DateEdit
        "dateedit_fundo": "white",
        "dateedit_texto": "black",
        "dateedit_borda": "#ddd",
        "dateedit_hover_borda": "#ff8c42",
        
        # SpinBox
        "spinbox_fundo": "white",
        "spinbox_texto": "#333",
        "spinbox_selecao": "#ff8c42",
        
        # RadioButton
        "radio_checked": "#ff8c42",
        "radio_unchecked_fundo": "white",
        "radio_unchecked_borda": "#ccc",
        
        # Menu
        "menu_fundo": "#f0f0f0",
        "menu_borda": "#cccccc",
        "menu_item_hover": "#ff5032",
        
        # ToolButton
        "toolbutton_texto": "#000",
        "toolbutton_hover_fundo": "#e0e0e0",
        "toolbutton_hover_texto": "#000",
        
        # Labels especiais
        "label_erro_fundo": "#ffe6e6",
        "label_erro_texto": "#d32f2f",
        "label_erro_borda": "#d32f2f",
        "label_resultado_texto": "#333",
        "label_info_borda": "#ff8c42",
        "label_destaque": "#ff7052",
        
        # Botões data
        "botao_data_fundo": "white",
        "botao_data_texto": "#333",
        "botao_data_borda": "#ddd",
        "botao_data_hover": "#ff8c42",
        
        # Calendário
        "calendario_fundo": "white",
        "calendario_nav_fundo": "#f0f0f0",
        "calendario_nav_texto": "black",
        "calendario_nav_hover": "#ff8c42",
        "calendario_spinbox_fundo": "#f0f0f0",
        "calendario_spinbox_texto": "black",
        "calendario_grid_fundo": "white",
        "calendario_grid_texto": "black",
        "calendario_selecao": "#ff8c42",
        "calendario_grid_linha": "#e0e0e0",
        "calendario_header_fundo": "#f5f5f5",
        "calendario_dias_desativados": "#cccccc",
        
        # GroupBox
        "groupbox_fundo": "transparent",
        
        # Símbolo moeda
        "simbolo_fundo": "transparent",
    },
    
    "escuro": {
        # Fundo geral
        "fundo_janela": "#1e1e1e",
        "fundo_widget": "#2d2d2d",
        
        # Texto
        "texto_principal": "#e0e0e0",
        "texto_secundario": "#aaa",
        "texto_escuro": "#ffffff",
        "texto_claro": "white",
        "texto_info": "#bbb",
        
        # Botões numéricos
        "botao_num_fundo": "#3a3a3a",
        "botao_num_texto": "#e0e0e0",
        "botao_num_borda": "#555",
        "botao_num_hover": "#4a4a4a",
        "botao_num_hover_borda": "#666",
        
        # Botões operadores
        "botao_op_fundo": "#ff5032",
        "botao_op_hover": "#ff7052",
        
        # Botão apagar
        "botao_apagar_fundo": "#d32f2f",
        "botao_apagar_hover": "#ff5252",
        
        # Botão apagar tudo
        "botao_ce_fundo": "#b71c1c",
        "botao_ce_hover": "#d32f2f",
        
        # Botão resultado
        "botao_resultado_fundo": "#ff8c42",
        "botao_resultado_hover": "#ff7052",
        
        # LineEdit
        "input_fundo": "transparent",
        "input_texto": "#ffffff",
        "input_borda": "#555",
        "input_foco_borda": "#ff7052",
        "input_estilo_borda": "none; border-bottom: 2px solid #555",
        "input_estilo_borda_foco": "none; border-bottom: 2px solid #ff7052",
        "input_radius": "",
        
        # Display
        "display_fundo": "transparent",
        "display_texto": "#ffffff",
        "display_borda": "#555",
        
        # ComboBox
        "combo_fundo": "#3a3a3a",
        "combo_texto": "#e0e0e0",
        "combo_borda": "#555",
        "combo_item_selecionado": "#ff7052",
        
        # DateEdit
        "dateedit_fundo": "#3a3a3a",
        "dateedit_texto": "#e0e0e0",
        "dateedit_borda": "#555",
        "dateedit_hover_borda": "#ff8c42",
        
        # SpinBox
        "spinbox_fundo": "#3a3a3a",
        "spinbox_texto": "#e0e0e0",
        "spinbox_selecao": "#ff8c42",
        
        # RadioButton
        "radio_checked": "#ff8c42",
        "radio_unchecked_fundo": "#3a3a3a",
        "radio_unchecked_borda": "#666",
        
        # Menu
        "menu_fundo": "#2d2d2d",
        "menu_borda": "#555",
        "menu_item_hover": "#ff5032",
        
        # ToolButton
        "toolbutton_texto": "#fff",
        "toolbutton_hover_fundo": "#4a4a4a",
        "toolbutton_hover_texto": "#fff",
        
        # Labels especiais
        "label_erro_fundo": "#4a1c1c",
        "label_erro_texto": "#ff8a80",
        "label_erro_borda": "#d32f2f",
        "label_resultado_texto": "#e0e0e0",
        "label_info_borda": "#ff8c42",
        "label_destaque": "#ff7052",
        
        # Botões data
        "botao_data_fundo": "#3a3a3a",
        "botao_data_texto": "#e0e0e0",
        "botao_data_borda": "#555",
        "botao_data_hover": "#ff8c42",
        
        # Calendário
        "calendario_fundo": "#2d2d2d",
        "calendario_nav_fundo": "#3a3a3a",
        "calendario_nav_texto": "#e0e0e0",
        "calendario_nav_hover": "#ff8c42",
        "calendario_spinbox_fundo": "#3a3a3a",
        "calendario_spinbox_texto": "#e0e0e0",
        "calendario_grid_fundo": "#2d2d2d",
        "calendario_grid_texto": "#e0e0e0",
        "calendario_selecao": "#ff8c42",
        "calendario_grid_linha": "#444",
        "calendario_header_fundo": "#3a3a3a",
        "calendario_dias_desativados": "#666",
        
        # GroupBox
        "groupbox_fundo": "transparent",
        
        # Símbolo moeda
        "simbolo_fundo": "transparent",
    }
}


def gerar_estilos(tema, caminho_seta, caminho_calen):
    """Gera todos os estilos CSS com base no tema escolhido."""
    c = TEMAS[tema]
    
    estilos = {
        # --- JANELA PRINCIPAL ---
        "janela": f"background-color: {c['fundo_janela']};",
        
        # --- BOTÕES NUMÉRICOS (0-9) ---
        "botao_numero": f"""
            QPushButton {{
                background-color: {c['botao_num_fundo']};
                color: {c['botao_num_texto']};
                font-size: 20px;
                font-weight: bold;
                border: 1px solid {c['botao_num_borda']};
                border-radius: 8px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {c['botao_num_hover']};
                border: 1px solid {c['botao_num_hover_borda']};
            }}
        """,
        
        # --- BOTÕES OPERADORES (+, -, *, /, %, ±, .) ---
        "botao_operador": f"""
            QPushButton {{
                background-color: {c['botao_op_fundo']};
                color: {c['texto_claro']};
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {c['botao_op_hover']};
            }}
        """,
        
        # --- BOTÃO APAGAR (←) ---
        "botao_apagar": f"""
            QPushButton {{
                background-color: {c['botao_apagar_fundo']};
                color: {c['texto_claro']};
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {c['botao_apagar_hover']};
            }}
            font-size: 24px !important;
        """,
        
        # --- BOTÃO APAGAR TUDO (CE) ---
        "botao_ce": f"""
            QPushButton {{
                background-color: {c['botao_ce_fundo']};
                color: {c['texto_claro']};
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {c['botao_ce_hover']};
            }}
        """,
        
        # --- BOTÃO RESULTADO (=) ---
        "botao_resultado": f"""
            QPushButton {{
                background-color: {c['botao_resultado_fundo']};
                color: {c['texto_claro']};
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: {c['botao_resultado_hover']};
            }}
        """,
        
        # --- DISPLAY DA CALCULADORA ---
        "display": f"""
            QLineEdit {{
                background-color: {c['display_fundo']};
                color: {c['display_texto']};
                font-size: 72px;
                font-weight: bold;
                border: 2px solid {c['display_borda']};
                border-radius: 5px;
                padding: 10px;
            }}
        """,
        
        # --- CAMPOS DE ENTRADA (LineEdit conversões) ---
        "input_conversao": f"""
            QLineEdit {{
                background-color: {c['input_fundo']};
                color: {c['input_texto']};
                font-size: 42px;
                font-weight: bold;
                border: {c['input_estilo_borda']};
                {c['input_radius']}
                padding: 10px;
            }}
            QLineEdit:focus {{
                border: {c['input_estilo_borda_foco']};
                {c['input_radius']}
            }}
        """,
        
        # --- COMBOBOX ---
        "combo": f"""
            QComboBox {{
                background-color: {c['combo_fundo']};
                color: {c['combo_texto']};
                font-size: 11px;
                border: 2px solid {c['combo_borda']};
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
        """,
        
        # --- COMBOBOX POPUP (lista dropdown) ---
        "combo_popup_window": f"""
            QWidget {{
                background-color: {c['combo_fundo']};
                border: 2px solid {c['combo_borda']};
                border-radius: 8px;
            }}
        """,
        
        "combo_popup_list": f"""
            QListView {{
                background-color: {c['combo_fundo']};
                color: {c['combo_texto']};
                border: 1px solid {c['combo_borda']};
                outline: 0;
            }}
            QListView::item {{
                padding: 5px;
                outline: 0;
                color: {c['combo_texto']};
            }}
            QListView::item:selected {{
                background-color: {c['combo_item_selecionado']};
                color: {c['texto_claro']};
            }}
        """,
        
        # --- DATEEDIT ---
        "dateedit": f"""
            QDateEdit {{
                background-color: {c['dateedit_fundo']};
                color: {c['dateedit_texto']};
                border: 2px solid {c['dateedit_borda']};
                border-radius: 8px;
                padding: 5px 8px;
                font-size: 14px;
                height: 35px;
            }}
            QDateEdit:hover {{
                border: 2px solid {c['dateedit_hover_borda']};
            }}
            QDateEdit:focus {{
                border: 2px solid {c['dateedit_hover_borda']};
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
        """,
        
        # --- SPINBOX ---
        "spinbox": f"""
            QSpinBox {{
                background-color: {c['spinbox_fundo']};
                color: {c['spinbox_texto']};
                font-size: 14px;
                selection-background-color: {c['spinbox_selecao']};
                selection-color: {c['texto_claro']};
            }}
        """,
        
        # --- RADIOBUTTON ---
        "radiobutton": f"""
            QRadioButton {{
                color: {c['texto_principal']};
            }}
            QRadioButton::indicator {{
                width: 11px;
                height: 11px;
                border-radius: 7px;
            }}
            QRadioButton::indicator:checked {{
                background-color: {c['radio_checked']};
                border: 2px solid {c['radio_checked']};
            }}
            QRadioButton::indicator:unchecked {{
                background-color: {c['radio_unchecked_fundo']};
                border: 2px solid {c['radio_unchecked_borda']};
            }}
        """,
        
        # --- MENU ---
        "menu": f"""
            QMenu {{
                background-color: {c['menu_fundo']};
                border: 2px solid {c['menu_borda']};
                border-radius: 8px;
                padding: 5px;
            }}
            QMenu::item {{
                padding: 8px 25px;
                border-radius: 5px;
                color: {c['texto_principal']};
            }}
            QMenu::item:selected {{
                background-color: {c['menu_item_hover']};
                color: {c['texto_claro']};
            }}
        """,
        
        # --- TOOLBUTTON (≡ menu) ---
        "toolbutton": f"""
            QToolButton {{
                color: {c['toolbutton_texto']};
            }}
            QToolButton:hover {{
                color: {c['toolbutton_hover_texto']};
                background-color: {c['toolbutton_hover_fundo']};
                border-radius: 5px;
            }}
        """,
        
        # --- LABELS ESPECIAIS ---
        "label_erro": f"""
            QLabel {{
                background-color: {c['label_erro_fundo']};
                color: {c['label_erro_texto']};
                border: 2px solid {c['label_erro_borda']};
                border-radius: 8px;
                padding: 10px;
                font-size: 11px;
                font-weight: bold;
            }}
        """,
        
        "label_info": f"""
            QLabel {{
                background-color: transparent;
                color: {c['texto_secundario']};
                border-left: 3px solid {c['label_info_borda']};
                padding: 5px 10px;
                font-size: 12px;
            }}
        """,
        
        "label_resultado": f"""
            QLabel {{
                background-color: transparent;
                color: {c['label_resultado_texto']};
                border: none;
                padding: 5px;
                font-size: 13px;
                font-weight: bold;
            }}
        """,
        
        # --- BOTÕES DATA ATUAL ---
        "botao_data": f"""
            QPushButton {{
                background-color: {c['botao_data_fundo']};
                color: {c['botao_data_texto']};
                border: 2px solid {c['botao_data_borda']};
                border-radius: 8px;
                padding: 8px 15px;
                font-size: 11px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {c['botao_data_hover']};
                color: {c['texto_claro']};
                border: 2px solid {c['botao_data_hover']};
            }}
        """,
        
        "botao_data_link": f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                color: {c['texto_principal']};
                font-size: 12px;
                font-weight: bold;
                padding: 5px;
            }}
            QPushButton:pressed {{
                color: #e67a32;
            }}
        """,
        
        # --- CALENDÁRIO ---
        "calendario": f"""
            QCalendarWidget {{
                background-color: {c['calendario_fundo']};
            }}
            QCalendarWidget QToolButton {{
                color: {c['calendario_nav_texto']};
                background-color: {c['calendario_nav_fundo']};
                border: none;
                border-radius: 4px;
                padding: 5px;
                margin: 2px;
            }}
            QCalendarWidget QToolButton:hover {{
                background-color: {c['calendario_nav_hover']};
                color: {c['texto_claro']};
            }}
            QCalendarWidget QSpinBox {{
                background-color: {c['calendario_spinbox_fundo']};
                color: {c['calendario_spinbox_texto']};
                selection-background-color: {c['calendario_selecao']};
                selection-color: {c['texto_claro']};
                border: 1px solid {c['combo_borda']};
            }}
            QCalendarWidget QMenu {{
                background-color: {c['calendario_fundo']};
                color: {c['calendario_grid_texto']};
            }}
            QCalendarWidget QTableView {{
                background-color: {c['calendario_grid_fundo']};
                color: {c['calendario_grid_texto']};
                selection-background-color: {c['calendario_selecao']};
                selection-color: {c['texto_claro']};
                border: none;
                gridline-color: {c['calendario_grid_linha']};
            }}
            QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: {c['calendario_header_fundo']};
            }}
            QCalendarWidget QAbstractItemView:enabled {{
                color: {c['calendario_grid_texto']};
            }}
            QCalendarWidget QAbstractItemView:disabled {{
                color: {c['calendario_dias_desativados']};
            }}
        """,
        
        # --- GROUPBOX ---
        "groupbox": f"""
            QGroupBox {{
                background-color: {c['groupbox_fundo']};
                border: none;
            }}
        """,
        
        # --- SÍMBOLO MOEDA ---
        "simbolo": f"""
            border: none;
            background: {c['simbolo_fundo']};
            color: #999;
            font-size: 32px;
        """,
        
        # --- LABELS GENÉRICAS (cor do texto) ---
        "label_geral": f"""
            color: {c['texto_principal']};
        """,
        
        # --- LABELS ACERCA DE ---
        "label_destaque": f"""
            font-size: 12px;
            font-weight: bold;
            color: {c['label_destaque']};
        """,
        
        "label_descricao": f"""
            font-size: 12px;
            color: {c['texto_info']};
        """,
        
        "label_link": f"""
            font-size: 12px;
            color: {c['label_destaque']};
        """,
    }
    
    return estilos


def aplicar_tema(ui, janela, tema, caminho_seta, caminho_calen):
    """Aplica o tema a todos os widgets da aplicação."""
    
    e = gerar_estilos(tema, caminho_seta, caminho_calen)
    
    # --- JANELA ---
    janela.setStyleSheet(e["janela"])
    
    # --- DISPLAY CALCULADORA ---
    ui.fonte_display.setStyleSheet(e["display"])
    
    # --- BOTÕES NUMÉRICOS ---
    botoes_numero = [
        # Calculadora
        ui.numero_0, ui.numero_1, ui.numero_2, ui.numero_3, ui.numero_4,
        ui.numero_5, ui.numero_6, ui.numero_7, ui.numero_8, ui.numero_9,
        # Distância
        ui.numero_0_dist, ui.numero_1_dist, ui.numero_2_dist, ui.numero_3_dist,
        ui.numero_4_dist, ui.numero_5_dist, ui.numero_6_dist, ui.numero_7_dist,
        ui.numero_8_dist, ui.numero_9_dist,
        # Temperatura
        ui.numero_0_temp, ui.numero_1_temp, ui.numero_2_temp, ui.numero_3_temp,
        ui.numero_4_temp, ui.numero_5_temp, ui.numero_6_temp, ui.numero_7_temp,
        ui.numero_8_temp, ui.numero_9_temp,
        # Tempo
        ui.numero_0_tempo, ui.numero_1_tempo, ui.numero_2_tempo, ui.numero_3_tempo,
        ui.numero_4_tempo, ui.numero_5_tempo, ui.numero_6_tempo, ui.numero_7_tempo,
        ui.numero_8_tempo, ui.numero_9_tempo,
        # Moedas
        ui.numero_0_moedas, ui.numero_1_moedas, ui.numero_2_moedas, ui.numero_3_moedas,
        ui.numero_4_moedas, ui.numero_5_moedas, ui.numero_6_moedas, ui.numero_7_moedas,
        ui.numero_8_moedas, ui.numero_9_moedas,
        # Velocidade
        ui.numero_0_velocidade, ui.numero_1_velocidade, ui.numero_2_velocidade,
        ui.numero_3_velocidade, ui.numero_4_velocidade, ui.numero_5_velocidade,
        ui.numero_6_velocidade, ui.numero_7_velocidade, ui.numero_8_velocidade,
        ui.numero_9_velocidade,
    ]
    for botao in botoes_numero:
        botao.setStyleSheet(e["botao_numero"])
    
    # --- BOTÕES OPERADORES ---
    botoes_operador = [
        ui.botao_decimal, ui.operador_menos, ui.operador_percentagem,
        ui.operador_dividir, ui.operador_mais, ui.botao_sinal,
        ui.operador_multiplicar,
    ]
    for botao in botoes_operador:
        botao.setStyleSheet(e["botao_operador"])
    
    # --- BOTÕES APAGAR ---
    botoes_apagar = [
        ui.botao_apagar, ui.botao_apagar_dist, ui.botao_apagar_temp,
        ui.botao_apagar_tempo, ui.botao_apagar_moedas, ui.botao_apagar_velocidade,
    ]
    # Inclui os _temp_9 se existirem
    for nome in ['botao_apagar_temp_9']:
        if hasattr(ui, nome):
            botoes_apagar.append(getattr(ui, nome))
    for botao in botoes_apagar:
        botao.setStyleSheet(e["botao_apagar"])
    
    # --- BOTÕES CE ---
    botoes_ce = [
        ui.botao_apagar_tudo, ui.botao_apagar_tudo_dist, ui.botao_apagar_tudo_temp,
        ui.botao_apagar_tudo_tempo, ui.botao_apagar_tudo_moedas,
        ui.botao_apagar_tudo_velocidade,
    ]
    for nome in ['botao_apagar_tudo_temp_9']:
        if hasattr(ui, nome):
            botoes_ce.append(getattr(ui, nome))
    for botao in botoes_ce:
        botao.setStyleSheet(e["botao_ce"])
    
    # --- BOTÃO RESULTADO ---
    ui.botao_resultado.setStyleSheet(e["botao_resultado"])
    
    # --- CAMPOS DE ENTRADA ---
    inputs = [
        ui.distancia_1, ui.distancia_2,
        ui.temperatura_1, ui.temperatura_2,
        ui.tempo_1, ui.tempo_2,
        ui.valor_origem, ui.valor_destino,
        ui.velocidade_origem, ui.velocidade_destino,
    ]
    for inp in inputs:
        inp.setStyleSheet(e["input_conversao"])
    
    # --- COMBOBOXES ---
    combos = [
        ui.combo_distancia_1, ui.combo_distancia_2,
        ui.combo_temp_1, ui.combo_temp_2,
        ui.combo_tempo_1, ui.combo_tempo_2,
        ui.combo_datas_1, ui.combo_datas_2,
        ui.combo_moeda_1, ui.combo_moeda_2,
        ui.combo_velocidades_origem, ui.combo_velocidades_destino,
    ]
    if hasattr(ui, 'combo_tema'):
        combos.append(ui.combo_tema)
    for combo in combos:
        combo.setStyleSheet(e["combo"])
        combo.view().window().setStyleSheet(e["combo_popup_window"])
        combo.view().setStyleSheet(e["combo_popup_list"])
    
    # --- DATEEDITS ---
    dateedits = [ui.date_edit_1, ui.date_edit_2, ui.date_edit_3]
    for de in dateedits:
        de.setStyleSheet(e["dateedit"])
        de.calendarWidget().setStyleSheet(e["calendario"])
    
    # --- SPINBOXES ---
    spinboxes = [ui.spinbox_meses, ui.spinbox_dias, ui.spinbox_anos, ui.spinBox_casas_decimais]
    for sb in spinboxes:
        sb.setStyleSheet(e["spinbox"])
    
    # --- RADIOBUTTONS ---
    ui.radio_adicionar.setStyleSheet(e["radiobutton"])
    ui.radio_subtrair.setStyleSheet(e["radiobutton"])
    
    # --- TOOLBUTTONS ---
    toolbuttons = [
        ui.toolButton_0, ui.toolButton_1, ui.toolButton_2, ui.toolButton_3,
        ui.toolButton_4, ui.toolButton_5, ui.toolButton_6, ui.toolButton_7,
        ui.toolButton_8, ui.toolButton_9,
    ]
    for tb in toolbuttons:
        tb.setStyleSheet(e["toolbutton"])
    
    # --- LABELS ESPECIAIS ---
    ui.label_erro.setStyleSheet(e["label_erro"])
    ui.label_dias.setStyleSheet(e["label_info"])
    ui.label_horas.setStyleSheet(e["label_info"])
    ui.label_semanas.setStyleSheet(e["label_info"])
    ui.label_resultado.setStyleSheet(e["label_resultado"])
    
    # --- LABELS GENÉRICAS (títulos, textos, etc.) ---
    labels_gerais = [
        'label', 'label_3', 'label_4', 'label_5', 'label_6',
        'label_7', 'label_8', 'label_9',
        'label_calculadora', 'label_cambio', 'label_dataup',
        'label_distancias', 'label_distancias_2', 'label_distancias_3',
        'label_distancias_4', 'label_distancias_5', 'label_distancias_6',
        'label_distancias_7', 'label_distancias_8', 'label_distancias_9',
        'label_final', 'label_tema',
    ]
    for nome in labels_gerais:
        if hasattr(ui, nome):
            getattr(ui, nome).setStyleSheet(e["label_geral"])
    
    # --- BOTÕES DATA ---
    ui.botao_data_atual_2.setStyleSheet(e["botao_data"])
    ui.botao_data_atual_3.setStyleSheet(e["botao_data"])
    ui.botao_data_atual.setStyleSheet(e["botao_data_link"])
    ui.botao_update.setStyleSheet(e["botao_data_link"])
    
    # --- GROUPBOX ---
    ui.groupBox.setStyleSheet(e["groupbox"])
    
    # --- SÍMBOLO MOEDA ---
    ui.simbolo_origem.setStyleSheet(e["simbolo"])
    if hasattr(ui, 'simbolo_destino'):
        ui.simbolo_destino.setStyleSheet(e["simbolo"])
    
    # --- LABELS ACERCA DE ---
    if hasattr(ui, 'label_10'):
        ui.label_10.setStyleSheet(e["label_destaque"])
    if hasattr(ui, 'label_11'):
        ui.label_11.setStyleSheet(e["label_descricao"])
    if hasattr(ui, 'label_link'):
        ui.label_link.setStyleSheet(e["label_link"])
