# define parametros
# etiquetasusadas: 0=etiquetas mas significativas, 1=etiquetas resultantes del entrenamiento
import json
diccionario={"etiquetasusadas":1,"valorreferenciahotel":3.7,"valorreferenciaactividad":3.7}
print(diccionario["etiquetasusadas"])

with open('parameters.json', 'w') as fp:
    json.dump(diccionario, fp)
