import os
import sys

rep=sys.path
print("liste de PYTHONPATH:")
for item in rep:
    print(item)


import test_imports
from test_imports import sous_module

print("test_imports:", type(test_imports))
test_imports.sous_module.toto()
test_imports.sous_module.toto1()
test_imports.sous_module.toto2()

#Pour inclure le test_imports le plus haut, il faut que le plus haut soit dans PYTHONPATH.


