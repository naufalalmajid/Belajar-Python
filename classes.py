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


# the __str__() function when the class object is represented as a string
class myDaily:
    def __init__(self, brand, series, year):
        self.brand = brand
        self.series = series
        self.year = year

    def __str__(self):
        return f"{self.brand},{self.series},{self.year}"


myDaily1 = myDaily("Ford", " Ranger Raptor XLT", 2022)
print(myDaily1)


# object methods, object can also contain methods
class myFamilyCar:
    def __init__(self, series, years):
        self.series = series
        self.years = years

    def myFam(self):
        print("my family car is: ", self.series)


myFamilyCar1 = myFamilyCar("Toyota Alphard Hybrid 2.5", 2023)
myFamilyCar2 = myFamilyCar("Toyota Land Cruiser", 2020)
myFamilyCar2.myFam()


# the self parameter, is reference to the current instance of the class and is used to access variables belongs to the class
# we can named whatever we like
class myFavCar:
    def __init__(myFav, name, serie, yearlaunch):
        myFav.name = name
        myFav.serie = serie
        myFav.yearlaunch = yearlaunch

    def myfavorite(car):
        print("my favorite car is: ", car.name)


car1 = myFavCar("Mustang Dark Horse", "Fastback", 2023)
car2 = myFavCar("Ford Ranger Raptor XLT", "Truck 4x4", 2022)
car3 = myFavCar("Lamborghini Urus", "SUV", 2023)
car3.myfavorite()

# modify objects properties
car1.series = "New Fastback 2024"

# delete object properties by using del keyword
del car1.yearlaunch

# delete object by using del keyword
del car1


# pass statements, by using pass for avoid getting an error if the class is empty
class myTrucks:
    pass
