import random

from brain_games.cli import get_user_name, welcome_user
from brain_games.engine import game_engine
from brain_games.scripts.brain_games import greet


def get_question() -> str:
    progression_list = []
    start_value = random.randint(0, 25)
    step = random.randint(1, 10)
    progression_lenght = random.randint(10, 10)
    for index in range (progression_lenght):
        current_element = start_value + index * step
        current_element = str(current_element)
        progression_list.append(current_element)
    replacement_index = random.randint(0, progression_lenght-1)
    progression_list[replacement_index] = ".."
    result = " ".join(progression_list)
    return result


def get_correct_answer(question: str) -> str:
    question_list = question.split()
    required_index = question_list.index("..")
    if required_index + 2 > len(question_list):
        major_number = question_list[required_index-1]
        minor_number = question_list[required_index-2]
    else:
        major_number = question_list[required_index+1]
        minor_number = question_list[required_index+2]
    major_number = int(major_number)
    minor_number = int(minor_number)
    step = major_number - minor_number
    required_number = major_number + step
    return str(required_number)


RULES = "What number is missing in the progression?"


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
