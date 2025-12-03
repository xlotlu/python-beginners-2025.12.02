# Exercițiu:
# dată fiind următoarea tuplă:
t = (11, 12, 7, 2, 6, 4, 18)

# iterați prin ea și printați toate elementele care 
# au valoare mai mare decât 10


# Exercițiu:
# dată fiind tupla de tuple de forma (titlu, scor):

movies = (
    ("Titanic", 7.9),
    ("Star Wars", 8.6),
    ("The Lord of the Rings", 9),
    ("Harry Potter", 7.6),
    ("Transformers", 7),
)

# printați titlul filmelor recomandate.
# un film recomandat este unul care are
# scorul mai mare decât 8.

for movie in movies:
    title = movie[0]
    score = movie[1]

    if score > 8:
        print(title)

# concepte:
for title, score in movies: # unpacking
    print(f'{score:.02f} :: {title}')
    # f-string cu formatare de float


# Exercițiu
# dată fiind structura de date
people = [
    ("Jane", 42, ["hiking", "jogging", "knitting"]),
    ("Mike", 17, ["hiking", "fishing", "reading"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
]

# iterați prin ea
# și printați numele prietenilor care au hobby "hiking"

for name, age, hobbies in people:
    if "hiking" in hobbies:
        print(name)


# Exercițiu:
# construiți o listă cu pătratele
# numerelor impare de la 10 la 15.


#### Pattern de acumulare ####

# 1. inițializăm sursa
source = range(10, 16)

# 2. inițializăm obiectul rezultant
squares = []

# 3. iterăm în sursă
for item in source:
    # 4. filtrăm
    if item % 2:
        # 5. ne facem calculul
        value = item * item

        # 6. acumulăm
        squares.append(value)

# 7. suntem gata (inspectăm rezultatul)
print(squares)


# Exercițiu
# dată fiind structura de date `people` de mai sus,
# scrieți o funcție
def filter_by_hobby(lst, hobby):
    pass
# ce primește ca prim parametru `lst`
# o listă de tuple de forma
# (name, age, hobbies)
# 
# și returnează o listă nouă cu tuplele
# care au printre hobbies `hobby`.


def filter_by_hobby(lst, hobby):
    # 1. sursa este `lst`
    # 2. inițializăm obiectul rezultant
    out = []

    # 3. iterăm în sursă
    for person in lst:
        hobbies = person[2]
        # 4. filtrăm
        if hobby in hobbies:
            # 5. (nu e nimic de calculat)
            # 6. acumulăm
            out.append(person)

    # 7. suntem gata, deci returnăm
    return out

# Exercițiu:
# obțineți prietenii care fac "hiking"
# folosind funcția filter:

def is_hiker(elem):
    return "hiking" in elem[2]

for friend in filter(is_hiker, people):
    print(friend)
