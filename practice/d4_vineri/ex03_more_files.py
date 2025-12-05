# more files...

# folosim context manager
with open("data/it-was.txt", encoding="utf-8") as fp:
    # aici îmi fac treaba....
    1 / 0


# Exercițiu:

# scrieți într-un fișier "test.txt"
# string-ul "Salutare, salut, salut"


# Exercițiu:
# scrieți o funcție
def cp(source, target):
    pass
# care primind două căi către fișiere,
# copiază conținutul lui `source` în `target`

def cp(source, target):
    with open(source, "r", encoding="utf-8") as fsursa:
        content = fsursa.read()

    with open(target, "w", encoding="utf-8") as ftarget:
        ftarget.write(content)

# alternativ: deschidem simultan cm-urile
def cp(source, target):
    # with poate să introducă mai multe context managere:
    with (
        open(source, "r", encoding="utf-8") as fsursa,
        open(target, "w", encoding="utf-8") as ftarget
    ):
        ftarget.write(
            fsursa.read()
        )

# alternativ 2: mai eficient cu memoria
def cp(source, target):
    # with poate să introducă mai multe context managere:
    with (
        open(source, "r", encoding="utf-8") as fsursa,
        open(target, "w", encoding="utf-8") as ftarget
    ):
        for line in fsursa:
            ftarget.write(line)

# modificați funcția `cp()` astfel încât
# să îi adăugăm argumentul `overwrite`, default `False``:
def cp(source, target, overwrite=False):
    mode = "w" if overwrite else "x"

    with (
        open(source, "r", encoding="utf-8") as fsursa,
        open(target, mode, encoding="utf-8") as ftarget
    ):
        for line in fsursa:
            ftarget.write(line)

# modificați funcția cp() astfel încât
# să funcționeze în mod binar
def cp(source, target, overwrite=False, chunk=8192):
    mode = "wb" if overwrite else "xb"

    with(
        open(source, 'rb') as src,
        open(target, mode) as tgt
    ):
        while content := src.read(chunk): 
            tgt.write(content)


