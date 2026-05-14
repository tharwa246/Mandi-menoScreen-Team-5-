import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Data.questions import questions

print("Total questions:", len(questions))

context_questions = [q for q in questions if q["type"] == "context"]
scored_questions = [q for q in questions if q["type"] == "scored"]
safety_questions = [q for q in questions if q["type"] == "safety_flag"]

print("Context questions:", len(context_questions))
print("Scored questions:", len(scored_questions))
print("Safety flag questions:", len(safety_questions))

print("\nFirst question:")
print(questions[0])

print("\nLast question:")
print(questions[-1])
