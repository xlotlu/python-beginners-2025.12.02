# Exerciții
#
# 1. Scrieți o funcție
def get_person(collection, name):
    pass

# ce primind ca argumente o colecție de liste de forma
people = [
    ["Jane", 42, ["hiking", "jogging", "knitting"]],
    ["Mike", 17, ["hiking", "fishing", "reading"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# și un string,
# returnează listă respectivă a acelei persoane.
#
# asigurați-vă că returnați o referință la obiectul listă din colecție,
# și nu o listă nouă.

def get_person(collection, name):
    for person in collection:
        if name == person[0]:
            return person


# 2. Folosind funcția `get_person()` de mai sus,
# modificați următoarele valori:

# a) faceți ca Jane să fi îmbătrânit un an
j = get_person(people, "Jane")
j[1] += 1

# b) ștergeți-i ultimul hobby lui Sam
get_person(people, "Sam")[2].pop()
# sau
#del get_person(people, "Sam")[2][-1]

# c) adăugați-i lui Dan "jogging" la hobbies
def get_hobbies_for_person(obj):
    return obj[2]

def hbb(collection, name):
    return get_hobbies_for_person(get_person(collection, name))

hbb(people, "Dan").append("jogging")

# d) ștergeți-i lui Mike "fishing"
hbb(people, "Mike").remove("fishing")

# e) adăugați-i lui Anna toate elementele din ("reading", "cooking", "running")
#hbb(people, "Anna").append("reading")
#hbb(people, "Anna").append("cooking")
#hbb(people, "Anna").append("running")

hbb(people, "Anna").extend(
    ("reading", "cooking", "running")
)

# verificați ce s-a întâmplat cu valorile din `people`.




# Exercițiu
# dată fiind lista

cities = [
    "București", "Arad", "Cluj", "Timișoara",
]

# 1) adăugați "Constanța" la final
cities.append("Constanța")

# 2) inserați "Galați" înainte de "Arad"
arad_idx = cities.index("Arad")
cities.insert(arad_idx, "Galați")

# 3) ștergeți elementul de la indexul 2 și faceți-i print
print(cities.pop(2))

# 4) adăugați la listă toate elementele din: ["Berlin", "Lisabona", "Londra"]
cities.extend(["Berlin", "Lisabona", "Londra"])

# 5) găsiți indexul elementului "Cluj"
cluj_idx = cities.index("Cluj")

# 6) modificați elementul "Cluj" astfel încât să fie "Cluj-Napoca"
cities[cluj_idx] = "Cluj-Napoca"

# 7) faceți print celui de-al 3lea element din listă
print(cities[2])

# 8) faceți print penultimului element din listă
print(cities[-2])

