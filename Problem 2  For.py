# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:26:09 2023

@author: micke
"""

s = 'azcbobobegghakl'

def numberOfTimesBob(s):
     '''
     Input: A string of lower case characters
     Output: Returns the number of times bob occurs
     '''
     nBob = 0
     for i in range(len(s)):
            w = s[i:i+3]
            if w == "bob":
                nBob += 1
     return nBob
         
 
print(numberOfTimesBob(s))