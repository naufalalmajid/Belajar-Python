# we can add new items in dictonary by using a new index key and assigning the values
myCar = {"brands": "Ford", "model": "Ranger Raptor", "year": "2022"}
print(myCar)

# adding new items
myCar["color"] = "Meteor Grey"

# or we can using update() method for adding some items into dictionary by argument (dictionary too) or an iterable object with key:values
myCar.update({"engine": "Diesel"})
print(myCar)
