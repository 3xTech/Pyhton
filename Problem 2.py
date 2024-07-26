# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:02:22 2023

@author: micke
"""

def remainingBalance(balance, annualInterestRate, fixedPayment):
                   months = 12
                   for m in range(months):
                       monthlyInterest = annualInterestRate/12.0
                       unpaid = balance - fixedPayment
                       remainingBalance = unpaid + (monthlyInterest * unpaid)
                       balance = remainingBalance
                   return balance
    
    
    
balance = 3329
annualInterestRate = 0.2
fixedPayment = 0
result = 1

while result > 0:
         fixedPayment += 10
         result = int(remainingBalance(balance, annualInterestRate, fixedPayment))

         
         
         
print(fixedPayment)




