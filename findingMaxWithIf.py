num1=input('Enter a number: ')
num2=input('Enter another number: ')
num3=input('Enter another number: ')
#condition
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
max= max_num(float(num1),float(num2),float(num3))
print('The maximum number is: '+"%.2f"%max)
# "%.2f"% means printing a decimal number upto two decimal point