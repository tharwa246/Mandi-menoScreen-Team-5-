from dataclasses import dataclass

@dataclass
class PatientResponse:
    question_id: int        #the question number (e.g., 5)
    selected_score: int     # hte severity score of the patient (0, 1, 2, or 3)