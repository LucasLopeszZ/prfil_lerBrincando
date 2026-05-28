from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit
)

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt

from telas.perfil import PerfilWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.avatar_escolhido = "masculino"

        self.setWindowTitle("LerBrincando")
        self.resize(1000, 700)

        self.setup_ui()

    def setup_ui(self):

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout()

        layout_principal.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.setSpacing(20)

        # TÍTULO
        titulo = QLabel("LerBrincando")

        titulo.setStyleSheet("""
            font-size: 42px;
            color: white;
            font-weight: bold;
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # INPUT NOME
        self.input_nome = QLineEdit()

        self.input_nome.setPlaceholderText(
            "Digite seu nome"
        )

        self.input_nome.setFixedWidth(300)
        self.input_nome.setFixedHeight(50)

        # TEXTO AVATAR
        texto_avatar = QLabel(
            "Escolha seu robô"
        )

        texto_avatar.setStyleSheet("""
            font-size: 22px;
            color: white;
            font-weight: bold;
        """)

        # ÁREA AVATARES
        area_avatar = QHBoxLayout()

        # BOTÃO MASCULINO
        btn_masculino = QPushButton("🤖 Menino")

        btn_masculino.clicked.connect(
            self.avatar_masculino
        )

        # BOTÃO FEMININO
        btn_feminino = QPushButton("🤖 Menina")

        btn_feminino.clicked.connect(
            self.avatar_feminino
        )

        area_avatar.addWidget(btn_masculino)
        area_avatar.addWidget(btn_feminino)

        # BOTÃO ENTRAR
        btn_entrar = QPushButton("Entrar")

        btn_entrar.setFixedWidth(220)
        btn_entrar.setFixedHeight(55)

        btn_entrar.clicked.connect(
            self.abrir_perfil
        )

        # ADICIONANDO
        layout_principal.addWidget(titulo)

        layout_principal.addWidget(
            self.input_nome,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(
            texto_avatar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addLayout(area_avatar)

        layout_principal.addWidget(
            btn_entrar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setLayout(layout_principal)

    def avatar_masculino(self):

        self.avatar_escolhido = "masculino"

    def avatar_feminino(self):

        self.avatar_escolhido = "feminino"

    def abrir_perfil(self):

        nome = self.input_nome.text()

        self.perfil = PerfilWindow(nome,self.avatar_escolhido)

        self.perfil.show()

        self.close()