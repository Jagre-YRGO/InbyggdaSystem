def is_prime(number):
    '''returns True if argument is prime'''
    if number == 1:
        return True
    #itterera från 2 till (argument-1)
    for i in range(2,number):
        #om modulo ger 0 på något tal så är argument inte ett primtal
        if number % i == 0:
            return False
    #Inget tal funnet som går jämnt upp i argument -> primtal!
    return True

while True:
    test_number_string = input('Ange tal att prova:')
    if int(test_number_string)==0:
        break
    if is_prime(int(test_number_string)):
        print(f'{test_number_string} är ett primtal!')
    else:
        print(f'{test_number_string} är INTE ett primtal!')