def print_greeting():
    """FFFFunciton that takes no arguments and prints welcome text"""
    #Dett är en kommentar
    print('Welcome to 10:th lession in Inbyggda System 2')

for i in range(0,10):
    print_greeting()
    break

while True:
    favorite_number = input('Tell me your favorite number!')
    if int(favorite_number) == 0:
        break
    print(f'your favorite number is:{favorite_number}')
