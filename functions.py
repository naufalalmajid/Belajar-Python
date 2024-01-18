# function is block of code which only run when it is called
# we can create function by using def
def my_car():
    print("My favorite is Ford Ranger Raptor XLT")


# calling function
my_car()


# we can arguments the function
def my_toyota(mytoyota):
    print("Toyota " + mytoyota)


my_toyota("Land Cruiser")
my_toyota("GR 86")
my_toyota("Hilux GR")


# parameters or arguments, parameter is used inside parentheses in function definition but argument is used when function called
# we can make fuction with 2 arguments or more
def my_suv(brands, type):
    print(brands + " " + type)


my_suv("Toyota", "Land Cruiser")
my_suv("Mitsubishi", "Outlander")


# arbitrary arguments, in case we dont know how much the arguments we can using * in parameter like *args
def my_daily(*cars):
    print("My daily car is " + cars[1])


my_daily("Ford Ranger Raptor XLT", "Toyota Hilux GR", "Misubishi Outlander")


# keywords arguments, we can send arguments by using key = value sintax
def my_family_cars(cars1, cars2, cars3, cars4):
    print("My family car is " + cars1)


my_family_cars(
    cars1="Toyota Land Cruiser",
    cars2="Mitsubishi Outlander",
    cars3="Toyota Alphard 2.5 Hybrid",
    cars4="Lamborghini Urus",
)


# arbitrary keywords arguments, in case we dont know how much keyword arguments we can using two asterisk **
def my_special(**special):
    print("the car i like is " + special["toyota"])


my_special(toyota="Toyota GR 86", nissan="Nissan GTR R34")


# default parameter value, used when we call the function without parameter value
def my_brands(carbrands="Toyota"):
    print("my car brand is" + carbrands)


my_brands()
my_brands("Mitsubishi")
my_brands("Ford")


# passing a list as an argument, we can send any data types to function
def my_carbrands(mycarbrands):
    for x in mycarbrands:
        print(x)


mycar = ["Toyota", "Ford", "Mitsubishi", "Isuzu"]
my_carbrands(mycar)
