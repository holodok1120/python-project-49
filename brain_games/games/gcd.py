from random import randint

RULES = "Find the greatest common divisor of given numbers."


def get_question() -> str:
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
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
