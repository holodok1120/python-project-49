from brain_games.engine import game_engine
from brain_games.games import calc


def main():
    game_engine(
        rules=calc.RULES,
        get_question=calc.get_question,
        get_correct_answer=calc.get_correct_answer
    )


if __name__ == '__main__':
    main()
