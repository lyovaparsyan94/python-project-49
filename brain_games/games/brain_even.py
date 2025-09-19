import random

from brain_games.cli import welcome_user


def generate_round():
    question = "2"
    answer = "even"
    return question, answer


def is_even(number):
    return number % 2 == 0


def get_question():
    return random.randint(1, 100)


def play():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = get_question()
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    play()
