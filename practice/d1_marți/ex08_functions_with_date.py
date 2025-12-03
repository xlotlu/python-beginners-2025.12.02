# Exercițiu:
# scrieți o funcție
def get_greeting():
    pass
# ce returnează salutul potrivit, astfel:
#
# între 5 și 11 dimineața:      "Bună dimineața"
# între 11 și 6 seara:          "Bună ziua"
# între 6 și 9 seara:           "Bună seara"
# între 9 seara și 5 dimineața: "Noapte bună"

# pentru a obține ora curentă:
from datetime import datetime

now = datetime.now()
hour = now.hour


def get_greeting():
    now = datetime.now()
    hour = now.hour

    print(hour)

    if 5 <= hour < 11:
        # hour >= 5 and hour < 11
        return "Bună dimineața"
    elif 11 <= hour < 16:
        # hour >= 11 and hour < 18
        return "Bună ziua"
    elif 16 <= hour < 21:
        # hour >= 18 and hour < 21
        return "Bună seara"
    else:
        return "Noapte bună"

result = get_greeting()
print(result)
    
