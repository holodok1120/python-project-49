from brain_games.engine import game_engine
from brain_games.games import prime


def main():
    game_engine(
        rules=prime.RULES,
        get_question=prime.get_question,
        get_correct_answer=prime.get_correct_answer
    )


if __name__ == '__main__':
    main()
