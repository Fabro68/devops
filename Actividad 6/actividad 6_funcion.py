# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:07:58 2025

@author: angel
"""

print("Hola Angel Fabro,Ingrese numero entero")
n = int(input())

try:
    print("El numero ingresado es:", n)

    for number in range (n):
        if((n % 2)==0):
            print("El residuo es:", number % 2)
            print("El numero es: " , number)
        else:
            print("El cuadrado del numero es" , pow(number, 2))
except:
    print("La entrda no es un numero entero")


    