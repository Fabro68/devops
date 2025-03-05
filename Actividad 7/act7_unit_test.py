# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 18:27:30 2025

@author: angel
"""
import unittest

class TestRacionales(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
if __name__ == '__main__':
    unittest.main()
    