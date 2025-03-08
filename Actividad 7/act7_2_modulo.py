# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:43:30 2025

@author: angel
"""

import act7_1_numeros
import act7_3_abstract_class

print ("Ingrese un numero")
n = int(input())
enteros = act7_1_numeros.Numeros(n)
enteros.print_numeros()
print("Ingrese un numero racional")

q=float(int(input()))
racionales = act7_1_numeros.Racionales(q)
racionales.print_numeros()

print("Ingrese un numero racional para el modulo abstracto")
m = float(input())
racionales = act7_3_abstract_class.Racionales(m)
racionales = act7_3_abstract_class.AbsNumeros()
racionales.print_numeros()
