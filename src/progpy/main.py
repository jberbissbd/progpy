# encoding = 'utf-8'
import pprint as pp
from progpy.moduls.bbdd.bbdd import Lectorbbdd

a = Lectorbbdd(1)
pp.pprint(a.ruta_arxiu_bbdd, compact=True)
