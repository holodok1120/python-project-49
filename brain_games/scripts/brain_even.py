from brain_games.engine import game_engine
from brain_games.games import even


def main():
    game_engine(
        rules=even.RULES,
        get_question=even.get_question,
        get_correct_answer=even.get_correct_answer
    )


if __name__ == '__main__':
    main()
