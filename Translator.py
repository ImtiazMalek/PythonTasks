count=int(input('No. of names: '))
names=[input('Enter a name: ') for number in range(count)]
result=[]
total_vowel=0
for name in names:
    vowel_count=0
    new_name = ''
    for letter in name:
        if letter in 'AEIOUaeiou':
            new_name = new_name + '*'
            vowel_count +=1
            total_vowel +=1
        else:
            new_name=new_name+letter
    result.append(new_name+" | Total vowels:--> %s"%vowel_count)
check=input('Do you want to see the updated list?: ')
if check== "Yes" or check == "yes":
    #print(result)
    for name in result:
        if name==result[count-1]:
            print(name)
            print('And number of vowel in total:-->', total_vowel)
        else:
            print(name)
else:
    print('Number of vowel in total:-->', total_vowel)
    print("Good bye :) ")

