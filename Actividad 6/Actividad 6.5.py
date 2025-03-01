# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:17:06 2025

@author: angel
"""

def print_numbers():
    for number in range(n):
        if ((n % 2)==0):
            print("El numero ingresado es: " , number)
        else:
            print("El cuadrado del numero es: ", number ** 2)
            
print("Ingresa un numero entero")
try:
    n = int(input())
    print("El numero que ingresaste es: ", n)
    
    print_numbers()
    
except:
    print("Ingresa un numero valido")
    