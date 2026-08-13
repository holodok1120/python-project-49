### Hexlet tests and linter status:
[![Actions Status](https://github.com/holodok1120/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/holodok1120/python-project-49/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=holodok1120_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=holodok1120_python-project-49)

## Requirements:

[Python 3.12 +] - (https://www.python.org/downloads/)

[UV 0.9.4] - (https://astral.sh)
***

## Installation:

``` 
git clone git@github.com:holodok1120/python-project-49.git
```

```
cd python-project-49
```

```
uv build
```

```
uv tool install dist/*.whl
```

***
[![asciicast](https://asciinema.org/a/x9Gilh32rtuYSTs2.svg)](https://asciinema.org/a/x9Gilh32rtuYSTs2)

## How to play

This project includes five math brain games. In each game, the computer asks you a question, and you need to give the correct answer. To win, you must answer **three questions correctly in a row**. One wrong answer ends the game – you lose.

The five games are:

1. **Even Check** – determine if a number is even or odd.
2. **Calculator** – calculate the result of a simple arithmetic expression (e.g., `5 + 3`).
3. **Greatest Common Divisor (GCD)** – find the greatest common divisor of two numbers.
4. **Arithmetic Progression** – find the missing number in a progression.
5. **Prime Number** – decide if a number is prime or not.

Run any game with the corresponding command:

- `brain-even`
- `brain-calc`
- `brain-gcd`
- `brain-progression`
- `brain-prime`

### Game 1: Even Check
***
**Rules:** Answer `yes` if the number is even, otherwise answer `no`.

Examples:
- Question: `15` → Answer: `no`
- Question: `42` → Answer: `yes`

Demo:

[![asciicast](https://asciinema.org/a/A5nsXwsUmq0lvl62.svg)](https://asciinema.org/a/A5nsXwsUmq0lvl62)

### Game 2: Calculator
***
**Rules:** What is the result of the expression?

Examples:
- Question: `4 * 10` → Answer: `40`

Demo:

[![asciicast](https://asciinema.org/a/IBq1ZADwzLPde3lq.svg)](https://asciinema.org/a/IBq1ZADwzLPde3lq)

### Game 3: Greatest Common Divisor (GCD)
***
**Rules:** Find the greatest common divisor of given numbers.

Examples:
- Question: `86 66` → Answer: `2`

Demo:

[![asciicast](https://asciinema.org/a/61b8uCWPgBEj5G7J.svg)](https://asciinema.org/a/61b8uCWPgBEj5G7J)

### Game 4: Arithmetic Progression
***
**Rules:** What number is missing in the progression?

Examples:
- Question: `10 18 26 34 .. 50 58` → Answer: `42`

Demo:

[![asciicast](https://asciinema.org/a/58sykjmlN03TG6nK.svg)](https://asciinema.org/a/58sykjmlN03TG6nK)

### Game 5: Prime Number
***
**Rules:** Answer `yes` if given number is prime. Otherwise answer `no`.

Examples:
- Question: `47` → Answer: `yes`
- Question: `9` → Answer: `no`

Demo:

[![asciicast](https://asciinema.org/a/aYPxeKZqEIDFJLHe.svg)](https://asciinema.org/a/aYPxeKZqEIDFJLHe)

## Development and Testing
### Linting
Run ruff to check for linting issues:
```
make lint
```