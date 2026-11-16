import csv
import sys
from pathlib import Path
from collections import defaultdict
from decimal import Decimal
from tabulate import tabulate

NAME = "Illia Lazarev"
GROUP = "IT-31"

print(f"{NAME}, {GROUP}")

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "expenses.csv"

if not CSV_FILE.exists():
    print("Error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)

# Зберігаємо кількість записів і суму за категоріями
categories = defaultdict(lambda: {
    "count": 0,
    "total": Decimal("0.00")
})

# Загальна сума та кількість витрат
total_amount = Decimal("0.00")
total_count = 0

# Читаємо CSV
with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row:
            continue

        # Пропускаємо коментарі
        if row[0].strip().startswith("#"):
            continue

        try:
            if len(row) != 4:
                raise ValueError("Invalid number of columns")

            category = row[1].strip()
            amount = Decimal(row[2].strip())

            if not category or amount < 0:
                raise ValueError("Invalid category or amount")

            categories[category]["count"] += 1
            categories[category]["total"] += amount

            total_count += 1
            total_amount += amount

        except (ValueError, ArithmeticError) as error:
            print(f"Warning: skipped row {row}: {error}",
                  file=sys.stderr)

if total_count == 0:
    print("No valid expenses found")
    sys.exit(1)

# Формуємо таблицю
table = []

for category, values in sorted(categories.items()):
    table.append([
        category,
        values["count"],
        f"{values['total']:.2f}"
    ])

# Загальний підсумок
table.append([
    "TOTAL",
    total_count,
    f"{total_amount:.2f}"
])

# Виведення таблиці
print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github"
))