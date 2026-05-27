from PySide6.QtWidgets import (QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout)
from PySide6.QtCore import  Qt
from PySide6.QtGui import QPixmap

class AvatarCard(QWidget):
    def __init__(self,nome, nivel,):
        super().__init__()

        self.nome= nome
        self.nivel = nivel
        self.setObjectName("avatarCard")
        self.setup_ui()

    def setup_ui(self):

        imagem = QPixmap("assets/avatares/robo_masculino.png")
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        imagem = imagem.scaled(240, 240)
        lbl_avatar = QLabel()
        
        lbl_avatar.setPixmap(imagem)

        lbl_nome = QLabel(self.nome)
        lbl_nivel= QLabel(f"Nivel {self.nivel}")

        lbl_avatar.setAlignment(Qt.AlignCenter)
        lbl_nome.setAlignment(Qt.AlignCenter)
        lbl_nivel.setAlignment(Qt.AlignCenter)

        lbl_avatar.setMinimumHeight(150)

        layout.addWidget(lbl_avatar)
        layout.addWidget(lbl_nome)
        layout.addWidget(lbl_nivel)
        layout.addWidget(lbl_avatar)
        

        self.setLayout(layout)