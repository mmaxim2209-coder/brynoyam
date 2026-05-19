def greet(name):
    result = "Привет, " + name + "! Рад тебя видеть!"
    return result

name = input("Введите ваше имя: ")
greeting = greet(name)
print(greeting)
