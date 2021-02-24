import sqlite3
import pypandoc
from tabulate import tabulate
conn = sqlite3.connect('decret.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
instruccio = 'SELECT comp_num, comp_desc FROM "competencia" WHERE comp_ambit=2'
cur.execute(instruccio)
valor = []
descripcio = []
for row in cur.fetchall():
    valor.append(str(row[0]))
    descripcio.append(str(row[1]))
cur.close()
result = {"valors":valor,"descripcions":descripcio}
differencia = {'a': '2', 'b': '3', 'c': '5'}
# result.append(['codis', "\n".join(differencia)])
print(result)
result_html = tabulate(result, headers=["Numero competencia", "Text competencia"], tablefmt="html")
# Escrivim a arxiu json:
with open("decret.html", "w") as file:
    file.write(result_html)
output = pypandoc.convert_file('decret.html', 'odt', format='html', outputfile="somefile.odt")
output2 = pypandoc.convert_file('decret.html', 'docx', format='html', outputfile="somefile.docx")
