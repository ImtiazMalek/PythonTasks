imtiaz= True
password= True
#checking the condition,
#in this case, it is boolean function
if imtiaz and password:
    print('Welcome imtiaz,\nwe missed you.')
elif imtiaz and not(password):
    print('Welcome imtiaz,\nUnfortunately your password is wrong.')
elif not(imtiaz) and password:
    print('Welcome Admin\nBut the user name is wrong.')
else:
    print('Your user name and password are incorrect\nTry again.')