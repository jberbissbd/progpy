# from moduls import bbdd as base
import sys
# import os
from moduls import bbdd 
from bbdd import LectorMateriesCompletes

# sys.path.append("../")
print(sys.path)

encoding = 'utf-8'




encoding = 'utf-8'


b = LectorMateriesCompletes(0)
b.taula= "taula_falsa"
c = b.combinar_info_materies()

print(c)
