name=input('Enter your name: ')
age=input('Enter your age: ')
def greettings(name:str,age:str):
#returning an action
 return f'Hello {name},\nYou are: {age}'
user=greettings(name,age)
print("Good morning\n"+user)