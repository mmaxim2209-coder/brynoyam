def convert_temp(temp, unit):
    if unit == "C":
        result = (temp * 9/5) + 32
        return result
    if unit == "F":
        result = (temp - 32) * 5/9
        return result
    else:
        return "Ошибка! некорректная единица измерения"
input_temp = float(input("Введите температуру: "))
input_unit = input("Введите единицу измерения (C или F): ")

converted = convert_temp(input_temp, input_unit)

if converted == "Ошибка! некорректная единица измерения":
    print(converted)
else:
    print("Температура в эквиваленте:", converted)
