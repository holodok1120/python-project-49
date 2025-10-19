from random import randint

import prompt

from brain_games.cli import get_user_name, welcome_user
from brain_games.scripts.brain_games import greet as brain_games_greet


def random_number():
    return randint(1, 100)


def is_even(value):
    if value % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_score = 1
    game_count = 0
    while game_count < 3:
        game_count += 1
        question_number = random_number()
        print(f'Question: {question_number}')
        user_answer = prompt.string("Your answer: ")
        correct_answer = is_even(question_number)
        if user_answer.lower() != correct_answer:
            result = (f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.\n"
                      f"Let's try again, {user_name}!")
            print(result)
            game_score = 0
            break
        else:
            result = 'Correct!'
            print(result)

    if game_score == 1:
        print(f'Congratulations, {user_name}!')


def main():
    brain_games_greet()
    global user_name
    user_name = get_user_name()
    welcome_user(user_name)
    brain_is_even()


if __name__ == '__main__':
    main()
