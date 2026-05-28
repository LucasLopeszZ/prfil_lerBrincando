from PySide6.QtWidgets import QApplication

from telas.login import LoginWindow

app = QApplication([])

window = LoginWindow()

window.show()

app.exec()