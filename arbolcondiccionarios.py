#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:42:19 2020

@author: nautica
"""
#diccionario vacio
miarbol=[]
miarbol.append({1:[2,3,6,7]})
miarbol.append({2:[4]})
miarbol.append({3:[]})
print(miarbol)
print(miarbol[1].values())
for nodos in miarbol:
    print(nodos)
    for key,values in nodos.items():
        print(key,values)
        