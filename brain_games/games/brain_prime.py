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
        right_answer = compare_answer(answer=answer, result=correct_answer)

        if right_answer:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
