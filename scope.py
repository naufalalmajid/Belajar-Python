# scope is variable which only available in inside region it is created
# local scope
def myfuels():
    diesel = 6500
    print("harga", diesel)


myfuels()


# function inside function
def tank():
    fuelTank = 50

    def fuels():
        print("isi tank", fuelTank)

    fuels()


tank()

# global scope, is some variables in main body code
dexlite = 14500


def dex():
    print("harga dexlite", dexlite)


dex()
print(dexlite)


# naming variable, with same name variable local and global it will be different
def dexfuel():
    dexlite = 14850
    print(dexlite)


dexfuel()
print(dexlite)


# global keyword, by using global keyword we can make global variable
def cetanedexlite():
    global cetane
    cetane = 51


cetanedexlite()
print(cetane)

# we can update values variable by usung global keyword
cetanevalue = 51
print("cetane dasar:", cetanevalue)
print("update variable cetane")


def cetanex():
    global cetanevalue
    cetanevalue = 53


cetanex()
print("setelah pakai dex:", cetanevalue)
