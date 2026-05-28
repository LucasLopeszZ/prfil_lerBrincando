from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
    QGraphicsDropShadowEffect
)

from PySide6.QtGui import (
    QPixmap,
    QColor
)

from PySide6.QtCore import Qt

from componetes.avatar_card import AvatarCard


class PerfilWindow(QWidget):

    def __init__(self,nome,avatar):
        super().__init__()
        self.nome= nome
        self.avatar = avatar

        self.setWindowTitle("Perfil")
        self.resize(1000, 700)
        self.setObjectName("perfilWindow")


        self.carregar_estilos()

        self.criar_fundo()

        self.setup_ui()



    def carregar_estilos(self):

        estilo = ""

        with open(
            "estilos/global.qss",
            "r",
            encoding="utf-8"
        ) as arquivo:

            estilo += arquivo.read()

        with open(
            "estilos/perfil.qss",
            "r",
            encoding="utf-8"
        ) as arquivo:

            estilo += arquivo.read()

        self.setStyleSheet(estilo)



    def criar_fundo(self):

        self.fundo = QLabel(self)
        self.fundo.lower()



    def criar_titulo(self):

        titulo = QLabel("Perfil do Jogador")

        titulo.setObjectName("tituloPerfil")

        return titulo


    def criar_avatar(self):

        avatar_card = AvatarCard(self.nome, 7,self.avatar)

        return avatar_card



    def criar_botao_voltar(self):

        voltar = QPushButton("Voltar ao jogo")

        voltar.setFixedWidth(220)
        voltar.setFixedHeight(55)

        return voltar


    #INFORMAÇÕES


    def criar_painel_info(self):

        #INTERNO
        layout_info = QVBoxLayout()

        layout_info.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        layout_info.setSpacing(18)

        layout_info.setContentsMargins(
            20,
            20,
            20,
            20
        )

        lbl_id = QLabel("ID:")

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

        # ESTRELAS
        estrelas = QLabel("⭐⭐⭐☆☆")

        estrelas.setObjectName("lblEstrelas")


        #ELEMENTOS
        layout_info.addWidget(lbl_id)

        layout_info.addWidget(lbl_matematica)
        layout_info.addWidget(barra_matematica)

        layout_info.addWidget(lbl_portugues)
        layout_info.addWidget(barra_portugues)

        layout_info.addWidget(lbl_logica)
        layout_info.addWidget(barra_logica)

        layout_info.addWidget(estrelas)

        layout_info.addSpacing(15)



        painel_widget = QWidget()

        painel_widget.setObjectName("painelInfo")

        painel_widget.setFixedWidth(420)
        painel_widget.setFixedHeight(320)

        painel_widget.setLayout(layout_info)

        sombra_painel = QGraphicsDropShadowEffect()

        sombra_painel.setBlurRadius(35)
        sombra_painel.setXOffset(0)
        sombra_painel.setYOffset(8)

        sombra_painel.setColor(
            QColor(0, 0, 0, 80)
        )

        painel_widget.setGraphicsEffect(
            sombra_painel
        )

        return painel_widget

    # INTERFACE PRI

    def setup_ui(self):

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout()

        layout_principal.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.setContentsMargins(
            50,
            30,
            50,
            30
        )

        layout_principal.setSpacing(20)

        titulo = self.criar_titulo()

        avatar = self.criar_avatar()

        painel_info = self.criar_painel_info()

        botao_voltar = self.criar_botao_voltar()

        card_principal = QWidget()

        card_principal.setObjectName(
            "cardPrincipal"
        )

        layout_card = QHBoxLayout()

        layout_card.setContentsMargins(
            40,
            40,
            40,
            40
        )

        layout_card.setSpacing(50)

        layout_card.addWidget(avatar)

        layout_card.addWidget(painel_info)

        card_principal.setLayout(layout_card)

        sombra_card = QGraphicsDropShadowEffect()

        sombra_card.setBlurRadius(40)

        sombra_card.setXOffset(0)

        sombra_card.setYOffset(10)

        sombra_card.setColor(
            QColor(0, 0, 0, 90)
        )

        card_principal.setGraphicsEffect(
            sombra_card
        )

        
        layout_principal.addWidget(titulo)

        layout_principal.addWidget(
            card_principal,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(
            botao_voltar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

       
        self.setLayout(layout_principal)

    #FUNDO


    def resizeEvent(self, event):

        imagem = QPixmap(
            "assets/fundo/fundo.png"
        )

        imagem = imagem.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        self.fundo.setPixmap(imagem)

        self.fundo.setGeometry(
            0,
            0,
            self.width(),
            self.height()
        )

        super().resizeEvent(event)