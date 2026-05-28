from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor


class AvatarCard(QWidget):

    def __init__(self, nome, nivel,avatar):
        super().__init__()

        # DADOS
        self.avatar = avatar
        self.nome = nome
        self.nivel = nivel

        # CONFIGURAÇÃO DO CARD
        self.setObjectName("avatarCard")
        self.setFixedWidth(260)

        # INTERFACE
        self.setup_ui()

        # SOMBRA
        self.adicionar_sombra()

    def setup_ui(self):

        # LAYOUT PRINCIPAL
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 20, 20, 20)
        layout.setSpacing(10)

        # IMAGEM DO AVATAR
        if self.avatar == "masculino":

            caminho_avatar = (
            "assets/avatares/robo_masculino.png"
            )

        else:
            caminho_avatar = (
            "assets/avatares/robo_feminino.png"
            )

        imagem = QPixmap(caminho_avatar)
        imagem = imagem.scaled(
            240,
            240,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        lbl_avatar = QLabel()
        lbl_avatar.setPixmap(imagem)
        lbl_avatar.setAlignment(Qt.AlignCenter)

        # NOME
        lbl_nome = QLabel(self.nome)
        lbl_nome.setAlignment(Qt.AlignCenter)

        # NÍVEL
        lbl_nivel = QLabel(f"Nível {self.nivel}")
        lbl_nivel.setAlignment(Qt.AlignCenter)

        # PLACA
        placa_widget = QWidget()
        placa_widget.setObjectName("placaAvatar")

        layout_placa = QVBoxLayout()

        layout_placa.setContentsMargins(15, 10, 15, 10)
        layout_placa.setSpacing(5)

        placa_widget.setLayout(layout_placa)

        # ADICIONANDO TEXTO
        layout_placa.addWidget(lbl_nome)
        layout_placa.addWidget(lbl_nivel)

        # ADICIONANDO NO LAYOUT PRINCIPAL
        layout.addWidget(lbl_avatar)
        layout.addWidget(placa_widget)

        # DEFININDO LAYOUT
        self.setLayout(layout)

    def adicionar_sombra(self):

        sombra = QGraphicsDropShadowEffect()

        sombra.setBlurRadius(35)
        sombra.setXOffset(0)
        sombra.setYOffset(8)

        sombra.setColor(QColor(0, 0, 0, 80))

        self.setGraphicsEffect(sombra)