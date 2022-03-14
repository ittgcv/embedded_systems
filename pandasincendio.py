import pandas as pd
data = pd.read_csv("dataall.csv") 
# muestra los nombres de las columnas
print(data.columns)
# pone nombres a las columnas
data.columns=['latitud', 'longitud', 'maximo', 'distancia']
print(data.columns)
# imprime los primeros datos
print(data.head())
# ordena los datos tomando como referencia una columna en orden ascendente
data.sort_values(by=['distancia'], inplace=True)
print(data.head())
# ordena los datos en forma descendente
data.sort_values(by=['distancia'], inplace=True,  ascending=False)
print(data.head())
# ordena por varias columnas
data.sort_values(by=['maximo','distancia'], inplace=True)
print(data.head())
# accesando a los datos de una columna
print(data['longitud'])
# accesando ciertos renglones
print(data[600:605])
# accesando un dato en particular
print(data.loc[601])
print(data.loc[601, 'maximo'])
# indices booleanos
print(data[data['distancia']>30])
#for i, rows in data.iterrows():
   # print(i, rows)
