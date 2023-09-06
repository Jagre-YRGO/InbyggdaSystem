def is_retired(a,retirement_age=64):
    if a > retirement_age:
        return True
    else:
        return False

age = int(input('Tell me your age!\n'))
print(f'Your age is {age}')

while age != 0:
    if is_retired(a=age):
        print('you are retired!')
    else:
        print('you are in working age')

    age = int(input('Tell me your age!\n'))
