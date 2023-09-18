f = open('my_names.txt',mode='w')
f.close()

while True:
    input_string = input('Give me a name:')
    f = open('my_names.txt',mode='a')
    f.write(input_string.title() + '\n')
    f.close()

