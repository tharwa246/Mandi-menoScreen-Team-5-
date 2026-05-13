# MenoScreen 23-question clinical screening framework
# Q1-Q4 = context questions (NOT scored)
# Q5-Q22 = scored symptom questions, 0-3 scale
# Q23 = safety flag, triggers Complex pathway (NOT scored)

SEVERITY_OPTIONS = {
    0: "Not at all",
    1: "A little",
    2: "Quite a bit",
    3: "Extremely"
}

questions = [
    # Block 1:Patient Context
    {
        "id": 1,
        "text": "How old are you?",
        "type": "context",
        "category": "Patient Context",
        "options": ["35-44", "45-54", "55-64", "65+"]
    },
    {
        "id": 2,
        "text": "When did your periods last change or stop?",
        "type": "context",
        "category": "Patient Context",
        "options": [
            "Still regular",
            "Becoming irregular",
            "Stopped less than 2 years ago",
            "Stopped more than 2 years ago",
            "Hysterectomy",
            "Not sure"
        ]
    },
    {
        "id": 3,
        "text": "Has a doctor ever spoken to you about menopause or your hormones?",
        "type": "context",
        "category": "Patient Context",
        "options": ["Yes", "No", "Not sure"]
    },
    {
        "id": 4,
        "text": "Are you currently taking any regular medication?",
        "type": "context",
        "category": "Patient Context",
        "options": ["Yes - specify", "No", "Not sure"]
    },

    # Block 2:Cognitive & Mood
    {
        "id": 5,
        "text": "Have you been struggling to concentrate, or feeling like your thinking is foggy?",
        "type": "scored",
        "category": "Cognitive and Mood",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 6,
        "text": "Have you been forgetting names, words, or where you put things more than usual?",
        "type": "scored",
        "category": "Cognitive and Mood",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 7,
        "text": "Have you been feeling anxious, low, or tearful for no clear reason?",
        "type": "scored",
        "category": "Cognitive and Mood",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 8,
        "text": "Have you been feeling more irritable than usual, or finding your moods are harder to manage?",
        "type": "scored",
        "category": "Cognitive and Mood",
        "options": SEVERITY_OPTIONS
    },

    # Block 3:Vasomotor & Sleep
    {
        "id": 9,
        "text": "Have you been experiencing sudden waves of heat through your body?",
        "type": "scored",
        "category": "Vasomotor and Sleep",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 10,
        "text": "Have you been waking up drenched in sweat or feeling overheated at night?",
        "type": "scored",
        "category": "Vasomotor and Sleep",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 11,
        "text": "Have you been struggling to fall asleep, or waking up during the night?",
        "type": "scored",
        "category": "Vasomotor and Sleep",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 12,
        "text": "Have you noticed your heart racing or beating irregularly?",
        "type": "scored",
        "category": "Vasomotor and Sleep",
        "options": SEVERITY_OPTIONS
    },

    # Block 4:Musculoskeletal & Energy
    {
        "id": 13,
        "text": "Have you been experiencing joint pain or stiffness, especially in the mornings?",
        "type": "scored",
        "category": "Musculoskeletal and Energy",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 14,
        "text": "Do you feel exhausted even after a full night's sleep?",
        "type": "scored",
        "category": "Musculoskeletal and Energy",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 15,
        "text": "Have you been getting new headaches, or are your existing headaches becoming more frequent or severe?",
        "type": "scored",
        "category": "Musculoskeletal and Energy",
        "options": SEVERITY_OPTIONS
    },

    # Block 5:Urogenital & Sexual Health
    {
        "id": 16,
        "text": "Have you been experiencing any vaginal soreness, irritation, or discomfort — including during sex?",
        "type": "scored",
        "category": "Urogenital and Sexual Health",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 17,
        "text": "Have you been needing to rush to the bathroom urgently, or experiencing any leaking?",
        "type": "scored",
        "category": "Urogenital and Sexual Health",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 18,
        "text": "Have you been getting urinary tract infections repeatedly?",
        "type": "scored",
        "category": "Urogenital and Sexual Health",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 19,
        "text": "Has your interest in sex reduced or disappeared?",
        "type": "scored",
        "category": "Urogenital and Sexual Health",
        "options": SEVERITY_OPTIONS
    },

    # Block 6:Quality of Life Impact
    {
        "id": 20,
        "text": "Have these symptoms been affecting your ability to work — your concentration, productivity, or confidence?",
        "type": "scored",
        "category": "Quality of Life Impact",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 21,
        "text": "Have these symptoms been affecting your relationships — with your partner, family, or friends?",
        "type": "scored",
        "category": "Quality of Life Impact",
        "options": SEVERITY_OPTIONS
    },
    {
        "id": 22,
        "text": "Overall, how much are these symptoms getting in the way of your daily life?",
        "type": "scored",
        "category": "Quality of Life Impact",
        "options": SEVERITY_OPTIONS
    },

    # Block 7:Safety Flag
    {
        "id": 23,
        "text": "Do you have any health conditions — such as diabetes, heart disease, a history of cancer, or an autoimmune condition — that we should consider before discussing treatment?",
        "type": "safety_flag",
        "category": "Safety Flag",
        "options": ["Yes", "No"],
        "if_yes": "Complex case. Specialist referral required before treatment. Do not recommend HRT without specialist input."
    }

]

