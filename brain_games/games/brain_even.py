from brain_games.cli import welcome_user
import random
from brain_games.scripts.game_rules import ROUND_LIMIT
from brain_games.scripts.game_rules import ask_question, compare_answer


def is_even(number):
    return number % 2 == 0


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < ROUND_LIMIT:
        number = random.randint(1, 100)
        answer = ask_question(f"Question: {number}").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"
        right_answer = compare_answer(result=correct_answer, answer=answer, user=user_name)
        correct_answers += 1
        if right_answer is False:
            return


if __name__ == "__main__":
    main()
