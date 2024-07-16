from brain_games.cli import welcome_user
import random
from brain_games.scripts.game_rules import ROUND_LIMIT
from brain_games.scripts.game_rules import ask_question


def is_even(number):
    return number % 2 == 0


def compare_answer(user, answer, result):
    if str(answer) != str(result):
        return False
    return True


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < ROUND_LIMIT:
        number = random.randint(1, 100)
        answer = ask_question(f"Question: {number}").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"
        right_answer = compare_answer(user=user_name,
                                      answer=answer,
                                      result=correct_answer
                                      )

        if right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
