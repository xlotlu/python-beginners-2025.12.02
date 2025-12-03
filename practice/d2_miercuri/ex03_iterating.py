iterable = [1, 2, 3, 5, 12] # this is a list

# for <...> in <...>
for element in iterable:
    print("doing something with", element)

s = 'acesta este un string'
# str-ul este iterabil după caractere
for elem in s:
    print("»", elem)

tup = ("ala", "bala", "portocala")

for elem in tup:
    print("»", elem)


#### str, tuple, list sunt "sequences". ####

s = "acesta este un string"
tup = ("ala", "bala", "portocala")
lst = ["zero", "unu", "doi", "trei"]

# 1. sunt iterabile
for elem in lst:
    print(elem)

# 2. au lungime
len(s), len(lst), len(tup)

#3. au metodele .count() .index()

#4. suportă acces după index


# str și tuple sunt read-only. "immutable"
# list is mutable

lst = ["zero", "unu", "doi", "trei"]
# list supports "item assignment"
lst[2] = "patru"

# pattern LIFO:
lst.append("something")
lst.pop()

# pattern FIFO (first-in, first-out):
lst.insert(0, "something")
lst.pop()

# pattern FIFO alternativ
lst.append("something else")
lst.pop(0)


# !! !! !!
lst.append(elem) # adaugă UN element la coada listei
lst.insert(iterable) # adaugă TOATE elementele din `iterable` la coada listei


## sortarea listei
# Exercițiu. dată fiind lista
lst = ['Iași', 'Cluj', 'București', 'Brașov', 'Arad', "Bod", "Călărași", "Aiud"]

# sortați-o după lungimea caracterelor fiecărui element

def sortbylen(elem):
    return len(elem)

lst.sort(key=sortbylen)

# sortați-o după lungimea caracterelor fiecărui element
#           și alfabetic
def sortbylen_and_alpha(elem):
    return (len(elem), elem)


# Exercițiu:
# știind cum să găsiți indexul unui element într-o listă,
# știind că puteți face del listă[index],
# scrieți o funcție
def remove(lst, value):
    pass
# care replică funcționalitatea metodei `lst.remove()`


def remove(lst, value):
    "caută `value` în `lst` și îl șterge dacă există"
    try:
        idx = lst.index(value)
        del lst[idx]
    except ValueError:
        pass
