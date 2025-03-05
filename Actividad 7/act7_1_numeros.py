# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:25:02 2025

@author: angel
"""
class Numeros:
    def __init__(self,n):
        self.n = n
        
    def print_numeros(self):
        for number in range(self.n):
            if((self.n%2)==0):
                print("El numero es:" , number)
                
            else:
                print("El cuadrado del numero es: ",number**2)
                
class Racionales(Numeros):
    def __init__(self, n):
        super().__init__(n)
        
    def print_numeros(self):
        print("EL numero racional es: ", self.n)
        print ("El numero racional en forma de fraccion es: " , self.n.as_interger_ratio())
        
        
    def print_hello(self):
        return "Hello Fabro"