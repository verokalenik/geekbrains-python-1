my_file = open('file.txt', 'r')

cnt = 0
for line in my_file:
    word_count = len(line.split(' '))
    print('In line ', cnt, ' we have ', word_count, ' words')
    cnt += 1
