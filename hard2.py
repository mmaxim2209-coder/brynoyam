numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_number = int(input("Введите число: "))

if user_number in numbers:
    print(f"Число {user_number} найдено!")
if user_number not in numbers:
    numbers.append(user_number)
    print(f"Число {user_number} небыло найдено! Число {user_number} добавлено в список. Обновленный список: {numbers}")