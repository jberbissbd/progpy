from moduls.bbdd import InformadorMateria, Lectorsabers

encoding = 'utf-8'

a = InformadorMateria(1).obtenir_criteris_materia(1)
b = Lectorsabers(1).segons_bloc_materia(1, 1)

print(b)
