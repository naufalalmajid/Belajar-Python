# with inheritance allow us to define a class inherits all the methods and properties from another class
# parent class is the class being inherited from called as base class, and child class is the class inherits from another class


# it is parent class
class Car:
    def __init__(self, carname, series) -> None:
        self.carname = carname
        self.series = series

    def mycar(self):
        print(self.carname, self.series)


mycar1 = Car("Ford", "Ranger Raptor XLT")
mycar2 = Car("Toyota", "Alphard Hybrid 2.5")
mycar3 = Car("Mitsubishi", "Outlander")

mycar3.mycar()


# it is child class
class DailyCar(Car):
    pass


dailycar1 = DailyCar("Toyota", "Hilux Dcab 4x4")
dailycar1.mycar()


# we can add the __init__() function to the child class, the __init__() function called automatically
# __init__() function overrides the inheritance of the parents __init__() function
class Race:
    def __init__(racer, type, engine):
        racer.type = type
        racer.engine = engine

    def myRacer(racer):
        print(racer.type, racer.engine)


class myrace(Race):
    def __init__(racer, type, engine):
        Race.__init__(racer, type, engine)


race1 = myrace("Nissan GTR R34", "Gasoline")
race1.myRacer()


# use the super() function, for inherit all methods and properties from parents class
class mydayrace(Race):
    def __init__(racer, type, engine):
        super().__init__(type, engine)


mydayrace1 = myrace("Toyota 86", "Gasoline")
mydayrace1.myRacer()


# add properties
class mydayraces(Race):
    def __init__(racer, type, engine, year):
        super().__init__(type, engine)
        racer.year = year


races1 = mydayraces("Toyota 86", "Gasoline", "2023")
races1.myRacer()


# add methods
class mydayracing(Race):
    def __init__(racer, type, engine, years):
        super().__init__(type, engine)
        racer.years = years

    def printracing(racer):
        print(
            "my favorite race car is: ",
            racer.type,
            "with engine ",
            racer.engine,
            "manufactured at ",
            racer.years,
        )


mydayracing1 = mydayracing("Toyota 86", "Gasoline", 2023)
mydayracing1.printracing()
