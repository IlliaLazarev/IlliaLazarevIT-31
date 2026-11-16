from pathlib import Path


def list_files(directory):
    path = Path(directory)

    if not path.is_dir():
        return []

    return [file.name for file in path.iterdir() if file.is_file()]


def find_files(directory, substring):
    files = list_files(directory)

    return [
        file for file in files
        if substring.lower() in file.lower()
    ]


def create_file(path, text):
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")

    return file_path


if __name__ == "__main__":
    print("Перевірка модуля lazarev_files.py")

    current_directory = Path(__file__).parent

    print("\nСписок файлів:")
    print(list_files(current_directory))

    print("\nПошук файлів зі словом 'main':")
    print(find_files(current_directory, "main"))

    print("\nСтворення тестового файлу:")
    created_file = create_file(
        current_directory / "test_file.txt",
        "Це тестовий файл для перевірки модуля."
    )
    print(f"Файл створено: {created_file.name}")