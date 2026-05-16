import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


class ResultsWindow(QMainWindow):

    def __init__(self, percentage_score, triage_result):
        super().__init__()

        # Loads the results screen designed in Qt Designer
        uic.loadUi("User-Interface/results_window.ui", self)

        # Stores score and triage result
        self.percentage_score = percentage_score
        self.triage_result = triage_result

        # Applies Mandi brand styling BEFORE displaying data
        self.apply_brand_styling()

        # Applies result data to the screen
        self.display_results()

        # Connects PDF button for demo
        self.pdfButton.clicked.connect(self.print_patient_handout)


    def apply_brand_styling(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F4ECE4;
            }

            QWidget {
                background-color: #F4ECE4;
                color: #673C33;
                font-family: Montserrat, Arial;
                font-size: 12px;
            }

            QLabel {
                background-color: transparent;
                color: #673C33;
                font-family: Montserrat, Arial;
            }

            QTextEdit {
                background-color: white;
                color: #673C33;
                border: 2px solid #EE8954;
                font-family: Montserrat, Arial;
                font-size: 12px;
            }

            QLineEdit {
                background-color: white;
                color: #673C33;
                border: 2px solid #F5A623;
                font-family: Montserrat, Arial;
                font-size: 20px;
                font-weight: bold;
            }

            QPushButton {
                background-color: #C94A2B;
                color: white;
                border: 2px solid #C94A2B;
                border-radius: 8px;
                padding: 10px;
                font-family: Montserrat, Arial;
                font-size: 12px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #EE8954;
                color: white;
            }

            QProgressBar {
                background-color: white;
                border: 1px solid #673C33;
                height: 10px;
            }

            QProgressBar::chunk {
                background-color: #F5A623;
            }
        """)

        self.mandiHeader.setText("MANDI")
        self.mandiHeader.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
                font-family: Montserrat, Arial;
                font-size: 26px;
                font-weight: bold;
            }
        """)

        self.menolikelihoodLabel.setStyleSheet("""
            QLabel {
                color: #C94A2B;
                background-color: transparent;
                font-family: Montserrat, Arial;
                font-size: 24px;
                font-weight: bold;
            }
        """)

        self.scoreLabel.setStyleSheet("""
            QLabel {
                color: #C94A2B;
                background-color: transparent;
                font-family: Montserrat, Arial;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        self.scoreDisplay.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #673C33;
                border: 2px solid #F5A623;
                font-family: Montserrat, Arial;
                font-size: 20px;
                font-weight: bold;
            }
        """)

        self.messageDisplay.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #673C33;
                border: 2px solid #EE8954;
                font-family: Montserrat, Arial;
                font-size: 12px;
            }
        """)

        self.pdfButton.setStyleSheet("""
            QPushButton {
                background-color: #C94A2B;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-family: Montserrat, Arial;
                font-size: 13px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #EE8954;
            }
        """)


    def display_results(self):

        # Displays the MenoLikelihood score
        self.scoreDisplay.setText(f"{self.percentage_score}%")

        # Updates progress bar to match the score
        self.progressBar.setValue(self.percentage_score)

        # Displays triage message
        result_text = (
            f"Triage Band: {self.triage_result['band']}\n\n"
            f"{self.triage_result['on_screen_message']}\n\n"
            f"Clinician Summary:\n"
            f"{self.triage_result['clinician_summary_message']}"
        )

        self.messageDisplay.setPlainText(result_text)


    def print_patient_handout(self):

        QMessageBox.information(
            self,
            "Patient Handout",
            self.triage_result["patient_handout_message"]
        )


if __name__ == "__main__":

    test_triage = {
        "band": "Possible",
        "score_range": "31-55",
        "colour": "yellow",
        "on_screen_message": "Her symptom profile is consistent with early perimenopause.",
        "clinician_summary_message": "Moderate MenoLikelihood score. Recommend menopause conversation.",
        "patient_handout_message": "What you are feeling has a name. Support is available."
    }

    app = QApplication(sys.argv)

    window = ResultsWindow(50, test_triage)
    window.show()

    sys.exit(app.exec())