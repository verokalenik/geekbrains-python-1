income = float(input('total income'))
costs = float(input('total costs'))
result = income - costs
if result > 0:
   print('profit', result)

   ratio = result / income
   print('ratio', ratio)

   employees = int(input('total number of employees'))
   profit_per_employee = result / employees
   print('profit per employee', profit_per_employee)

if result <= 0:
   print('loss', result)




