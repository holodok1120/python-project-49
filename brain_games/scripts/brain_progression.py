from brain_games.engine import game_engine
from brain_games.games import progression


def main():
    game_engine(
        rules=progression.RULES,
        get_question=progression.get_question,
        get_correct_answer=progression.get_correct_answer
    )


if __name__ == '__main__':
    main()
