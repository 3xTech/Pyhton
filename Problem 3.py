
def remainingBalance(balance, annualInterestRate, fixedPayment):
                   months = 12
                   for m in range(months):
                       monthlyInterest = annualInterestRate/12.0
                       unpaid = balance - fixedPayment
                       remainingBalance = unpaid + (monthlyInterest * unpaid)
                       balance = remainingBalance
                   return balance
    
    
    
balance = 1200
annualInterestRate = 0.2
monthlyInterest = annualInterestRate/12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterest)**12) / 12.0
fixedPayment = (upperBound + lowerBound)/2
x = 2

while x <-0.12 or x > 0.12:
         result = remainingBalance(balance, annualInterestRate, fixedPayment)
         if result < -0.12  :
                     upperBound = fixedPayment
         if result > 0.12 :
                     lowerBound = fixedPayment
         fixedPayment = (upperBound + lowerBound)/2
         x = result

fixedPayment = round(fixedPayment, 2)
print("Lowest Payment:", fixedPayment)