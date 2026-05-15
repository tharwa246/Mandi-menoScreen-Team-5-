import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("MenoScreen")
window.resize(500, 300)

layout = QVBoxLayout()

title = QLabel("Welcome to MenoScreen")
layout.addWidget(title)

window.setLayout(layout)
window.show()

sys.exit(app.exec())