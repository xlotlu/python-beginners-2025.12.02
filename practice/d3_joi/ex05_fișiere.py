# fișiere...

fname = "data/it-was.txt"

fp = open(fname, encoding="utf-8")

print(fp.read()) # citește tot, deseori nu vrem asta!

fp.seek(0)

# iterăm linie cu linie:
for line in fp:
    print(line)


# Exercițiu, faceți print-ul de mai sus
# să facă output fără newline-uri în plus.

fp.seek(0)
for line in fp:
    print("»", line.removesuffix("\n"))
