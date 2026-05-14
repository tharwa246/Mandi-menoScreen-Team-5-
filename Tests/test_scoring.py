import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logic.scoring import calc_meno_score


responses = {

    # Context Questions
    1: "45-54",
    2: "Irregular",
    3: "Yes",
    4: "No",

    # Scored Questions (Q5-Q22)
    5: 2,
    6: 1,
    7: 3,
    8: 2,
    9: 1,
    10: 2,
    11: 2,
    12: 1,
    13: 3,
    14: 2,
    15: 1,
    16: 0,
    17: 1,
    18: 0,
    19: 1,
    20: 2,
    21: 1,
    22: 2,

    # Safety Flag
    23: "No"
}


result = calc_meno_score(responses)

print("Raw Score:", result["raw_score"])
print("Percentage Score:", result["percentage_score"])