# encoding = 'utf-8'
from progpy.moduls.bbdd import LectorMateriesCompletes  # pylint: disable=import-error


b = LectorMateriesCompletes(1)
b.taula = "materies_completes"
print(b.ruta_arxiu_bbdd)
c = b.combinar_info_materies()

print(c)
