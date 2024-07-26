# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:01:38 2023

@author: micke
"""

s = 'azcbobobegghakl'


def numberOfTimesBob(s):
     '''
     Input: A string of lower case characters
     Output: Returns the number of times bob occurs
     '''
     st = 0
     e = 3
     nBob = 0 
     c = 0
     while c < len(s):
         w = s[st:e]
         if w == "bob":
             nBob += 1
         c += 1
         st += 1
         e += 1
     return nBob
 
print(numberOfTimesBob(s))
         