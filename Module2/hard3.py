import os

filename = "Module2/tasks.txt"

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Купить продукты\nСделать уроки\nПозвонить другу\n")

with open(filename, "r", encoding="utf-8") as file:
    tasks = file.readlines()

print("Список задач:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task.strip()}")

while True:
    new_task = input("Введите новую задачу (или 'exit'): ")
    if new_task.lower() == 'exit':
        break
    tasks.append(new_task + "\n")

with open(filename, "w", encoding="utf-8") as file:
    file.writelines(tasks)
print("Файл обновлён!")