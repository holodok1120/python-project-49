from brain_games.cli import get_user_name, welcome_user


def greet():
    print("Welcome to the Brain Games!")


def main():
    greet()
    welcome_user(get_user_name())


if __name__ == "__main__":
    main()
