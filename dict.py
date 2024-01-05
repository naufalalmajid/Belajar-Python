# dictionaries are data types which used for store data values in key:values pairs
# using curl brackets, separate keys and values using colon and using commas for separate keys
myCar = {"brands": "Ford", "model": "Ranger Raptor", "year": "2022"}
print(type(myCar), myCar)

# dictionary items are ordered, changeable and not allow duplicates value (duplicate values will be choose the last values)
print(myCar["model"])

# in python 3.6 and earlier dict is unordered but in python 3.7 is ordered
# and in dict we can contain items with any types of data
myGarage = {
    "brands": ["Toyota", "Ford", "Mitsubishi", "Isuzu", "Brabus"],
    "year": (2017, 2018, 2020, 2022, 2023),
    "favorite": "Ford Ranger Raptor",
}
print(len(myGarage), myGarage)

# dict() conmstructor, by using dict() we can make a dictionary
myFord = dict(type="Mustang", engine=5.0, series="Dark Horse")
print(type(myFord), myFord)
