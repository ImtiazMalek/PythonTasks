num1=float(input('Enter a number: '))
op=input('Enter an operator: ')
num2=float(input('Enter another number: '))
#condition for calculator
if op == "+":
    print("%.2f"%(num1+num2))
elif op == "-":
    print("%.2f"%(num1-num2))
elif op == "*":
    print("%.2f"%(num1*num2))
elif op == "/":
    print("%.2f"%(num1/num2))
else:
    print("Invalid operator")
# "%.2f"% is for two decimal place value
