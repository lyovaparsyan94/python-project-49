from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.game_rules import ask_question, compare_answer
from brain_games.scripts.game_rules import ROUND_LIMIT


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def calculate(name):
    round_counter = 0
    while round_counter < ROUND_LIMIT:
        length = randint(5, 10)
        start = randint(1, 10)
        step = randint(1, 10)
        progression = generate_progression(start, step, length)

        hidden_index = randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = '..'

        progression_str = ' '.join(map(str, progression))

        print('What number is missing in the progression?')
        answer = ask_question(f'Question: {progression_str}')
        round_counter += 1
        right_answer = compare_answer(user=name, answer=answer, result=correct_answer)
        if right_answer is False:
            return


def main():
    name = welcome_user()
    calculate(name)


if __name__ == "__main__":
    main()
