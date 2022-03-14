#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:30:22 2020

@author: nautica
"""

lista=['a','b','c','d']
print(lista)
print(lista[2])
lista.append(4)
print(lista)
print(len(lista))
# accediendo a los datos individuales de una lista
for dato in lista:
    print(dato)
for i in range(len(lista)):
    print(i, lista[i])
# una lista dentro de otra lista
listadelista=[[1,2,3],[4,5]]
for dato in listadelista:
    print(dato)
    for i in dato:
        print(i)
# borrar un elemento de la lista
lista.remove('c')
print(lista)

# lista vacia
otra_lista=[]
print(otra_lista)
