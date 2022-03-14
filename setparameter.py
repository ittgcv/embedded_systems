# modifica un parametro
import json
import sys
with open('parameters.json', 'r') as fp:
    diccionario = json.load(fp)
print(diccionario)
# iteracion para cada argumento
print(sys.argv[1])
print(diccionario[sys.argv[1]])
print(len(sys.argv))