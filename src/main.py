# encoding = 'utf-8'
from moduls.bbdd import LectorMateriesCompletes  # pylint: disable=import-error


b = LectorMateriesCompletes(0)
b.taula = "taula_falsa"
c = b.combinar_info_materies()

print(c)
