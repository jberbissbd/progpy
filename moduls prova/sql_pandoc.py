import sqlite3
import simplejson
import pypandoc
import ast

conn = sqlite3.connect('decret.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
instruccio = 'SELECT comp_num, comp_desc FROM "competencia" WHERE comp_ambit=2'
cur.execute(instruccio)
# De moment la consulta la fa bé. Afegim diccionaris
valor = []
descripcio = []
# Que, per cada fila, valor sigui el numero i descripcio el text de la competencia:
for row in cur.fetchall():
    valor.append(row[0])
    descripcio.append(row[1])
result = {'N_competencia': valor, 'Text competencia': descripcio}
cur.close()
# Escrivim a arxiu json, però amb AST (Abstract Syntax Tree):
result_ast = ast.parse(result)
with open("decret.json", "w") as outfile:
    ast.dump(result_ast)
output = pypandoc.convert_file('decret.json', 'odt', format='json', outputfile="somefile.odt")
