# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:36:33 2025

@author: angel
"""

class Entero:
    def __init__(self,n):
        self.n = n
        
    def print_numbers(self):
        for number in range(self.n):
            if((self.n%2)==0):
                print("El numero es: ", number)
            else:
                print("El cuadrado del numero es: ", number**2)
print("Ingrese un numero: ")
num = int(input())
entero = Entero(num)
entero.print_numbers()
            