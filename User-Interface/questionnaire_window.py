import sys
import os

# Allows this file to import from Logic, Data, and DatabaseTemp folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QButtonGroup, QMessageBox

from Logic.questionnaire_processor import QuestionnaireProcessor
from Logic.scoring import calc_meno_score
from Logic.triage import determine_triage

try:
    from Logic.safety_flags import is_complex_case
except ImportError:
    from Logic.safety_flags import is_complex_case


class QuestionnaireWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Loads the UI design made in Qt Designer
        uic.loadUi("User-Interface/questionnaire_window.ui", self)
        # Forces navigation button styling so text is visible
        self.back_button.setText("Back")
        self.next_button.setText("Next")

        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #673C33;
                 color: #FFFFFF;
                 border: 2px solid #673C33;
                 border-radius: 6px;
                 font-size: 13px;
                 font-weight: bold;
                  padding: 6px;
                }
                """)

        self.next_button.setStyleSheet("""
             QPushButton {
                  background-color: #673C33;
                 color: #FFFFFF;
                 border: 2px solid #673C33;
                 border-radius: 6px;
                 font-size: 13px;
                 font-weight: bold;
                 padding: 6px;
                 }
                """)

        self.back_button.raise_()
        self.next_button.raise_()

        # Forces the MANDI heading to display properly
        self.mandi_label.setText("MANDI")

        self.mandi_label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: transparent;
                font-family: Montserrat;
                font-size: 26px;
                font-weight: bold;
            }
        """)

        # Makes sure the label is visible and above the pink frame
        self.mandi_label.raise_()
        self.mandi_label.show()
    
        self.setStyleSheet("""
        
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

            #section_name_label {
                color: #673C33;
                font-family: Montserrat, Arial;
                font-size: 20px;
                font-weight: 600;
            }

            #content_frame {
                background-color: #F4ECE4;
                border: none;
            }

            #header_frame {
                background-color: #E66C84;
                border: none;
            }

            QPushButton {
                background-color: #673C33;
                color: white;
                border: 2px solid #673C33;
                border-radius: 4px;
                padding: 8px 18px;
                font-family: Montserrat, Arial;
                font-size: 12px;
                font-weight: bold;
            }
                           
      

            QPushButton:hover {
                background-color: #C94A2B;
                color: #F4ECE4;
            }

            QPushButton:pressed {
                background-color: #E66C84;
                color: #F4ECE4;
            }
                           
            QRadioButton {
                color: #673C33;
                font-size: 12px;
                spacing: 8px;
            }

            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #673C33;
                background: white;
            }

            QRadioButton::indicator:checked {
                background-color: #E66C84;
                border: 2px solid #673C33;
            }

            
            QProgressBar {
                background-color: #F4ECE4;
                border: 1px solid #673C33;
                height: 10px;
            }

            QProgressBar::chunk {
                background-color: #E66C84;
            }
        """)


        
        # Creates the questionnaire processor
        self.processor = QuestionnaireProcessor()

        # Stores radio button groups for each question row
        self.button_groups = []

        # Connects UI buttons to Python functions
        self.next_button.clicked.connect(self.next_block)
        self.back_button.clicked.connect(self.previous_block)

        # Loads the first block when the window opens
        self.load_current_block()


    # Creates radio button groups based on the current UI design
    def setup_button_groups(self):

        self.button_groups = []

        rows = [
            [
                self.not_at_all_button,
                self.a_little_button,
                self.quite_a_bit_button,
                self.extremely_button
            ],
            [
                self.not_at_all_button_3,
                self.a_little_button_4,
                self.quite_a_bit_button_4,
                self.extremely_button_4
            ],
            [
                self.not_at_all_button_2,
                self.a_little_button_3,
                self.quite_a_bit_button_3,
                self.extremely_button_3
            ],
            [
                self.not_at_all_button_4,
                self.a_little_button_2,
                self.quite_a_bit_button_2,
                self.extremely_button_2
            ]
        ]

        for row in rows:
            group = QButtonGroup(self)
            group.setExclusive(True)

            for button in row:
                button.setChecked(False)
                group.addButton(button)

            self.button_groups.append(group)


    # Loads the current block title, questions, and answer options onto the UI
    def load_current_block(self):

        self.setup_button_groups()

        block_title = self.processor.get_current_block_title()
        questions = self.processor.get_current_block_questions()

        self.section_name_label.setText(block_title)

        # Updates progress bar
        current_block = self.processor.current_block_index + 1
        total_blocks = 7
        progress_value = int((current_block / total_blocks) * 100)
        self.progress_Bar.setValue(progress_value)

        question_labels = [
            self.first_question,
            self.second_question,
            self.third_question,
            self.fourth_question
        ]

        # Hide all question rows first
        for label in question_labels:
            label.hide()

            # Hide all old buttons and clear previous selections
            for group in self.button_groups:

                # Temporarily allows buttons to be unchecked
                 group.setExclusive(False)

                 for button in group.buttons():

                      button.hide()
                      button.setChecked(False)

                     # Turns exclusivity back on
                 group.setExclusive(True)

        # Show questions for the current block
        for index, question in enumerate(questions):

            if index >= 4:
                continue

            question_labels[index].setText(question["text"])
            question_labels[index].show()

            buttons = self.button_groups[index].buttons()
            options = question["options"]

            for option_index, option in enumerate(options):

                if option_index >= len(buttons):
                    continue

                button = buttons[option_index]

                button.setText(option["text"])
                button.option_value = option["value"]
                button.option_text = option["text"]
                button.question_id = question["id"]

                button.show()

        # Change Next button to Submit on the final block
        if self.processor.current_block_index == total_blocks - 1:
            self.next_button.setText("Submit")
        else:
            self.next_button.setText("Next")


    # Saves answers selected on the current block
    def save_current_block_answers(self):

        questions = self.processor.get_current_block_questions()

        for index, question in enumerate(questions):

            if index >= 4:
                continue

            selected_button = self.button_groups[index].checkedButton()

            if selected_button is None:
                QMessageBox.warning(
                    self,
                    "Missing Answer",
                    "Please answer all questions before continuing."
                )
                return False

            # If option_value is None, save option text instead
            if selected_button.option_value is None:
                answer = selected_button.option_text
            else:
                answer = selected_button.option_value

            self.processor.save_answer(question["id"], answer)

        return True


    # Handles Next / Submit button
    def next_block(self):

        saved_successfully = self.save_current_block_answers()

        if not saved_successfully:
            return

        # If this is the last block, calculate and show results
        if self.processor.current_block_index == 6:
            self.show_results()
            return

        self.processor.next_block()
        self.load_current_block()


    # Handles Back button
    def previous_block(self):

        self.processor.previous_block()
        self.load_current_block()


    # Calculates score, checks safety flag, and displays triage result
    def show_results(self):

        responses = self.processor.get_responses()

        score_result = calc_meno_score(responses)

        percentage_score = score_result["percentage_score"]

        question_23_answer = responses.get(23, "No")
        complex_case = is_complex_case(question_23_answer)

        triage_result = determine_triage(
            percentage_score,
            complex_case
        )

        result_message = (
            f"MenoLikelihood Score: {percentage_score}/100\n\n"
            f"Triage Band: {triage_result['band']}\n\n"
            f"{triage_result['on_screen_message']}\n\n"
            f"Clinician Summary:\n"
            f"{triage_result['clinician_summary_message']}"
        )

        QMessageBox.information(
            self,
            "MenoScreen Result",
            result_message
        )


# Starts the application
app = QApplication(sys.argv)

window = QuestionnaireWindow()
window.show()

sys.exit(app.exec())