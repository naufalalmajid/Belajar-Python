# polymorphism refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# function polymorphism, example is len() function
x = "Mitsubishi"
print(len(x))

myToyota = ("Hilux Dcab 4x4", "Alphard Hybrid 2.5", "Toyota GT 86")
print(len(myToyota))

myHilux = {"brands": "Toyota", "series": "Hilux DCab", "engine": "Diesel"}

print(len(myHilux))


# class polymorphism, in class polymorphism often used so we can have multiple class with same methode name
class Toyota:
    def __init__(self, series, engine):
        self.series = series
        self.engine = engine

    def product(self):
        print("Japan")


class Mitsubishi:
    def __init__(self, series, engine):
        self.series = series
        self.engine = engine

    def product(self):
        print("Japan")


class Ford:
    def __init__(self, series, engine):
        self.series = series
        self.engine = engine

    def product(self):
        print("US")


Toyota1 = Toyota("Alphard Hybrid 2.5", "Hybrid")
Mitsubishi1 = Mitsubishi("Outlander PHEV", "Hybrid")
Ford1 = Ford("Ranger Raptor XLT", "Diesel")

for yxz in (Toyota1, Mitsubishi1, Ford1):
    print(yxz.series, yxz.engine)
    yxz.product()


# inheritance class polymorphism
class Car:
    def __init__(self, type, years):
        self.type = type
        self.years = years

    def manufactured(self):
        print("Japan")


class myToyota(Car):
    pass


class myFord(Car):
    def manufactured(self):
        print("US")


class myVolvo(Car):
    def manufactured(self):
        print("Sweden")


myToyota1 = myToyota("Hilux DCab 4x4", 2023)
myFord1 = myFord("Ranger Raptor XLT", 2022)
myVolvo1 = myVolvo("XC90 Recharge", 2024)

for myCars in (myToyota1, myFord1, myVolvo1):
    print(myCars.type)
    print(myCars.years)
    myCars.manufactured()
