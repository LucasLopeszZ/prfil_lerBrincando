from PySide6.QtWidgets import QApplication
from telas.perfil import PerfilWindow
import sys

app = QApplication(sys.argv)

window = PerfilWindow()
window.show()

sys.exit(app.exec())