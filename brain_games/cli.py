import prompt


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    return user_name


def welcome_user(user_name):
    print(f"Hello, {user_name}!")
