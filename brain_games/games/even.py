from random import randint

RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def get_question() -> int:
    return randint(1, 100)


def get_correct_answer(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
