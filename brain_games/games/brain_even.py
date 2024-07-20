from random import randint
from brain_games.scripts.game_engine import run_game


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    number = randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question_and_answer, game_rule, "Even Game")


if __name__ == "__main__":
    main()
