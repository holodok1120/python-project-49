from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question() -> int:
    return randint(0, 100)


def get_correct_answer(question: int) -> str:

    def is_prime(number: int) -> bool:
        if number in (0, 1):
            return False
        if number in (2, 3):
            return True
        for i in range(2, (number // 2 + 1)):
            if number % i == 0:
                return False
        return True
    
    return 'yes' if is_prime(question) else 'no'
