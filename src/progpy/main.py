# encoding = 'utf-8'
import pprint as pp
from progpy.moduls.curriculum import InformadorGlobal  # pylint: disable=import-error
from progpy.moduls.estudis import GeneradorArbreMateries

a = GeneradorArbreMateries(0).obtenir_modealitats()
pp.pprint(a,compact=True)
