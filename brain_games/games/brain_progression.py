def generate_round():
    question = "1 2 3 4 5"
    answer = "5"
    return question, answer

import random
from brain_games.cli import welcome_user

def generate_progression(length=10):
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    return [start + step * i for i in range(length)]

def play():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers < 3:
        progression = generate_progression()
        hidden_index = random.randint(0, len(progression) - 1)
        correct_answer = str(progression[hidden_index])
        progression[hidden_index] = ".."
        print(f"Question: {' '.join(map(str, progression))}")
        answer = input("Your answer: ").strip()
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")