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