from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greet()


if __name__ == "__main__":
    main()