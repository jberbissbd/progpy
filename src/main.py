from moduls.bbdd import InformadorMateria, Lectorsabers,Lectormateries, Lectorsblocs
encoding = 'utf-8'

encoding = 'utf-8'

a = Lectormateries(0).llistar_materies_completes()
b = Lectorsabers(1).segons_bloc_materia(1, 1)
c = Lectorsblocs(1)
h = c.obtenir_blocs(999)
print(h)
