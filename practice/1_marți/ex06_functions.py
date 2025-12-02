# functions

# am învățat
# input, print, int, str, abs

# scopul fundamental al unei funcții:
#   să primească input
#   să facă calcule (ea știe ce) pe baza acestui input
#   să returneze rezultatul


def func():
    print("aici execut ceva")
    print("și altceva")

def add(x, y):
    return x + y

result = add(3, 7)

# Exercițiu:
# scrieți o funcție
def repeat(txt, num):
    # (un statement care nu face nimic dar este valid sintactic)
    pass

# ce returnează string-ul `txt` repetat de `num` ori


def repeat(txt , num):
    return txt * num

result = repeat("tralala", 3)
print(result)


# Exercițiu:
# scrieți o funcție
def ft_to_m(ft):
    pass
# care primește parametrul `ft` = număr de picioare
# și retunează valoarea în metri.
#
# ținem cont că 1ft = 0.3048m

def ft_to_m(ft):
    return ft * 0.3048

# Exercițiu:
# cereți utilizatorului cu input un număr de picioare,
# apoi faceți print nr.-ului de m corespunzător

# 1. cer date de la utilizator
num = input("picioare? ") # acum este str
# 2. conversie
num = float(num)
# 3. calcul
result = ft_to_m(num)
# x. printez rezultatul
print(f"{num:.04f} picioare înseamă {result:.04f} metri")

