import sqlite3
import simplejson
import pypandoc
conn = sqlite3.connect('decret.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
instruccio = 'SELECT comp_num, comp_desc FROM "competencia" WHERE comp_ambit=2'
cur.execute(instruccio)
# De moment la consulta la fa bé. Afegim diccionaris
valor = []
descripcio = []
for row in cur.fetchall():
    valor.append(row[0])
    descripcio.append(row[1])
result = {'Taula': {'N_competencia': valor, 'Text competencia': descripcio}}
cur.close()
# codificat = json.JSONEncoder().encode(result)
# Escrivim a arxiu:
with open("decret.json", "w") as outfile:
    simplejson.dump(result, outfile, indent=(4))
output = pypandoc.convert_file('decret.json', 'odt', format='json', outputfile="somefile.odt")
