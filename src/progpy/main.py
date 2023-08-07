# encoding = 'utf-8'
import pprint as pp

from dataclasses import asdict, dataclass
from moduls.missatgeria import NovaProgramacio, Programacio
from moduls.bbdd.usuari import ControladorTemes, ControladorProgramacions

a = ControladorProgramacions(0)
a.obtenir_programacio(2)


