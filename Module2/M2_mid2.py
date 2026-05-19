def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None

print(divide(10, 2))
(divide(5, 0))
# без принта чтоб нан не выводился