import json

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if filename.endswith('.json'):
                content = json.load(file)
            else:
                content = file.read()
        print(content)
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет доступа к файлу.")

read_file("unknown.txt")  # Выведет: Файл не найден.
read_file("book.json")