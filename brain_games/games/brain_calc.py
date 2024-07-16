from random import choice, randint
from brain_games.cli import welcome_user
from brain_games.scripts.game_rules import ask_question, compare_answer
from brain_games.scripts.game_rules import ROUND_LIMIT


def calculate(name):
    round_counter = 0
    operands = ['*', '-', '+']
    while round_counter < ROUND_LIMIT:
        left_number = randint(1, 100)
        right_number = randint(1, 100)
        action = choice(operands)
        expression = f"{left_number} {action} {right_number}"
        result = eval(expression)
        print('What is the result of the expression?')
        answer = ask_question(f'Question: {expression}')
        right_answer = compare_answer(answer=answer, result=result)

        if right_answer:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
