import os
import sys

# cette commande ne fonctionne pas si on execute le fichier avec exec(open(nomdufichier).read())
#dossier = os.path.dirname(os.path.abspath(__file__))
# Le probleme avec le os.getcwd() est que si il est execute ailleurs, pas le repertoire courrant, il ne sera pas valide pour cette exemple.
# slick edit fait ca, il execute a partir du repertoire par defaut.
# Par contre, le PYTHON PATH inclus le repertoire contenant le fichier python execute.
dossier = os.getcwd()
dossier1 = ''
print ('dossier ', dossier)
dossier_valide=True

while not dossier.endswith('test_imports'):
    if dossier1 == dossier:
        dossier_non_valide=False
        break
    dossier1 = dossier
    dossier = os.path.dirname(dossier)
    
if dossier_valide==True:
    dossier = os.path.dirname(dossier)

    if dossier not in sys.path:
        print("Le dossier suivant ", dossier, " sera ajoute au sys.path")
        sys.path.append(dossier)

rep=sys.path
print("liste de PYTHONPATH:")
for item in rep:
    print(item)

import test_imports

