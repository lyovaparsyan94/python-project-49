from random import randint
from brain_games.scripts.game_engine import run_game


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_question_and_answer():
    length = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    progression = generate_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    progression_str = ' '.join(map(str, progression))
    question = progression_str
    return question, correct_answer


def main():
    game_rule = 'What number is missing in the progression?'
    run_game(generate_question_and_answer, game_rule, "Progression Game")


if __name__ == "__main__":
    main()
