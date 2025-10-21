from random import randint

from brain_games.engine import game_engine

from brain_games.cli import get_user_name, welcome_user
from brain_games.scripts.brain_games import greet


def get_question() -> int:
    return randint(1, 100)


def get_correct_answer(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    greet()
    user_name = get_user_name()
    welcome_user(user_name)
    game_engine(
        rules=RULES,
        user_name=user_name,
        get_question=get_question,
        get_correct_answer=get_correct_answer
    )


if __name__ == '__main__':
    main()
