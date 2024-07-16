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
        right_answer = compare_answer(answer=answer, result=correct_answer)

        if right_answer:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
