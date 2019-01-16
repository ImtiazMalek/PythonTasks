counter=0
limit = int(input('How many time you wanna guess? :'))
correct_word = 'panda'
check =False
#taking the guesses
while counter<limit:
    guess=input('Guess a word: ')
    if guess == correct_word:
        check=True
        break
    counter+=1
#checking the boolean
if check:
    print('You win')
else:
    print('You lose')