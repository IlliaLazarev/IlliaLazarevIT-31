import math
import sys
import csv
from pathlib import Path
from datetime import date, datetime, timedelta

NAME = "Illia Lazarev"
GROUP = "IT-31"

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data" / "expenses.csv"

print(f"{NAME}, {GROUP}")

# Перевірка файлу
if not FILE_PATH.exists():
    print("Error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)

expenses = {}

# Читання CSV
with FILE_PATH.open("r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row or row[0].strip().startswith("#"):
            continue

        try:
            if len(row) != 4:
                raise ValueError("Invalid number of fields")

            expense_date = date.fromisoformat(row[0].strip())
            amount = float(row[2].strip())

            if amount < 0:
                raise ValueError("Negative amount")

            expenses[expense_date] = (
                expenses.get(expense_date, 0.0) + amount
            )

        except (ValueError, IndexError) as error:
            print(f"Warning: invalid row {row}: {error}",
                  file=sys.stderr)

if not expenses:
    print("No valid expenses found", file=sys.stderr)
    sys.exit(1)

# Період
first_date = min(expenses)
last_date = max(expenses)

period_days = (last_date - first_date).days + 1

print(
    f"\nperiod: {first_date:%d.%m.%Y} "
    f"({first_date:%A}) - "
    f"{last_date:%d.%m.%Y} "
    f"({last_date:%A}), {period_days} days"
)

# Витрати за кожним днем
weekday_totals = [0.0] * 7
daily_values = []

current_date = first_date

while current_date <= last_date:
    amount = expenses.get(current_date, 0.0)
    weekday_totals[current_date.weekday()] += amount
    daily_values.append(amount)
    
    current_date += timedelta(days=1)

print("\nweekday      total")

weekdays = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

for i in range(7):
    print(f"{weekdays[i]:12} {weekday_totals[i]:.2f}")

# Загальна сума
total = math.fsum(daily_values)

average = total / period_days

# Стандартне відхилення
variance = math.fsum(
    (value - average) ** 2 for value in daily_values
) / period_days

std_deviation = math.sqrt(variance)

# Найбільші витрати
top_date = max(expenses, key=expenses.get)

# Дні без витрат
no_spend_days = sum(
    1 for value in daily_values if value == 0
)

print(f"\ntotal: {total:.2f}")
print(f"per day: {average:.2f} +- {std_deviation:.2f}")

print(
    f"top day: {top_date:%d.%m.%Y} "
    f"({top_date:%A}), {expenses[top_date]:.2f}"
)

print(f"no-spend days: {no_spend_days}")

# Кількість днів у місяці
month_start = last_date.replace(day=1)

if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)

days_in_month = (next_month - month_start).days

days_left = (next_month - last_date).days - 1

forecast = average * days_in_month

print(f"days in month: {days_in_month}")
print(f"days left after {last_date:%d.%m}: {days_left}")
print(f"month forecast: {forecast:.2f}")

# Перевірка грудня та високосного року
test_dates = [
    date(2026, 12, 15),
    date(2028, 2, 10)
]

print("\nMonth length tests:")

for test_date in test_dates:
    start = test_date.replace(day=1)

    if test_date.month == 12:
        end = date(test_date.year + 1, 1, 1)
    else:
        end = date(test_date.year, test_date.month + 1, 1)

    print(f"{test_date}: {(end - start).days} days");