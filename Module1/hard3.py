numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secret_number = 4
user_number = int(input("Угадай число от 1 до 10: "))
if user_number == secret_number:
    print("Ах****!, ты угадал!")
if user_number > secret_number:
    print("Бери меньше.")
if user_number < secret_number:
    print("Бери больше.")