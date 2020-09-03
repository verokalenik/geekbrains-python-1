dictionary = {
    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Щесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять'
}

in_file = open('file3.txt', 'r')
out_file = open('file4.txt', 'w')

for line in in_file:
    lst = line.split(' - ')
    out_file.write(dictionary[lst[0]] + ' - ' + lst[1] + '\n')

