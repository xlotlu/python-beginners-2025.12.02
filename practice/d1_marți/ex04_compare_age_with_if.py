# compare ages:
# 1) cereți vârsta utilizatorului
# 2) cereți vârsta prietenului său
# 3) faceți print cu unul din stringurile:

"Ești mai mare cu «x» ani decât prietenul tău"
"Prietenul tău este mai mare cu «x» ani decât tine"
"Aveți aceeași vârstă"

# faceți asta folosind if / elif / else

my_age = int(input("vârsta ta? "))
friend_age = int(input("vârsta prietenului? "))

diff = abs(my_age - friend_age)

if my_age > friend_age:
    print(f"Ești mai mare cu {diff} ani decât prietenul tău")

elif my_age < friend_age:
    #diff = diff * -1
    print(f"Prietenul tău este mai mare cu {diff} ani decât tine")

else: # elif my_age == friend_age:
    print("Aveți aceeași vârstă")
