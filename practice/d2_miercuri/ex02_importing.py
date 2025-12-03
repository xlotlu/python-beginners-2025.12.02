#############
# forma nr. 1
#############
#import modul 
import os
import sys

# variațiune la forma 1:
# import fully.qualified.symbol
import os.path
# rezultă în import os (importă tot tree-ul)

# forma nr. 1 cu alias-uri
import os as myos

##############
# forma nr. 2:
##############
# from modul import simbol
from os import path
from os.path import join


# forma nr. 2 cu alias-uri: 
from os.path import join as myjoin


####
# notă importantă:
# putem să importăm multiplu
####

from os.path import join, abspath, normpath, isdir, isfile

from os.path import (
    join,
    abspath,
    normpath,
    isdir,
    isfile,
)

import sys, os # preferabil fiecare pe o linie


####
# altă notă:
# putem să importăm toate simbolurile dintr-un modul
####

from os.path import * # preferabil nu faceți asta
                      # ca să nu "poluați" mediul curent



# Întrebare: care sunt directoarele din care se încarcă un modul la import?
# Răspuns: vezi sys.path