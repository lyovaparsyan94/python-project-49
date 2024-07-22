from random import choice, randint
from brain_games.scripts.game_engine import run_game


def compute_expression(left_number, right_number, action):
    if action == '+':
        return left_number + right_number
    elif action == '-':
        return left_number - right_number
    elif action == '*':
        return left_number * right_number
    else:
        raise ValueError(f"Unsupported operation: {action}")


def generate_question_and_answer():
    operands = ['*', '-', '+']
    left_number = randint(1, 100)
    right_number = randint(1, 100)
    action = choice(operands)
    question = f"{left_number} {action} {right_number}"
    correct_answer = str(compute_expression(left_number, right_number, action))
    return question, correct_answer


def main():
    game_rule = 'What is the result of the expression?'
    run_game(generate_question_and_answer, game_rule, "Calculate Game")
