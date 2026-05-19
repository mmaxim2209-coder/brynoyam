text = "Python is great!"
wow = text.split(" ")
oldgrandwow = tuple(wow)
newgrandwow = text.replace("great", "awesome")
print(newgrandwow)
print(oldgrandwow[-1])