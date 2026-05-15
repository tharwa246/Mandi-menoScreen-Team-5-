# output templates for MenoScreen 
# this is the file that stores all the messegaes once screening is done
#it connects to scoring.py and uses the percentage score to determine which message to display

#the band is detemined by the get_band function in scoring.py
#ohh and the complex comes from question 23 in the brief 

TRIAGE_TEMPLATES={
    "unlikely":{
        "band":"Unlikely",
        "score_range":"0-30",
        "colour":"green",
        "on_screen_message":"Her symptom profile does not strongly suggest hormonal change at this time. Reassure her and invite her to return if symptoms persist or worsen.",
        "clinician_summary_message":"Low Menolikelihood score: {percentage_score}/100\n Triage Band: Unlikely (0-30)\n\nNo signifcant symptom cluster identified at this time.\n\n Recommend: reassurance and routine follow-up",
        "patient_handout_message":"Your results today don't show a strong hormonal pattern but your body knows best.\n If you notice changes, come back.\n JoinMandi.com has information to help you understand what to watch for.", 
    },

    "possible":{
        "band":"Possible",
        "score_range":"31-55",
        "colour":"yellow",
        "on_screen_message":"Her symptom profile is consistent with early perimenopause. Begin the menopause conversation. Consider lifestyle support or referral",
        "clinician_summary_message":"Moderate MenoLikelihood score: {percentage_score}/100\n Triage Band: Possible (31-55)\n\nSymptom cluster consistent with perimenopause.\n\nRecommend: menopause conversation, lifestyle support, consider referral",
        "patient_handout_message":"What you are feeling has a name. Your results today suggest your hormones may be starting to change. This is perimenopause — and there is support available. JoinMandi.com will help you understand what is happening and what your options are", 
    },

    "likely":{
        "band":"Likely",
        "score_range":"56-80",
        "colour":"red",
        "on_screen_message":"Her symptom profile is strongly consistent with peri/menopause. Discuss HRT options or refer to a menopause-trained GP or gynaecologist",
        "clinician_summary_message":"High MenoLikelihood score: {percentage_score}/100\n Triage Band: Likely (56-80)\n\nStrong symptom pattern consistent with perimenopause or menopause.\n\nRecommend:discussion of HRT options or referral to menopause-trained specialist",
        "patient_handout_message":"Your symptoms are real and they have a cause. \nYour results today suggest you are likely in perimenopause or menopause.\n You have options, and you deserve to know about them. JoinMandi.com will walk you through what is happening and how to find the right support", 
    },

    "significant":{
        "band":"Significant",
        "score_range":"81-100",
        "colour":"red",
        "on_screen_message":"She is carrying a significant symptom burden. Urgent referral is recommended. Please use warm, validating language in your conversation and in her summary",
        "clinician_summary_message":"Very high MenoLikelihood score: {percentage_score}/100\n Triage Band: Significant (81-100)\n\nSevere symptom burden. Urgent referral to menopause-trained specialist recommended.\n Patient requires compassionate, timely support.",
        "patient_handout_message":"You have been carrying a lot.\n Your results today show that your symptoms are significant — and you deserve urgent, proper support. \nPlease do not wait. JoinMandi.com can help you find the right doctor now", 
    },

    "complex":{
        "band":"Complex",   
        "score_range":"any score",
        "on_screen_message":"This patient has existing health conditions that require specialist input before any treatment is considered.\n Please refer before discussing HRT.",
        "clinician_summary_message":"Menolikelihood score: {percentage_score}/100\n Triage Band: Complex\n\n Complex case flag raised. Existing health conditions noted. Specialist referral required before any treatment decision. Do not recommend HRT without specialist input",
        "patient_handout_message":"Your results today suggest your symptoms may be related to your hormones — but because of your health history, your doctor wants to make sure you get the right specialist support. JoinMandi.com has information to help you prepare for that conversation",
    },
}
  #the funtion used her is takes a specific band and returns the info in that band 
  #e.g you call band "unlikely" it will retun everything in that band
  
def get_template(band):
    return TRIAGE_TEMPLATES.get(band)

#this function takes the score from scoring.py and retuns the band the patient falls into 
#the complex is set false by default unless the patient answers yes then it returns complex if not the normal scoring is used 

def get_band_from_score (percentage_score, complex=False):
    if complex:
        return "complex"
    elif percentage_score <= 30:
        return "unlikely"
    elif percentage_score <= 55:
        return "possible"
    elif percentage_score <= 80:
        return "likely"
    else:
        return "significant"

    #function calls the band name and score 
    #get_template calls the band name and everything in it, stores it in variable template

    def format_clinician_summary_message(percentage_score, band):
        template = get_template(band)
        if template:
            return template["clinician_summary_message"].format(percentage_score=percentage_score)
        else:
            return "Error: Band not found in templates."
