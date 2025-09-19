def generate_round():
    question = "8 12"
    answer = "4"
    return question, answer

import random
from brain_games.cli import welcome_user
import math

def get_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def play():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        num1, num2 = get_question()
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ").strip()
        correct_answer = str(math.gcd(num1, num2))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")