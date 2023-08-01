# encoding = 'utf-8'
import pprint as pp
from progpy.moduls.curriculum import InformadorGlobal  # pylint: disable=import-error
from progpy.moduls.estudis import GeneradorArbreMateries

a = GeneradorArbreMateries(1).obtenir_materies_curs(1)
pp.pprint(a, compact=True)
