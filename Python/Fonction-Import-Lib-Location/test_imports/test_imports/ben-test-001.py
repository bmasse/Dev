import sys
rep=sys.path
print("liste de PYTHONPATH:")
print(rep)
#for item in rep:
#    print(item)

import test_imports
from test_imports import package_tout_en_haut
from test_imports import top_module
from test_imports.package_tout_en_haut import sous_module


""" Va donner l'erreur suivante:
Traceback (most recent call last):
  File "C:\Data\Projets\Python-Dev\Fonction-Import-Lib-Location\test_imports\test_imports\ben-test-001.py", line 2, in <module>
    from test_imports import package_tout_en_haut
ImportError: cannot import name 'package_tout_en_haut'
"""


