try:
    age = int(input('Enter your age: '))
    result = "%.2f"%(10/age)
    name = input('Enter a name: ')
    test = True
    print('Hello %s'%name+'\nYour score is %s'%result)
except ZeroDivisionError as err:
    print(err)
except ValueError as val_err:
    print('Invalid input')