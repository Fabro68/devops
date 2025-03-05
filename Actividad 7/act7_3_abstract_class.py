# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:58:38 2025

@author: angel
"""

from abc import ABC, abstractmethod

class AbsNumeros (ABC):
    
    @abstractmethod
    def print_numeros(self):
        pass
    
class Racionales(AbsNumeros):
    def __init__(self,n):
        self.n = n
    def print_numeros(self):
        print("El numero racional es: ", self.n)
        print ("El numero racional en forma de fraccion es: " ,self.n.as_interger_ratio())
            