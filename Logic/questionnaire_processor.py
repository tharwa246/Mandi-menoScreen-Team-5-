from DatabaseTemp.question_repository import get_questions_from_database

questions = get_questions_from_database()
# loads questionnaire data from the SQLite database


# list of questionnaire blocks in the order they should appear - 
# Hermi approved blocks per page instead of 1 question per page

question_blocks = [
    {"block_number": 1, "block_name": "Patient Context"},
    {"block_number": 2, "block_name": "Cognitive and Mood"},
    {"block_number": 3, "block_name": "Vasomotor and Sleep"},
    {"block_number": 4, "block_name": "Musculoskeletal and Energy"},
    {"block_number": 5, "block_name": "Urogenital and Sexual Health"},
    {"block_number": 6, "block_name": "Quality of Life Impact"},
    {"block_number": 7, "block_name": "Safety Flag"}
]


class QuestionnaireProcessor:

    # sets up the questionnaire processor
    # starts at Block 1
    # creates an empty dictionary to store patient responses
    def __init__(self):
        self.current_block_index = 0
        self.responses = {}

    # returns the current block information
    def get_current_block(self):
        return question_blocks[self.current_block_index]

    # returns the current block name for display
    # e.g. Block 1: Patient Context
    def get_current_block_title(self):
        current_block = self.get_current_block()
        return f"Block {current_block['block_number']}: {current_block['block_name']}"

    # returns all questions that belong to the current block
    def get_current_block_questions(self):
        current_block = self.get_current_block()
        current_block_name = current_block["block_name"]

        return [
            question for question in questions
            if question["category"] == current_block_name
        ]

    # saves one answer using the question id as the key
    # does not allow for duplicated answers if the user goes back to change an answer
    #why dictionary is used
    def save_answer(self, question_id, answer):
        self.responses[question_id] = answer

    # saves all answers from the current block/page
    # e.g. {1: "45-54", 2: "Becoming irregular"}
    def save_block_answers(self, block_answers):
        for question_id, answer in block_answers.items():
            self.save_answer(question_id, answer)

    # moves to the next block/page
    # does not aallow the system from going past the final block
    def next_block(self):
        if self.current_block_index < len(question_blocks) - 1:
            self.current_block_index += 1
            return self.get_current_block_questions()

        return None

    # moves back to the previous block/page
    # does not allow the system from going before Block 1 as nothing is there
    def previous_block(self):
        if self.current_block_index > 0:
            self.current_block_index -= 1

        return self.get_current_block_questions()

    # checks whether all 23 questions have been answered
    def is_complete(self):
        return len(self.responses) == len(questions)

    # returns all stored questionnaire responses
    def get_responses(self):
        return self.responses