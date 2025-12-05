# exceptions, fully

def fac_chestii():
    fp = open("data/it-was.txt")

    try:
        # aici îmi fac treaba....

        1 / 0

    finally:
        print("!! închid fișierul !!")
        fp.close()

try:
    fac_chestii()
except ZeroDivisionError:
    print("nu știi... ceva")


# gramatica completă:


try:
    pass
except: # catch-all
    pass 


try:
    pass
except IndexError: # prinde doar asta
    pass 


try:
    pass
except IndexError: # prinde doar asta
    pass 
except KeyError: # alt branch
    pass 


try:
    pass
except (IndexError, KeyError): # un branch cu ambele
    pass 


try:
    pass
except IndexError: # prinde doar asta
    pass 
except KeyError: # alt branch
    pass 
except: # catch-all
    pass


try:
    pass
finally: # excepția nu e tratată, dar rulâm niște cod oricum
    pass


try:
    pass
except: # tratăm excepția...
    pass
finally: # ...dar rulâm niște cod oricum
    pass



try:
    pass
except: # tratăm excepția...
    pass
else:   # totul a fost în regulă
    pass
finally: # ...dar rulâm niște cod oricum
    pass