import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from DatabaseTemp.question_repository import get_questions_from_database

questions = get_questions_from_database()

print("Total database questions:", len(questions))
print("First question:", questions[0])
print("Last question:", questions[-1])