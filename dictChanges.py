# we can change dictionaries items by reffering key name
myCar = {"brands": "Ford", "model": "Ranger Raptor", "year": "2022"}
print(myCar)

# change items
myCar["year"] = 2023
print(myCar)

# or we can using update() method,  which it will be update items by argument (dictionary too) or an iterable object with key:values
myCar.update({"model": "Ranger Raptor XLT"})
print(myCar)
