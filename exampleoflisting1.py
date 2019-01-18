#taking inputs
names=[input('Enter a name:') for number in range(int(input('How many names you want to include?: ')))]
check=input('Enter a name you wanna find: ')
result= False
#checking for the condition
for name in names:
    if check==name:
        result=True
        break
#matching boolean
if result:
    print('He is listed')
else:
    print('He/she is not listed')