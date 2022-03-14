import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
sql_command = """
CREATE TABLE tbmeasures ( 
idmeasure INTEGER PRIMARY KEY, 
measure VARCHAR(200));"""
#cursor.execute(sql_command)
sql_command = """
CREATE TABLE catproducto ( 
id_producto SMALLINT PRIMARY KEY, 
nombre VARCHAR(20), 
existencia SMALLINT, 
precio DECIMAL(5,2),
id_sucursal SMALLINT);"""
#cursor.execute(sql_command)
sql_command = """
CREATE TABLE catventa ( 
id_venta INTEGER PRIMARY KEY, 
id_producto SMALLINT, 
id_sucursal SMALLINT,
fecha VARCHAR(8),
precio DECIMAL(5,2));"""
#cursor.execute(sql_command)
sql_command = """
CREATE TABLE catentrada ( 
id_entrada INTEGER PRIMARY KEY, 
id_producto SMALLINT, 
id_sucursal SMALLINT,
cantidad SMALLINT);"""
#cursor.execute(sql_command)
sql_command = """
CREATE TABLE catsucursal ( 
id_sucursal INTEGER PRIMARY KEY, 
sucursal VARCHAR(20));"""
#cursor.execute(sql_command)

# agrega lectura
sql_command = """INSERT INTO tbmeasures (idmeasure, measure)
    VALUES (0, "hola mundo");"""
cursor.execute(sql_command)
# agrega datos de sucursales
sql_command = """INSERT INTO catsucursal (id_sucursal, sucursal)
    VALUES (NULL, "Pimienta");"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO catsucursal (id_sucursal, sucursal)
    VALUES (NULL, "Seguro torre");"""
#cursor.execute(sql_command)
# agrega productos a una sucursal
articulos=[("papel", 500, 0.2), ("memoria usb 16gb", 2, 150.0)]
for p in articulos:
    format_str = """INSERT INTO catproducto (id_producto, nombre, existencia, precio)
    VALUES (NULL, "{first}", "{last}", "{gender}");"""
    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2])
    #cursor.execute(sql_command)
#update usuarios set nombre='Marceloduarte', clave='Marce'
  #where nombre='Marcelo';
#cursor.execute("SELECT * FROM catproducto")
print("fetchall:")
#result = cursor.fetchall()
#for r in result:
#    print(r)
#cursor.execute("SELECT * FROM catproducto")
#print("\nfetch one:")
#res = cursor.fetchone()
#print(res)
cursor.execute("SELECT * FROM tbmeasures")
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
connection.commit()
connection.close()
