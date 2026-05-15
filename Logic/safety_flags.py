#safety flag for if patient has existing health conditions

# Checks whether Question 23 triggered a complex case flag


def is_complex_case(answer):

    if answer == "Yes":
        return True

    return False