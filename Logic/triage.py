#Triage messages based on each menolikelihood scores

def determine_triage(percentagescore):

#message for a menolikelihood of 0-30%
    if 0<= percentagescore <=30:
     message = "Her symptom profile does not strongly suggest hormonal change at this time. Reassure her and invite her to return if symptoms persist or worsen"
     clinician_summary = "\n\nSummary\n\n Low MenoLikelihood score. \nNo significant symptom cluster identified at this time. \nRecommend: reassurance and routine follow-up."
    
#message for menolikelihood of 31-55%
    elif 31<= percentagescore<=55:
       message = "Her symptom profile is consistent with early perimenopause. Begin the menopause conversation. Consider lifestyle support or referral."
       clinician_summary = "\n\nSummary\n\nModerate MenoLikelihood score.\n Symptom cluster consistent with perimenopause. \nRecommend: menopause conversation, lifestyle support, consider referral."

    
#message for menolikelihood of 56-80
    elif 56<=percentagescore<=80:
       message = "Her symptom profile is strongly consistent with peri/menopause. Discuss HRT options or refer to a menopause-trained GP or gynaecologist"
       clinician_summary = "\n\nSummary\n\nHigh MenoLikelihood score. \nStrong symptom pattern consistent with perimenopause or menopause. \nRecommend: discussion of HRT options or referral to menopause-trained specialist."
   
#message for menolikelihood of 81-100
    else:
       message = "She is carrying a significant symptom burden. Urgent referral is recommended. Please use warm, validating language in your conversation and in her summary"
       clinician_summary = "\n\nSummary\n\nVery high MenoLikelihood score.\nSevere symptom burden. \nRecommend: Urgent referral to menopause-trained specialist. Patient requires compassionate, timely support."
       
    
    return message + clinician_summary 

