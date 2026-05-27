from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from componetes.avatar_card import AvatarCard


class PerfilWindow(QWidget):

    def __init__(self):
        super().__init__()

        # CONFIGURAÇÃO DA JANELA
        self.setWindowTitle("Perfil")
        self.resize(1000, 700)
        self.setObjectName("perfilWindow")

        # ESTILOS
        self.carregar_estilos()

        # FUNDO
        self.criar_fundo()

        # INTERFACE
        self.setup_ui()

    def carregar_estilos(self):

        estilo = ""

        with open("estilos/global.qss", "r", encoding="utf-8") as arquivo:
            estilo += arquivo.read()

        with open("estilos/perfil.qss", "r", encoding="utf-8") as arquivo:
            estilo += arquivo.read()

        self.setStyleSheet(estilo)

    def criar_fundo(self):

        self.fundo = QLabel(self)
        self.fundo.lower()

    def setup_ui(self):

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(50, 30, 30, 30)
        layout_principal.setSpacing(20)

        # TÍTULO
        
        titulo = QLabel("Perfil do jogador")
        titulo.setObjectName("tituloPerfil")

        # CENTRAL
        area_central = QHBoxLayout()
        area_central.setSpacing(40)
        area_central.setAlignment(Qt.AlignTop)

        # AVATAR 
        avatar_card = AvatarCard("Lucas", 7)

        # PAINEL DIREITO
        painel_info = QVBoxLayout()
        painel_info.setSpacing(10)
        painel_info.setAlignment(Qt.AlignTop)

        estrelas = QLabel("⭐⭐⭐☆☆")
        lbl_matematica = QLabel("📘 Matemática")
        barra_matematica = QProgressBar()
        barra_matematica.setValue(80)
        barra_matematica.setFixedWidth(250)

        lbl_portugues = QLabel("📖 Português")
        barra_portugues = QProgressBar()
        barra_portugues.setValue(60)
        barra_portugues.setFixedWidth(250)

        lbl_logica = QLabel("🧠 Lógica")
        barra_logica = QProgressBar()
        barra_logica.setValue(90)
        barra_logica.setFixedWidth(250)
        
        painel_widget = QWidget()
        painel_widget.setFixedHeight(220)
        painel_widget.setObjectName("painelInfo")
        painel_widget.setLayout(painel_info)

        painel_info.addWidget(estrelas)
        painel_info.addWidget(estrelas)

        painel_info.addWidget(lbl_matematica)
        painel_info.addWidget(barra_matematica)

        painel_info.addWidget(lbl_portugues)
        painel_info.addWidget(barra_portugues)

        painel_info.addWidget(lbl_logica)
        painel_info.addWidget(barra_logica)

        #ÁREA CENTRAL
        area_central.addWidget(avatar_card)
        area_central.addWidget(painel_widget)

        # BOTÃO
        voltar = QPushButton("Voltar")

        #LAYOUT PRINCIPAL
        layout_principal.addWidget(titulo)
        layout_principal.addLayout(area_central)
        layout_principal.addSpacing(30)
        layout_principal.addWidget(voltar)

        # DEFININDO LAYOUT
        self.setLayout(layout_principal)
    

    def resizeEvent(self, event):

        imagem = QPixmap("assets/fundo/fundo.png")

        imagem = imagem.scaled(
            self.size(),
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        self.fundo.setPixmap(imagem)

        self.fundo.setGeometry(
            0,
            0,
            self.width(),
            self.height()
        )

        super().resizeEvent(event)