from random import choice, randint

RULES = "What is the result of the expression?"


def get_question() -> str:
    operators = ("+", "-", "*")
    operator = choice(operators)

    if operator == "*":
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
    else:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)

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


