import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logic.questionnaire_processor import QuestionnaireProcessor
from Logic.scoring import calc_meno_score


processor = QuestionnaireProcessor()

# Full sample screening: Q1-Q23
sample_answers = [
    "45-54",
    "Becoming irregular",
    "No",
    "No",

    2, 1, 3, 2,
    1, 2, 2, 1,
    3, 2, 1,
    0, 1, 0, 1,
    2, 1, 2,

    "No"
]

for answer in sample_answers:
    processor.save_answer(answer)
    processor.next_question()

responses = processor.get_responses()
result = calc_meno_score(responses)

print("Screening complete:", processor.is_complete())
print("Raw Score:", result["raw_score"])
print("MenoLikelihood Score:", result["percentage_score"])