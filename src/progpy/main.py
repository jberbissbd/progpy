# encoding = 'utf-8'
import pprint as pp
from progpy.moduls.bbdd import InformadorGlobal  # pylint: disable=import-error

a = InformadorGlobal(0).obtenir_informacio_global(1)
    

pp.pprint(a,compact=True)