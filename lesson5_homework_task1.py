my_file = open('file.txt', 'w')

while True:
    inp_str = input('Enter string (empty to complete): ')
    if inp_str:
        my_file.write(inp_str + '\n')
    else:
        break
