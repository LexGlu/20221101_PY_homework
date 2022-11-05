import random


def math_quiz():
    operators = ['+', '-', '*', '**', '//', '%']
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(operators)
    quiz = f'{a} {operator} {b}'
    res = eval(quiz)
    answer = input(f'Enter answer for the following mathematical expression: {quiz}\n')
    if answer.isdigit() or answer[0] == '-' and answer[1:].isdigit():
        if int(answer) == res:
            print("That's correct!")
        else:
            print(f"WRONG! Correct answer is {res}")
    else:
        print("Please enter valid integer")
    next_try = input('Do you want to try again? Enter "y" if you are positive or anything else to stop.\n')
    if next_try == 'y':
        math_quiz()

        
math_quiz()
