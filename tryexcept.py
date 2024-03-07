# in python we will meet with try, except, else and finally block
# by using try block we can test a block of code for errors
# by using except block we can handle the error
try:
    print(myLandCruiser)
except NameError:
    print("you forget define variable myLandCruiser")
except:
    print("Something else went wrong")

# by using else block we can execute code when there is no error
try:
    print("now my Land Cruiser now in Garage")
except:
    print("Both Cars in maintenance")
else:
    print("ofc with my Ford Ranger")

# by using finally block we can execute code, regardless of the result of the try- and except blocks.
try:
    print(mySUV)
except:
    print("my SUV was used by my bro")
finally:
    print("my bro using my SUV")

# raise keyword is used to raise exception
diesel = 6500

if diesel < 7000:
    raise Exception("Sorry, diesel is too cheap")

