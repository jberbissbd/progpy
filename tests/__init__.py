"""Configuració inicial per als tests"""

import sys
import os
from os.path import dirname, join
sys.path.append(os.path.abspath(join(dirname((dirname(__file__))),
                                     "src/moduls")))
