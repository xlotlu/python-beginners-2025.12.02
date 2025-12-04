# dictionarul

# "item access":
#      ---> list, tuple, str :: index
#      ---> dict             :: key 


# Exercițiu:
# dat fiind
person = {
   "name"    : "Jane",
   "age"     : 42,
   "city"    : "Bucharest",
   "hobbies" : [],
}

# a) Jane s-a mutat în Cluj
person["city"] = "Cluj"

# b) Jane a îmbătrânit un an
person["age"] += 1

# c) am obținut nr.-ul de telefon al lui Jane: "09211".
#    adăugați-l la dicționar cu cheia "phone"
person["phone"] = "09211"

# d) adăugați-i hobby-ul "reading"
person["hobbies"].append("reading")

# print(person)


# Exercițiu:
#
# a) luați valoarea pentru cheia "address",
#    și dacă nu există returnați string-ul "---"
print(person.get("address", "---"))

# b) ștergeți cheia "city" în timp ce îi returnați
#    valoarea aferentă
print(person.pop("city"))

# c) modificați dicționarul, într-o singură operațiune,
#    astfel încât să apară / să se modifice cheile:
#    age : 43
#    city: Cluj
#    address: Str. Câmpiei 55

person.update(
    {
        "age": 43,
        "city": "Cluj",
        "address": "Str. Câmpiei 55"
    }
)
print(person)


# 2 pattern-uri:

# A. "database row", field-oriented
# (un singur rând dintr-un tabel, unde cunoaștem și numele coloanelor)
{
    "name": "...",
    "age": 52,
    "phone": "...",
}


collection = [
    {"name": "Jane", "age": 42},
    {"name": "Sam", "age": 52},
    {"name": "Pam", "age": 32},
]


# B. "collection", id-value oriented
# ("un tabel întreg cu 2 coloane")
ages = {
    "Jane": 42,
    "Sam": 52,
    "Pam": 32,
}

collection = {
    "Jane": (42, "Cluj"),
    "Sam": (52, "București"),
    "Pam": (32, "Iași"),
}

d = {}
# ! cea mai deasă modalitate de a itera un dicționar:
for k, v in d.items():
    pass

