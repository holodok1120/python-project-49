from brain_games.engine import game_engine
from brain_games.games import gcd


def main():
    game_engine(
        rules=gcd.RULES,
        get_question=gcd.get_question,
        get_correct_answer=gcd.get_correct_answer
    )


if __name__ == '__main__':
    main()
