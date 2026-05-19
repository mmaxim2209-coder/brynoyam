numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
washnumbers = list(set(numbers))
washnumbers.sort()
washnumbers.extend([18, 36, 40])
washnumbers.insert(2, 0)
print(washnumbers)
print(f"Длина списка: {len(washnumbers)}")