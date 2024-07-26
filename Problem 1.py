# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:37:01 2023

@author: micke
"""


s = 'azcbobobegghakl'

def numberOfVowels(s):
      '''
      Input: A string with only lowercase
      Output: The number of vowel it has.
      '''
      count = 0
      vowels = "aeiou"
      for letter in s:
           if letter in vowels:
               count += 1
      return count
  
print(numberOfVowels(s))