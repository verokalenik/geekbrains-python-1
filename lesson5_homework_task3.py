with open('file1.txt', 'r') as my_file:
    lines = my_file.readlines()
    employees = [{'name': line.split(' ')[0], 'salary': float(line.split(' ')[1])} for line in lines]

    for emp in employees:
        if emp['salary'] > 20000:
            print(emp['name'])

    sum = 0
    for emp in employees:
        sum += emp['salary']
    print('Average salary ', sum / len(employees))

