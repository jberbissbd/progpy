# encoding = 'utf-8'
import pprint as pp
from progpy.moduls.bbdd import LectorMateriesCompletes, Lectorcompetencies, InformadorMateriaPlantilla, LectorMateriesCompletes, LectorCursos, InformadorTransversals  # pylint: disable=import-error

a = InformadorTransversals(0).obtenir_transversals_materia(1)
    

pp.pprint(a,compact=True)