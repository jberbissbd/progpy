import sqlite3
import simplejson
import pypandoc
import xml.etree.ElementTree as ET
import dicttoxml

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
    result["NUMERO COMPETENCIA"].append(row[0])
    result["TEXT COMPETENCIA"].append(row[1])
cur.close()
# dades_xml = result.encode()
# codificat = json.JSONEncoder().encode(result)
# Escrivim a arxiu json:
# with open("decret.json", "w") as outfile:
    # simplejson.dump(result, outfile, indent=(4))
# output = pypandoc.convert_file('decret.json', 'odt', format='json', outputfile="somefile.odt")
processament = dicttoxml.dicttoxml(result)
print(processament)
doc = ET.fromstring(processament)
arbre = ET.ElementTree(doc)
arbre.write("prova_xml.xml", encoding="utf-8")
output = pypandoc.convert_file('prova_xml.xml', 'odt', format='html', outputfile="somefile.odt")
