# encoding = 'utf-8'
import pprint as pp

from dataclasses import asdict, dataclass
from moduls.missatgeria import NovaProgramacio, Programacio
from progpy.moduls.bbdd.usuari import ControladorProgramacions
from progpy.moduls.bbdd.curriculum import Lectorcompetencies, Lectorcriteris, Lectorsabers
a = ControladorProgramacions(0).obtenir_programacions()
print(a)



