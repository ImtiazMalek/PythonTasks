counter =int(input('Enter how many name you wanna enter: '))

family=['']*counter   # *counter help the list to determined
                      #How many in element will be in the list

for index in range(counter):
    name = input('Enter a name: ')
    family[index]=name
for index in range (counter):
    print(family[index])