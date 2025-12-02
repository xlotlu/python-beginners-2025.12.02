# age discrimination...
# 0) ne setăm variabilele
MIN_AGE = 18
MAX_AGE = 65
# 1) cerem vârsta utilizatorului
# 2) comparăm cu MIN_AGE și MAX_AGE,
#    2.1) dacă este mai mic decât MIN_AGE, mesaj:
"ești prea tânăr"
#    2.2) dacă este mai mare decât MAX_AGE, mesaj:
"ești prea în vârstă"
#    2.3) altfel:
"ești de vârstă potrivită"


MIN_AGE = 18
MAX_AGE = 65

user_age = int(input("Care este vârsta ta? "))

if user_age < MIN_AGE:
    print (f"ești prea tânăr")

elif user_age > MAX_AGE:
    print ("ești prea în vârstă")

else:
    print ("ești de vârstă potrivită")
