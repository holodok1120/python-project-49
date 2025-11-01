from random import randint

from brain_games.cli import get_user_name, welcome_user
from brain_games.engine import game_engine
from brain_games.scripts.brain_games import greet


def get_question() -> int:
    return randint(0, 100)


def get_correct_answer(question: int) -> str:
    return 'yes' if is_prime(question) else 'no'


def is_prime(number: int) -> bool:
    if number in (0, 1):
        return False
    if number in (2, 3):
        return True
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
