# encoding = 'utf-8'
import pprint as pp
from progpy.missatgeria import NovaProgramacio, Programacio
from progpy.moduls.bbdd.usuari import ControladorProgramacions

nova = NovaProgramacio("Curs", "Curs de prova")
antiga = Programacio(1, "Antiga", "Antiga", 0.0)

a = ControladorProgramacions(0)
a.actualitzar_programacio(antiga)

