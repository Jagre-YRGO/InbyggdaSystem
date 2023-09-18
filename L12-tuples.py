def my_funciton(argument):
    print(argument)
    for i in range(0,len(argument)):
        argument[i] = 'a' + argument[i]
    return

my_orginal_list = ('1','2','3')
#Illegal call - will try to change a tuple
#my_funciton(my_orginal_list)
print(my_orginal_list)

my_orginal_list = 'apa'
print(my_orginal_list)

