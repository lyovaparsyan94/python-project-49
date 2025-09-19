def generate_round():
    question = "2 + 2"
    answer = "4"
    return question, answer

import random
from brain_games.cli import welcome_user
import operator

OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul}

def get_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(list(OPS.keys()))
    return num1, num2, op

def play():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        num1, num2, op = get_question()
        print(f"Question: {num1} {op} {num2}")
        answer = input("Your answer: ").strip()
        correct_answer = str(OPS[op](num1, num2))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")