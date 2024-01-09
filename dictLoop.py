# we can loop through the dictionary by using for loop
# in loop we can return the key but we can return values
myCar = {
    "brands": "Ford",
    "model": "Ranger Raptor",
    "year": 2022,
    "color": "Meteor Grey",
    "engine": "Diesel",
    "type": "XLT 2.0 L",
}

# using loop for printing all keys in the dictionary
for my in myCar:
    print(my)

# we can using loop for print all values in the dictionary
for me in myCar:
    print(myCar[me])

# we can using values() method for printing all values in the dictionary
for i in myCar.values():
    print(i)

# or using keys() method for printing all keys in the dictionary
for j in myCar.keys():
    print(j)

# for both printing all keys and values in the dictionary we can using items() method
for alma, car in myCar.items():
    print(alma, car)
