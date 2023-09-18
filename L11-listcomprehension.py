f = open('some_csv_numbers.csv')

my_lis_of_numbers = []
my_integers = []

for line in f:
    my_integers = [int(i) for i in line.split(',')]
    my_lis_of_numbers.append(my_integers)

f.close()

print(my_lis_of_numbers[1][1])

