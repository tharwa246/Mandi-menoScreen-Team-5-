import sqlite3

DATABASE_PATH = "DatabaseTemp/menoscreen.db"


def get_questions_from_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id, question_text, question_type, category, option_group
    FROM questions
    ORDER BY id
    """)

    question_rows = cursor.fetchall()

    questions = []

    for row in question_rows:
        question_id, question_text, question_type, category, option_group = row

        cursor.execute("""
        SELECT option_text, option_value
        FROM options
        WHERE question_id = ?
        """, (question_id,))

        option_rows = cursor.fetchall()

        options = []

        for option_text, option_value in option_rows:
            options.append({
                "text": option_text,
                "value": option_value
            })

        questions.append({
            "id": question_id,
            "text": question_text,
            "type": question_type,
            "category": category,
            "option_group": option_group,
            "options": options
        })

    connection.close()

    return questions