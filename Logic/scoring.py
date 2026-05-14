
# MenoLikelihood scoring logic

MAX_RAW_SCORE = 54
# Explained why in Word document


def calc_raw_score(responses):

    # Calculates the total raw symptom score
    # from scored questionnaire responses

    raw_score = 0

    for question_id, answer in responses.items():

        # Only score questions 5-22
        if 5 <= question_id <= 22:
            raw_score += answer

    return raw_score


def convert_to_percentage(raw_score):

    # Converts raw score to percentage out of 100

    meno_percentage = (raw_score / MAX_RAW_SCORE) * 100

    return round(meno_percentage)


def calc_meno_score(responses):

    # Converts raw score to percentage out of 100
    # for final MenoLikelihood score

    raw_score = calc_raw_score(responses)

    percentage_score = convert_to_percentage(raw_score)

    return {
    "raw_score": raw_score,
    "percentage_score": percentage_score
}