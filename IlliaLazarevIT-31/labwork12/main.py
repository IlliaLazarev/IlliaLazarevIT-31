from pathlib import Path
import lazarev_files

directory = Path(file).parent

print("=== РОБОТА З ФАЙЛАМИ ===")

print("\n1. Список файлів:")
files = lazarev_files.list_files(directory)

for file in files:
    print("-", file)

print("\n2. Пошук файлів зі словом 'lazarev':")
found_files = lazarev_files.find_files(
    directory,
    "lazarev"
)

if found_files:
    for file in found_files:
        print("-", file)
else:
    print("Файлів не знайдено.")

print("\n3. Створення особистого файлу:")

personal_text = (
    "Ім'я: Ілля\n"
    "Прізвище: Лазарев\n"
    "Група: IT-31\n"
)

new_file = lazarev_files.create_file(
    directory / "personal_info.txt",
    personal_text
)

print(f"Файл успішно створено: {new_file.name}")
