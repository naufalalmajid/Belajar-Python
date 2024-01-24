# python is oop languange, a class is like an object constructor or a blueprint for creating objects
# we can create class by using keyword class
class myFuels:
    diesel = 50


# create a objects named fuels
fuels = myFuels()
print("my diesel needed :", fuels.diesel)


# __init__ function to assign values to object properties
class myCars:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type


cars1 = myCars("Ford", "Ranger Raptor XLT")
print(cars1.brand)
print(cars1.type)

self parameter

# the __str__() function when the class object is represented as a string



# object methods

# modify objects properties

# delete object properties by using del keyword 

# delete object by using del keyword

# pass statements, by using pass for passing
