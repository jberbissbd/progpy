import sqlite3
import pypandoc
from prettytable import PrettyTable

conn = sqlite3.connect('decret.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
instruccio = 'SELECT comp_num, comp_desc FROM "competencia" WHERE comp_ambit=2'
cur.execute(instruccio)
# De moment la consulta la fa bé. Afegim diccionaris
# valor = []
# descripcio = []
# El codi següent serveix per a JSON:
# for row in cur.fetchall():
    # valor.append(row[0])
    # descripcio.append(row[1])
# result = {'N_competencia': valor, 'Text competencia': descripcio}
# cur.close()
result = {"NUMERO COMPETENCIA":[], "TEXT COMPETENCIA":[]}
for row in cur.fetchall():
    result["NUMERO COMPETENCIA"].append(str(row[0]))
    result["TEXT COMPETENCIA"].append(str(row[1]))
cur.close()
differencia = {"a": 2, "b": 3, "c": 5}
result["NUMERO COMPETENCIA"].append('13')
result["TEXT COMPETENCIA"].append(differencia)
presult = PrettyTable(result)
print(result)
print(presult)
# Escrivim a arxiu json:
with open("decret.html", "w") as file:
    file.write(presult)
output = pypandoc.convert_file('decret.html', 'odt', format='html', outputfile="somefile.odt")
output2 = pypandoc.convert_file('decret.html', 'docx', format='html', outputfile="somefile.docx")
