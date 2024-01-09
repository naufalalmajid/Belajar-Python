# we can removing items in dictionary with several methods
# we can using pop() for removing item with specific key name
myCar = {
    "brands": "Ford",
    "model": "Ranger Raptor",
    "year": 2022,
    "color": "Meteor Grey",
    "engine": "Diesel",
    "type": "XLT 2.0 L",
}

myCar.pop("year")
print(myCar)

# or we can using popitem() for removing the last item inserted, but in version earlier than 3.7 random item will be removed
myCar.popitem()
print(myCar)

# another method is using del keyword following with key name
del myCar["engine"]
print(myCar)

# or we can using del withouth key name for removing the dictionary
# del myCar

# or we can using clear() keyword for removing all items in dictionary
myCar.clear()
print(myCar)
