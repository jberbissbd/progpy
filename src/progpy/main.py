# encoding = 'utf-8'
from progpy.moduls.bbdd import LectorMateriesCompletes # pylint: disable=import-error


b = LectorMateriesCompletes(1)
g = b.obtenir_materies()
print(g)
