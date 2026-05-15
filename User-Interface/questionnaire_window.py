import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class QuestionnaireWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        # loads the Qt Designer UI file
        uic.loadUi("User-Interface/questionnaire_window.ui", self)


# starts the application
app = QApplication(sys.argv)

window = QuestionnaireWindow()

window.show()

sys.exit(app.exec())