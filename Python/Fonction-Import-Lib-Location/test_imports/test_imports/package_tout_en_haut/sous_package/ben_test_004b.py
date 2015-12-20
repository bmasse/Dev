#from __future__ import absolute_import

import os
import sys

# Doit etre appele par un autre script plus haut pour avoir les deux test_imports.

rep=sys.path
print("liste de PYTHONPATH:")
for item in rep:
    print(item)


#import test_imports

#from test_imports import package_tout_en_haut
#from test_imports.package_tout_en_haut import sous_package
from . import test_imports
from .test_imports import sous_module

sous_module.toto()
sous_module.toto1()
sous_module.toto2()

import test_imports
from test_imports import top_module
from test_imports import package_tout_en_haut
from test_imports.package_tout_en_haut import sous_package

top_module.toto()
top_module.toto1()
top_module.toto2()
