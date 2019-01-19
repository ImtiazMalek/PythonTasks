a=0
read=[input() for number in range(int(input('No. of rows: ')))]
write=[input() for number in range(int(input('No. of columns: ')))]
for count1 in read:
    for count2 in write:
        print(count1,count2)