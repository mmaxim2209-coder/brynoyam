with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("\nThis is a text file.") 
    # вроде так правильно работать с \n или нет?
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)