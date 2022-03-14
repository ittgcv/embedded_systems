# This Python file uses the following encoding: utf-8
# elimina caracteres extranios en una cadena
def limpiacadena(cadena):
    try:
        #vss=cadena.replace(" "," ").decode('utf-8')
        vss=cadena.replace("/"," ")
    except:
        print(cadena, 'hay caracteres no reconocidos')
    return vss

