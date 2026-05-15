# Output templates for MenoScreen
# This file stores all triage messages and output content
# after questionnaire scoring is completed


TRIAGE_TEMPLATES = {

    "unlikely": {

        "band": "Unlikely",

        "score_range": "0-30",

        "colour": "green",

        "on_screen_message":
        "Her symptom profile does not strongly suggest hormonal "
        "change at this time. Reassure her and invite her to "
        "return if symptoms persist or worsen.",

        "clinician_summary_message":
        "Low MenoLikelihood score: {percentage_score}/100\n"
        "Triage Band: Unlikely (0-30)\n\n"
        "No significant symptom cluster identified at this time.\n\n"
        "Recommend: reassurance and routine follow-up.",

        "patient_handout_message":
        "Your results today do not show a strong hormonal pattern, "
        "but your body knows best.\n"
        "If you notice changes, come back.\n"
        "JoinMandi.com has information to help you understand "
        "what to watch for."
    },


    "possible": {

        "band": "Possible",

        "score_range": "31-55",

        "colour": "yellow",

        "on_screen_message":
        "Her symptom profile is consistent with early "
        "perimenopause. Begin the menopause conversation. "
        "Consider lifestyle support or referral.",

        "clinician_summary_message":
        "Moderate MenoLikelihood score: {percentage_score}/100\n"
        "Triage Band: Possible (31-55)\n\n"
        "Symptom cluster consistent with perimenopause.\n\n"
        "Recommend: menopause conversation, lifestyle support, "
        "consider referral.",

        "patient_handout_message":
        "What you are feeling has a name.\n"
        "Your results today suggest your hormones may be "
        "starting to change.\n"
        "This is perimenopause — and there is support available.\n"
        "JoinMandi.com will help you understand what is happening "
        "and what your options are."
    },


    "likely": {

        "band": "Likely",

        "score_range": "56-80",

        "colour": "orange",

        "on_screen_message":
        "Her symptom profile is strongly consistent with "
        "peri/menopause. Discuss HRT options or refer to "
        "a menopause-trained GP or gynaecologist.",

        "clinician_summary_message":
        "High MenoLikelihood score: {percentage_score}/100\n"
        "Triage Band: Likely (56-80)\n\n"
        "Strong symptom pattern consistent with perimenopause "
        "or menopause.\n\n"
        "Recommend: discussion of HRT options or referral "
        "to menopause-trained specialist.",

        "patient_handout_message":
        "Your symptoms are real and they have a cause.\n"
        "Your results today suggest you are likely in "
        "perimenopause or menopause.\n"
        "You have options, and you deserve to know about them.\n"
        "JoinMandi.com will walk you through what is happening "
        "and how to find the right support."
    },


    "significant": {

        "band": "Significant",

        "score_range": "81-100",

        "colour": "red",

        "on_screen_message":
        "She is carrying a significant symptom burden.\n"
        "Urgent referral is recommended.\n"
        "Please use warm, validating language in your "
        "conversation and in her summary.",

        "clinician_summary_message":
        "Very high MenoLikelihood score: {percentage_score}/100\n"
        "Triage Band: Significant (81-100)\n\n"
        "Severe symptom burden.\n"
        "Urgent referral to menopause-trained specialist "
        "recommended.\n"
        "Patient requires compassionate, timely support.",

        "patient_handout_message":
        "You have been carrying a lot.\n"
        "Your results today show that your symptoms are "
        "significant — and you deserve urgent, proper support.\n"
        "Please do not wait.\n"
        "JoinMandi.com can help you find the right doctor now."
    },


    "complex": {

        "band": "Complex",

        "score_range": "Any Score",

        "colour": "purple",

        "on_screen_message":
        "This patient has existing health conditions that "
        "require specialist input before any treatment is "
        "considered.\n"
        "Please refer before discussing HRT.",

        "clinician_summary_message":
        "MenoLikelihood score: {percentage_score}/100\n"
        "Triage Band: Complex\n\n"
        "Complex case flag raised.\n"
        "Existing health conditions noted.\n"
        "Specialist referral required before any treatment "
        "decision.\n"
        "Do not recommend HRT without specialist input.",

        "patient_handout_message":
        "Your results today suggest your symptoms may be "
        "related to your hormones — but because of your "
        "health history, your doctor wants to make sure "
        "you get the right specialist support.\n"
        "JoinMandi.com has information to help you prepare "
        "for that conversation."
    }
}


# Returns all information for a specific triage band
# Example: get_template("unlikely")
def get_template(band):

    return TRIAGE_TEMPLATES.get(band)


# Determines which triage band the patient falls into
# based on their MenoLikelihood score
def get_band_from_score(percentage_score, complex_case=False):

    if complex_case:

        return "complex"

    elif percentage_score <= 30:

        return "unlikely"

    elif percentage_score <= 55:

        return "possible"

    elif percentage_score <= 80:

        return "likely"

    else:

        return "significant"


# Formats the clinician summary message using the score
def format_clinician_summary_message(percentage_score, band):

    template = get_template(band)

    if template:

        return template["clinician_summary_message"].format(
            percentage_score=percentage_score
        )

    return "Error: Band not found in templates."