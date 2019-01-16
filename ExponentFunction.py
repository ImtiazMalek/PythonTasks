number=int(input('Enter a number: '))
pow=int(input('Enter a number: '))

#method

def getting_power(number,pow):
    result=1
    for index in range(pow):
        result=result*number
    return result

print('The result is',getting_power(number,pow))