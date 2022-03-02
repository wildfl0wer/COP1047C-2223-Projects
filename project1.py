"""""
A program that computes a person’s income tax. The program calculates the
income tax based on user inputs (gross income & number of dependents) and
the tax law. It then displays the income tax.
"""

TAX_RATE = .2                    # Universal flat tax rate of 20%
STANDARD_DEDUCTION = 10000.00    # Universal standard deduction
DEPENDENT_DEDUCTION = 3000.00    # Deduction per dependent

# Gross income must be entered to the nearest penny
grossIncome = float(input("Enter the gross income: "))

numDependents = input("Enter the number of dependents: ")
numDependents = float(numDependents)

taxableIncome = (grossIncome - STANDARD_DEDUCTION -
                (DEPENDENT_DEDUCTION * numDependents))

incomeTax = taxableIncome * TAX_RATE

# The income tax is expressed as a decimal number
# print (f"The income tax is ${incomeTax:.2f}")
print (f"The income tax is ${incomeTax}")
