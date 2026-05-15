import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logic.questionnaire_processor import QuestionnaireProcessor


processor = QuestionnaireProcessor()


print(processor.get_current_question()["text"])


processor.save_answer("45-54")

processor.next_question()


print(processor.get_current_question()["text"])


processor.save_answer("Becoming irregular")

processor.next_question()


print(processor.get_current_question()["text"])


print(processor.get_responses())