# Exercițiu:
# scrieți o funcție
def get_greeting(tod):
    pass

# care în funcție de "time of day", returnează
# salutul potrivit, astfel:
#
# "morning": "Bună dimineața"
# "noon":    "Bună ziua"
# "evening": "Bună seara"
# "night":   "Noapte bună"

def get_greeting(tod):
    if tod == "morning":
        greetings = "Bună dimineața"
    elif tod == "noon":
        greetings = "Bună ziua"
    elif tod == "evening":
        greetings = "Bună seara"
    elif tod == "night":
        greetings = "Noapte bună"
    else:
        raise ValueError(f"Invalid time of day: {tod}")

    return greetings


data = input("Tell me the time of day: ")

try:
    result = get_greeting(data) # buf!
    print(result)
except ValueError:
    # ValueError din funcția get_greeting() înseamnă că
    # time of day a fost invalid.
    print("Time of day is invalid!")

print("a continuat execuția")