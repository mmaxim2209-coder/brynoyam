student = {"name": "Alice", "age": 20, "city": "Moscow"}
student["grades"] = [5, 4, 3, 5, 4]
del student["age"]
setgrades = set(student["grades"])
print(student.keys())
print(setgrades)