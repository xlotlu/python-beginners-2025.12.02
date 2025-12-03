#1. obțineți partea întreagă a împărțirii lui 17 la 4.

17 // 4

int(17 / 4)

#2. obțineți restul împărțirii lui 17 la 4.

17 % 4

#3. ridicați 8 la puterea a 3a.

8 ** 3

#4. (opțional) știind că modulul se numește `math` și funcția ce o căutăm se numește `sqrt`, obțineți rădăcina pătrată a lui 2.
import math
print(math.sqrt(2))

# sau
from math import sqrt
print(sqrt(2))

#5. setați variabilele
name = "Jane"
is_student = True

# și folosiți-le într-un condițional care să facă print
# pe un branch la un string de forma "<name> is a student."
# și pe celălalt branch "<name> is not a student."

if is_student:
    print(name + " is a student.")
else:
    print(name + " is not a student.")

# apoi repetați codul schimbând variabilele în
name = "Andrew"
is_student = False

if is_student:
    print(name + " is a student.")
else:
    print(name + " is not a student.")

#6. concatenați string-ul "bla bli blu" cu sine de 7 ori.
"bla bli blu" * 7

#7. scrieți o funcție `cube(x)` ce calculează x la puterea a 3a.
def cube(x):
    return x ** 3

#8. luați un număr întreg ca input de la utilizator,
# și folosind funcția `cube()` faceți print cu textul:
# "Cubul numărului <număr> este <cub>".
#
# Rezolvați problema
# a) concatenând string-uri
# b) folosind un f-string.

num = input("Spune un număr întreg: ")
num = int(num)

print("Cubul numărului " + str(num) + " este " + str(cube(num)))
print(f"Cubul numărului {num} este {cube(num)}")

#9. folosind funcția `get_greeting()` de ieri,
# ce returnează salutul potrivit pentru momentul curent al zilei:
#
# întrebați utilizatorul care este numele său și faceți output
# unui string de forma "<salutare>, <nume>!".

from practice.d1_marți.ex08_functions_with_date import get_greeting

greeting = get_greeting()
name = input("Care este numele tău? ")

print(f"{greeting}, {name}!")