import sys

import test_imports
from test_imports import package_tout_en_haut
from test_imports import top_module
from test_imports.package_tout_en_haut import sous_module

rep=type(test_imports)
print("test_imports is a ", rep)
type(top_module)
print("top_module is a ", rep)
type(package_tout_en_haut)
print("package_tout_en_haut is a ", rep)
type(sous_module)
print("sous_module is a ", rep)

top_module.toto()

rep=sys.path
print("liste de PYTHONPATH:")
for item in rep:
    print(item)


