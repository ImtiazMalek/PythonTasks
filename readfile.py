employee_message=open("open.txt","r+")
print(employee_message.read())
for employee in employee_message.readlines():
    print(employee)
reply=input('Thank you boss, i am also looking forwond to that')
employee_message.write(reply)
employee_message.close()