import ujson
import pypandoc

llista_prova = ['hola', 'adeu', 'fins aviat']
a = ujson.dump(llista_prova,a)
# p = simplejson.JSONEncoder(t, for_json=True)
print(t)
# simplejson.parse(t)
# c = ujson.loads(t)
with open('data.json', 'w') as outfile:
    ujson.dumps(t, outfile)
output = pypandoc.convert_file('data.json', 'odt', outputfile="somefile.odt")
