import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logic.questionnaire_processor import QuestionnaireProcessor
from Logic.scoring import calc_meno_score


processor = QuestionnaireProcessor()

# Q1-Q4: context questions
context_answers = ["45-54", "Becoming irregular", "No", "No"]

for answer in context_answers:
    processor.save_answer(answer)
    processor.next_question()

# Q5-Q22: scored questions
sample_scores = [2, 1, 3, 2, 1, 2, 2, 1, 3, 2, 1, 0, 1, 0, 1, 2, 1, 2]

for score in sample_scores:
    processor.save_answer(score)
    processor.next_question()

# Q23: safety flag
processor.save_answer("No")

responses = processor.get_responses()
result = calc_meno_score(responses)

#print("Responses:", responses)
print("Raw Score:", result["raw_score"])
print("MenoLikelihood Score:", result["percentage_score"])