counter=int(input('How many name you wanna input? : '))
number=['']*counter
start =0
test= False
#taking inputs
while start<counter :
    name=input('Enter a name: ')
    number[start]=name
    start+=1
#asking for required name
show =input('Which name you wanna search? : ')
start=0
#searching result
while start<counter:
    if show == number[start]:
        test = True
        break
    start+=1
#result showing,using if condition
if test:
    print('Result: This name has been included')
else:
    print('Result: The parson is not here')