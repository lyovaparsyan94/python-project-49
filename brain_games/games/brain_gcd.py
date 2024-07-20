from random import randint
from brain_games.scripts.game_engine import run_game


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_question_and_answer():
    left_number = randint(1, 100)
    right_number = randint(1, 100)
    question = f"{left_number} {right_number}"
    correct_answer = str(gcd(left_number, right_number))
    return question, correct_answer


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    run_game(generate_question_and_answer, game_rule, "GCD Game")


if __name__ == "__main__":
    main()
