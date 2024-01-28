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

# use the super() function

# add properties

# add methods

