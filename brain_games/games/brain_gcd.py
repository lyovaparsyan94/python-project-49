from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.game_rules import ask_question, compare_answer
from brain_games.scripts.game_rules import ROUND_LIMIT


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def calculate(name):
    round_counter = 0
    while round_counter < ROUND_LIMIT:
        left_number = randint(1, 100)
        right_number = randint(1, 100)
        correct_answer = gcd(left_number, right_number)
        print('Find the greatest common divisor of given numbers.')
        answer = ask_question(f'Question: {left_number} {right_number}')
        round_counter += 1
        right_answer = compare_answer(user=name, answer=answer, result=correct_answer)
        if right_answer is False:
            return


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
