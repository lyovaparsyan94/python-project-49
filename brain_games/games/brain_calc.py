from random import choice, randint
from brain_games.cli import welcome_user
from brain_games.scripts.game_rules import ask_question, compare_answer
from brain_games.scripts.game_rules import ROUND_LIMIT


def calculate(name):
    round_counter = 0
    operands = ['*', '-', '+']
    while round_counter < ROUND_LIMIT:
        print(round_counter, ROUND_LIMIT)
        left_number = randint(1, 100)
        right_number = randint(1, 100)
        action = choice(operands)
        expression = f"{left_number} {action} {right_number}"
        result = eval(expression)
        print('What is the result of the expression?')
        answer = ask_question(f'Question: {expression}')
        round_counter += 1
        right_answer = compare_answer(user=name, answer=answer, result=result)
        if right_answer is False:
            return


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
