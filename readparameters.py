import json
with open('parameters.json', 'r') as fp:
    diccionario = json.load(fp)
print(diccionario)