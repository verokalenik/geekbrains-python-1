from sys import argv

script_name, hours, hourly_pay, bonus = argv

print('Salary', float(hours) * float(hourly_pay) + float(bonus))
