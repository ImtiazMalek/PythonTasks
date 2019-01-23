from Quiz import Question


quiz_prompt=[
    'what is the name of our cricket teams captain?\n(a)Mortuza\n(b)Sakib\n(c)Mushfiq\n\n',
    'How many districts are in Bangladesh?\n\n(a)64\n(b)72\n(c)7\n\n',
    'what is the color of banana?\n\n(a)Magenta\n(b)Red\n(c)Yellow\n\n'
]
questions=[
    Question(quiz_prompt[0],'a'),
    Question(quiz_prompt[1],'a'),
    Question(quiz_prompt[2],'c'),
    ]
def run_the_quiz(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print('Your score is '+str(score)+'/'+str(len(questions)))
run_the_quiz(questions)