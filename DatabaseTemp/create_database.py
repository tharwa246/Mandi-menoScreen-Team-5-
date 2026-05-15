import sqlite3

DATABASE_PATH = "DatabaseTemp/menoscreen.db"


option_groups = {
    "severity": [
        ("Not at all", 0),
        ("A little", 1),
        ("Quite a bit", 2),
        ("Extremely", 3)
    ],
    "age": [
        ("35-44", None),
        ("45-54", None),
        ("55-64", None),
        ("65+", None)
    ],
    "period": [
        ("Still regular", None),
        ("Becoming irregular", None),
        ("Stopped less than 2 years ago", None),
        ("Stopped more than 2 years ago", None),
        ("Hysterectomy", None),
        ("Not sure", None)
    ],
    "yes_no_unsure": [
        ("Yes", None),
        ("No", None),
        ("Not sure", None)
    ],
    "yes_no": [
        ("Yes", None),
        ("No", None)
    ]
}


questions = [
    (1, "How old are you?", "context", "Patient Context", "age"),
    (2, "When did your periods last change or stop?", "context", "Patient Context", "period"),
    (3, "Has a doctor ever spoken to you about menopause or your hormones?", "context", "Patient Context", "yes_no_unsure"),
    (4, "Are you currently taking any regular medication?", "context", "Patient Context", "yes_no_unsure"),

    (5, "Have you been struggling to concentrate, or feeling like your thinking is foggy?", "scored", "Cognitive and Mood", "severity"),
    (6, "Have you been forgetting names, words, or where you put things more than usual?", "scored", "Cognitive and Mood", "severity"),
    (7, "Have you been feeling anxious, low, or tearful for no clear reason?", "scored", "Cognitive and Mood", "severity"),
    (8, "Have you been feeling more irritable than usual, or finding your moods are harder to manage?", "scored", "Cognitive and Mood", "severity"),

    (9, "Have you been experiencing sudden waves of heat through your body?", "scored", "Vasomotor and Sleep", "severity"),
    (10, "Have you been waking up drenched in sweat or feeling overheated at night?", "scored", "Vasomotor and Sleep", "severity"),
    (11, "Have you been struggling to fall asleep, or waking up during the night?", "scored", "Vasomotor and Sleep", "severity"),
    (12, "Have you noticed your heart racing or beating irregularly?", "scored", "Vasomotor and Sleep", "severity"),

    (13, "Have you been experiencing joint pain or stiffness, especially in the mornings?", "scored", "Musculoskeletal and Energy", "severity"),
    (14, "Do you feel exhausted even after a full night's sleep?", "scored", "Musculoskeletal and Energy", "severity"),
    (15, "Have you been getting new headaches, or are your existing headaches becoming more frequent or severe?", "scored", "Musculoskeletal and Energy", "severity"),

    (16, "Have you been experiencing any vaginal soreness, irritation, or discomfort — including during sex?", "scored", "Urogenital and Sexual Health", "severity"),
    (17, "Have you been needing to rush to the bathroom urgently, or experiencing any leaking?", "scored", "Urogenital and Sexual Health", "severity"),
    (18, "Have you been getting urinary tract infections repeatedly?", "scored", "Urogenital and Sexual Health", "severity"),
    (19, "Has your interest in sex reduced or disappeared?", "scored", "Urogenital and Sexual Health", "severity"),

    (20, "Have these symptoms been affecting your ability to work — your concentration, productivity, or confidence?", "scored", "Quality of Life Impact", "severity"),
    (21, "Have these symptoms been affecting your relationships — with your partner, family, or friends?", "scored", "Quality of Life Impact", "severity"),
    (22, "Overall, how much are these symptoms getting in the way of your daily life?", "scored", "Quality of Life Impact", "severity"),

    (23, "Do you have any health conditions — such as diabetes, heart disease, a history of cancer, or an autoimmune condition — that we should consider before discussing treatment?", "safety_flag", "Safety Flag", "yes_no")
]


def create_tables(cursor):
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DROP TABLE IF EXISTS options")
    cursor.execute("DROP TABLE IF EXISTS questions")

    cursor.execute("""
    CREATE TABLE questions (
        id INTEGER PRIMARY KEY,
        question_text TEXT NOT NULL,
        question_type TEXT NOT NULL,
        category TEXT NOT NULL,
        option_group TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE options (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER NOT NULL,
        option_text TEXT NOT NULL,
        option_value INTEGER,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    """)


def insert_questions(cursor):
    for question_id, question_text, question_type, category, option_group in questions:
        cursor.execute("""
        INSERT INTO questions (id, question_text, question_type, category, option_group)
        VALUES (?, ?, ?, ?, ?)
        """, (question_id, question_text, question_type, category, option_group))

        insert_options(cursor, question_id, option_group)


def insert_options(cursor, question_id, option_group):
    for option_text, option_value in option_groups[option_group]:
        cursor.execute("""
        INSERT INTO options (question_id, option_text, option_value)
        VALUES (?, ?, ?)
        """, (question_id, option_text, option_value))


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    create_tables(cursor)
    insert_questions(cursor)

    connection.commit()
    connection.close()

    print("Database created and fully populated successfully!")


create_database()