import prompt

ROUND_LIMIT = 3


def ask_question(question):
    print(question)
    answer = prompt.string('Your answer: ')
    return answer


def compare_answer(user, answer, result):
    if str(answer) != str(result):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{result}'.\nLet's try again, {user}!")
        return False
    print(f"Correct!\nCongratulations, {user}!")
