numbers = [12, 45, 78, 34, 56]

with open("data.txt", "w", encoding="utf-8") as file:
    for num in numbers:
        file.write(str(num) + "\n")

total_sum = 0

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        total_sum = total_sum + int(line)

with open("sum.txt", "w", encoding="utf-8") as file:
    file.write(f"Сумма чисел: {total_sum}")
    print(total_sum)