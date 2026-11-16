import math
import random
from pathlib import Path
from datetime import datetime

NAME = "Illia Lazarev"
GROUP = "IT-31"
YEAR = 2008

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "results"
HISTORY_FILE = RESULTS_DIR / "history.csv"

print(f"{NAME}, {GROUP}")

# Однакові завдання при кожному запуску
random.seed(YEAR)

# Генерація математичних прикладів
number1 = random.randint(4, 20)
number2 = random.randint(3, 6)

a = random.randint(20, 100)
b = random.randint(10, 100)

n = random.randint(5, 10)
k = random.randint(2, n - 1)

percent = random.choice([5, 10, 15, 20])
amount = random.choice([100, 200, 300, 400, 500])

questions = [
    (
        f"sqrt({number1 ** 2})",
        math.isqrt(number1 ** 2)
    ),
    (
        f"{number2}!",
        math.factorial(number2)
    ),
    (
        f"gcd({a}, {b})",
        math.gcd(a, b)
    ),
    (
        f"comb({n}, {k})",
        math.comb(n, k)
    ),
    (
        f"{percent}% of {amount}",
        percent * amount // 100
    )
]

score = 0

# Початок вимірювання часу
start_time = datetime.now()

# П'ять завдань
for index, (question, correct_answer) in enumerate(
    questions, start=1
):
    answer = input(f"{index}) {question} = ")

    try:
        user_answer = int(answer.strip())

        if user_answer == correct_answer:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct_answer}")

    except ValueError:
        print(f"   wrong, answer: {correct_answer}")

# Завершення вимірювання
end_time = datetime.now()

elapsed = (end_time - start_time).total_seconds()

print(f"\nscore: {score}/5, time: {elapsed:.1f} s")

# Створення папки results
RESULTS_DIR.mkdir(exist_ok=True)

# Перевірка існування історії
if not HISTORY_FILE.exists():
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        file.write("# datetime;score;seconds\n")
        # Додавання результату
attempt_time = datetime.now()

with HISTORY_FILE.open("a", encoding="utf-8") as file:
    file.write(
        f"{attempt_time:%Y-%m-%d %H:%M};"
        f"{score};{elapsed:.1f}\n"
    )

# Читання історії
attempts = []

with HISTORY_FILE.open("r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue

        parts = line.strip().split(";")

        if len(parts) != 3:
            continue

        try:
            attempt_date = datetime.strptime(
                parts[0],
                "%Y-%m-%d %H:%M"
            )

            attempt_score = int(parts[1])
            attempt_seconds = float(parts[2])

            attempts.append((
                attempt_date,
                attempt_score,
                attempt_seconds
            ))

        except ValueError:
            continue

# Пошук найкращого результату
best = max(
    attempts,
    key=lambda item: (item[1], -item[2])
)

print(f"\nattempts: {len(attempts)}")

print(
    f"best: {best[1]}/5 in "
    f"{best[2]:.1f} s "
    f"({best[0]:%Y-%m-%d %H:%M})"
)