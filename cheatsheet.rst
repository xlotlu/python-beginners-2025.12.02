##########
cheatsheet
##########


Concepts:
=========

în Python, totul este o referință.


"callable": ceva ce poate fi executat, ca o funcție

"atribut": o proprietate a unui obiect, specifică lui

"metodă": o funcție agățată de un obiect
          (adică un atribut-funcție)

Python este self-documenting.

"iterator": ????
"yield":    ????


Essential debugging tools:
==========================

print()
help()


import ipdb
ipdb.set_trace()


Lucrat cu VSCode:
=================

Ctrl+F5     :: run code
Ctrl+/      :: comment block
Shift+Enter :: execută selecția într-un REPL persistent

«pe selecție» Tab / Shift+Tab :: indentare / dez-indentare



Usual Exceptions:
=================

SyntaxError, IndentationError
NameError, TypeError, ValueError


Installing packages:
====================

pip install ipython


# running ipython
python -m IPython


Lucrat cu IPython:
==================
Ctrl+l  :: clear
?(la sfărșit de linie) :: îți dă help




Metode utile de `str`:
======================

.split() / .join()


.replace()


.startswith() / .endswith()
.removesuffix() / .removepreffix()
.strip() / .lstrip() / .rstrip()

# dacă aveți de făcut output columnar:
.ljust() / .rjust() / .center()

.casefold() # dacă aveți de făcut comparații case-insensitive

.lower() / .upper()

.find() / .index() # "pythonic" este `index()`


.is*() # de știut că există



Essential wisdom
================

Există 2 probleme cu adevărat grele în computing:
- naming things
- cache invalidation
- off-by-one errors


PEP-8 :: the styleguide
https://peps.python.org/pep-0008/


OCD = "obsessive-compulsive disorder"


>>> import this


Există 10 tipuri de oameni, cei care știu binar și cei care nu știu.


Essentials skills:
- RTFM
- STFW
- ATFLLM ("prompt engineer")
- **debugging**

