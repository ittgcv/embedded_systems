import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dbVentas.csv") 
# muestra los nombres de las columnas
print(data.columns)
print(data.head())
# total de venta por dia
print(data.groupby(['fecha']).sum())

# calcula una columna nueva 
data['year']=pd.DatetimeIndex(data['fecha']).year
data['month']=pd.DatetimeIndex(data['fecha']).month
data['month_year'] = pd.to_datetime(data['fecha']).dt.to_period('M')
print(data.head())
# calcula ventas por año
print(data.groupby(['year']).sum())
# calcula ventas por mes
venta2019=data[data['year']<2020]
print(data.groupby(['year','month']).sum())
print(data.groupby(['month_year']).sum())
# plotea la cantidad agrupada por mes
data[['month_year','cantidad']].groupby(['month_year']).sum().plot(kind='bar')
#plt.show()
dicts=data.groupby(['month_year']).sum().to_dict('index')
for key, value in dicts.items():
    print(key, value['precio'])
