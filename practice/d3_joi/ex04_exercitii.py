# Exercițiu:
# dată fiind structura de date
people = [
    ["Jane", 42, ["hiking", "jogging", "knitting"]],
    ["Mike", 17, ["hiking", "fishing", "reading"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# 1. creați un dicționar ce va conține cheia numele și valoare vârsta
# {"Jane": 42, "Mike": 17, ...}

# pattern de acumulare:
# 1) instanțiez
ages = {} # <-- rezultat
# 2) iterez
for person in people:
    # 3) am obținut datele necesare
    name = person[0]
    age = person[1]
    
    # 4) acumulez. "construiesc la obiect".
    ages[name] = age

# 5) suntem gata
print(ages)


# 2. creați o listă de dicționare, în care fiecare element al listei
#    este de forma {"name": ..., "age": ..., "hobbies": ...}
"""
ppl = [
    {"name": "Jane", "age": 42, "hobbies": [...]},
    {"name": "Mike", "age": 17, "hobbies": [...]},
    # ....
]
"""


#### Pattern de acumulare ####

# 1. inițializăm sursa
# 2. inițializăm obiectul rezultant
# 3. iterăm în sursă
    # 4. filtrăm
        # 5. ne facem calculul
        # 6. acumulăm
# 7. suntem gata

ppl = []
for name, age, hobbies in people:
    ppl.append({
        "name" : name,
        "age" : age,
        "hobbies" : hobbies,
    })

print(ppl)


# "list comprehension"
odd_squares = []
for elem in range(15):
    if elem % 2:
        odd_squares.append(elem ** 2)

odd_squares = [
    elem ** 2
    for elem in range(15)
    if elem % 2
]



ppl = []
for name, age, hobbies in people:
    ppl.append({
        "name" : name,
        "age" : age,
        "hobbies" : hobbies,
    })

ppl = [
    {
        "name" : name,
        "age" : age,
        "hobbies" : hobbies,
    }
    for name, age, hobbies in people
]


ppl = [{"name" : name, "age" : age, "hobbies" : hobbies} for name, age, hobbies in people]
