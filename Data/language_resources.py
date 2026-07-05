from deep_translator import GoogleTranslator
import questions as q

LANGUAGE_MAP = {
    "English": "en",
    "Afrikaans": "af",
    "isiXhosa": "xh",
    "isiZulu": "zu",
    "Sesotho": "st",
    "Setswana": "tn",
    "Sepedi": "nso",
    "siSwati": "ss",
    "Tshivenda": "ve"
}

def translate_text(text, patient_code):
    if patient_code == "en":
        return text
    try:
        translated = GoogleTranslator(source="en", target=patient_code).translate(text)
        return translated
    except:
        return text


# this method translates into the patient language, it checks the language for the patient if 
# it does not have a code then makes english the default language
# and if the patient speaks english just return the questions as they are since they are alreafy in english
def get_translated_questions(patient_language):
    patient_code = LANGUAGE_MAP.get(patient_language, "en")
    
    if patient_code == "en":
        return q.questions

    new_translated_list = []

    for item in q.questions:
     
        translated_item = {
            "id": item["id"],
            
            # keep original english metadata for the backend which calculates menosore and clinician reports
            "type": item["type"],
            "category": item["category"],
            "english_text": item["text"],
            "english_options": item["options"],  # safely preserves the original english list or dict
            
            # now this is the metadata we are going to need in the patient language
            "translated_type": translate_text(item["type"], patient_code),
            "translated_category": translate_text(item["category"], patient_code)
        }
        
        # translate the main question text for the patient UI
        translated_item["text"] = translate_text(item["text"], patient_code)
        
        # create the translated clickable options for the patient UI
        raw_options = item["options"]
        
        if type(raw_options) == list:
            new_list = []
            for option in raw_options:
                new_list.append(translate_text(option, patient_code))
            translated_item["options"] = new_list
            
        elif type(raw_options) == dict:
            new_dict = {}
            for score in raw_options:
                text_label = raw_options[score]
                new_dict[score] = translate_text(text_label, patient_code)
            translated_item["options"] = new_dict

        #translate the safety warning if it exists (Q23)
        if "if_yes" in item:
            translated_item["if_yes"] = translate_text(item["if_yes"], patient_code)
            translated_item["english_if_yes"] = item["if_yes"] #keeps English backup

        new_translated_list.append(translated_item)

    return new_translated_list