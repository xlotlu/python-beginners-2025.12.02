# compare ages:
# 1) cereți vârsta utilizatorului
# 2) cereți vârsta prietenului său
# 3) faceți print cu diferența de vârstă

my_age = int(input("vârsta ta? "))
friend_age = int(input("vârsta prietenului? "))

diff = my_age - friend_age

# vreau să concatenez acest string cu un număr întreg
print("Diferența de vârstă este: " + str(diff))

# sau, nu e nevoie de concatenare
print("Diferența de vârstă este:", diff)

# sau folosim f-string
print(f"Diferența de vârstă este: {diff}")

