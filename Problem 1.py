# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:36:48 2023

@author: micke
"""
'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''


def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
                   months = 12
                   for m in range(months):
                       payment = balance * monthlyPaymentRate
                       monthlyInterest = annualInterestRate/12.0
                       unpaid = balance - payment
                       remainingBalance = unpaid + (monthlyInterest * unpaid)
                       balance = remainingBalance
                   return balance
    
    
    
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

print(round(remainingBalance(balance, annualInterestRate, monthlyPaymentRate),2))
