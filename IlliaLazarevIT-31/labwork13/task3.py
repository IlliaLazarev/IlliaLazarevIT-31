import math
import sys
from pathlib import Path
from datetime import datetime
import shutil

NAME = "Illia Lazarev"
GROUP = "IT-31"

BASE_DIR = Path(__file__).parent

print(f"{NAME}, {GROUP}")

# Перевірка аргументів
args = sys.argv[1:]

if len(args) == 1 and args[0] == "--help":
    print("usage: python task3.py [--dry-run] <dir>")
    sys.exit(0)

dry_run = False

if args and args[0] == "--dry-run":
    dry_run = True
    args = args[1:]

if len(args) != 1:
    print("usage: python task3.py [--dry-run] <dir>")
    sys.exit(2)

directory = Path(args[0])

if not directory.exists() or not directory.is_dir():
    print(f"Error: {directory} is not a directory",
          file=sys.stderr)
    sys.exit(1)

# Отримуємо лише звичайні файли з каталогу
files = sorted(
    [path for path in directory.iterdir() if path.is_file()],
    key=lambda path: path.stat().st_mtime
)

if not files:
    print("No files found")
    sys.exit(0)

# Формування плану переміщення
plan = []

for file_path in files:
    stat = file_path.stat()

    modification_date = datetime.fromtimestamp(stat.st_mtime)

    folder_name = modification_date.strftime("%Y-%m")

    destination_folder = directory / folder_name
    destination_file = destination_folder / file_path.name

    size = stat.st_size

    # Визначення одиниці розміру через math.log
    if size == 0:
        unit_index = 0
    else:
        unit_index = min(
            int(math.log(size, 1024)),
            3
        )

    units = ["B", "KB", "MB", "GB"]

    readable_size = size / (1024 ** unit_index)

    plan.append((
        file_path,
        destination_folder,
        destination_file,
        modification_date,
        readable_size,
        units[unit_index]
    ))

# Виведення плану
for item in plan:
    source, folder, destination, modified, size, unit = item

    print(
        f"{source.name:20} "
        f"{size:8.1f} {unit:2} "
        f"{modified:%d.%m.%Y %H:%M} "
        f" -> {folder.name}/"
    )
    folder_count = len(set(item[1] for item in plan))

if dry_run:
    print(
        f"\n{len(plan)} files, {folder_count} folders "
        "(dry run, nothing moved)"
    )
    sys.exit(0)

# Перевірка всіх конфліктів до переміщення
for item in plan:
    destination = item[2]

    if destination.exists():
        print(
            f"Error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

# Переміщення файлів
for item in plan:
    source, folder, destination, *_ = item

    folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))

# Створення звіту
report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

now = datetime.now()

report_name = now.strftime("organize_%Y%m%d_%H%M.txt")
report_path = report_dir / report_name

with report_path.open("w", encoding="utf-8") as report:
    report.write(f"{NAME}, {GROUP}\n")
    report.write(f"Date: {now}\n")
    report.write(f"Files moved: {len(plan)}\n\n")

    for item in plan:
        report.write(
            f"{item[0].name} -> {item[1].name}/\n"
        )

print(f"\n{len(plan)} files, {folder_count} folders")
print(f"Report saved to: {report_path}")