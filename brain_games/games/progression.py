from random import randint

RULES = "What number is missing in the progression?"


def get_question() -> str:
    progression_list = []
    start_value = randint(0, 25)
    step = randint(1, 10)
    progression_lenght = randint(5, 10)

    for index in range(progression_lenght):
        current_element = str(start_value + index * step)
        progression_list.append(current_element)

    replacement_index = randint(0, progression_lenght - 1)
    progression_list[replacement_index] = ".."
    result = " ".join(progression_list)
    return result


def get_correct_answer(question: str) -> str:
    question_list = question.split()
    required_index = question_list.index("..")

    if required_index + 2 > len(question_list):
        major_number = question_list[required_index - 1]
        minor_number = question_list[required_index - 2]
    else:
        major_number = question_list[required_index + 1]
        minor_number = question_list[required_index + 2]

    major_number = int(major_number)
    minor_number = int(minor_number)
    step = major_number - minor_number
    required_number = major_number + step
    return str(required_number)
