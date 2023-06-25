from moduls.bbdd import InformadorMateria, Lectorsabers,Lectormateries, Lectorsblocs, Lectorcriteris, LectorMateriesCompletes, Lectorcompetencies
encoding = 'utf-8'

encoding = 'utf-8'


b = LectorMateriesCompletes(0)
b.taula= "taula_falsa"
c = b.combinar_info_materies()

print(c)
