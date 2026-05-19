import json
book = {"title": "Python", "price": 500, "year": 2023}
with open("book.json", "w") as file:
    json.dump(book, file)
with open("book.json", "r") as file:
    data = json.load(file)
    
    old_price = data["price"]
    new_price = old_price * 1.1
    data["price"] = int(new_price)  
    # чтоб ноля небыло

with open("book_updated.json", "w") as file:
    json.dump(data, file)