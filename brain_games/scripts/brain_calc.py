import random

from brain_games.engine import game_engine

from brain_games.cli import get_user_name, welcome_user
from brain_games.scripts.brain_games import greet


def get_question() -> str:
    operators = ("+", "-", "*")
    operator = random.choice(operators)
    if operator == "*":
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
    else:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
    question = f'{str(number_1)} {str(operator)} {str(number_2)}' 
    return question


def get_correct_answer(question: str) -> str:
    number_1, operator, number_2 = question.split()
    match operator:
        case "+":
            result = int(number_1) + int(number_2)
        case "-":
            result = int(number_1) - int(number_2)
        case "*":
            result = int(number_1) * int(number_2)
    return str(result)        


RULES = "What is the result of the expression?"


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
