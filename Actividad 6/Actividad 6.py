# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:42:41 2025

@author: angel
"""

print("Hola Angel Fabro,Ingrese numero entero")
n = int(input())

try:
    print("El numero ingresado es:", n)

    for number in range (n):
        print(number)
except:
    print("la entrada no es un entero")