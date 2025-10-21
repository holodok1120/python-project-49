import prompt

MAX_GAMES = 3


def check_answer(correct_answer: str, user_answer: str) -> bool:
    return correct_answer == user_answer.lower()


def game_engine(rules, user_name, get_question, get_correct_answer):
    print(rules)
    game_win = True
    game_count = 0
    while game_count < MAX_GAMES:
        game_count += 1
        question = get_question()
        correct_answer = get_correct_answer(question)
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if check_answer(correct_answer, user_answer):
            print('Correct!')
        else:
            result = (f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.\n"
                      f"Let's try again, {user_name}!")
            print(result)
            game_win = False
            break

    if game_win:
        print(f'Congratulations, {user_name}!')
