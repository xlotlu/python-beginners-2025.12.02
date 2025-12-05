# Exercițiu:
#
# scrieți o funcție
def count_occurences(fname, word):
    pass
# ce, primind o cale către un fișier și un cuvânt,
# returnează numărul de apariții al acelui cuvânt
# în fișier

def count_occurences(fname, word):
    fp = open(fname, encoding="utf-8")
    content = fp.read()

    for chr in '.,!?#$%^&*()[]{}':
        content = content.replace(chr, " ")

    words = content.split()

    return words.count(word)

# implementare alternativă
def count_occurences(fname, word):
    fp = open(fname, encoding="utf-8")
    
    total = 0
    for line in fp:
        for chr in '.,!?#$%^&*()[]{}':
            line = line.replace(chr, " ")

        words = line.split()
        count = words.count(word)

        total += count

    return total


print(count_occurences("data/it-was.txt", "was"))

# modificați funcția de mai sus
# astfel încât să funcționeze și în modul
# case-insensitive:
def count_occurences(fname, word, insensitive=False):
    fp = open(fname, encoding="utf-8")

    if insensitive:
        word = word.casefold()
    
    total = 0
    for line in fp:
        if insensitive:
            line = line.casefold()

        for chr in '.,!?#$%^&*()[]{}':
            line = line.replace(chr, " ")

        words = line.split()
        count = words.count(word)

        total += count

    return total

print(count_occurences("data/it-was.txt", "was"))

