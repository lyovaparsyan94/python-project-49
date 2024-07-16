from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.game_rules import ask_question, compare_answer
from brain_games.scripts.game_rules import ROUND_LIMIT


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate(name):
    round_counter = 0
    while round_counter < ROUND_LIMIT:
        number = randint(1, 100)
        correct_answer = "yes" if is_prime(number) else "no"

        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        answer = ask_question(f'Question: {number}')
        round_counter += 1
        right_answer = compare_answer(user=name, answer=answer, result=correct_answer)
        if right_answer is False:
            return


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
