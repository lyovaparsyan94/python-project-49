from random import choice, randint
from brain_games.scripts.game_engine import run_game


def generate_question_and_answer():
    operands = ['*', '-', '+']
    left_number = randint(1, 100)
    right_number = randint(1, 100)
    action = choice(operands)
    question = f"{left_number} {action} {right_number}"
    correct_answer = str(eval(question))
    return question, correct_answer


def main():
    game_rule = 'What is the result of the expression?'
    run_game(generate_question_and_answer, game_rule, "Calculate Game")


if __name__ == "__main__":
    main()
