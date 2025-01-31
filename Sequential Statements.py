salary = float(input("Enter your salary: ").replace(",",""))
numDependents = int (input("Enter the number of dependents: "))

stateTax = salary * 0.065

federalTax = salary * 0.28

dependentDeduction = salary * 0.025 * numDependents

totalWithholding = stateTax + federalTax + dependentDeduction

takeHomePay = salary - totalWithholding

print(f"/nState Tax: ${stateTax:.2f}")
print(f"Federal Tax: ${federalTax:.2f}")
print(f"Dependents: ${dependentDeduction:.2f}")
print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")