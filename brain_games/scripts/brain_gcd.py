import random

from brain_games.cli import get_user_name, welcome_user
from brain_games.engine import game_engine
from brain_games.scripts.brain_games import greet


def get_question() -> str:
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{str(number_1)} {str(number_2)}' 
    return question


def get_correct_answer(question: str) -> str:
    number_a, number_b = question.split()
    number_a = int(number_a)
    number_b = int(number_b)
    while number_b != 0:
        temporary_variable = number_b
        number_b = number_a % number_b
        number_a = temporary_variable
    return str(number_a)       


RULES = "Find the greatest common divisor of given numbers."


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
