# in python we don't have arrays so we using python lists
# we can using lists as arrays, but however for work with arrays we need import library like numpy library
myCars = ["Toyota", "Ford", "Mitsubishi", "Isuzu"]

# access the elements of an array
x = myCars[1]
print(x)

# modify value of first arrays
myCars[0] = "Mazda"

# the length of array by using len() method
y = len(myCars)
print(y)

# looping array elements by using for in loop
for yxz in myCars:
    print(yxz)

# adding array elements by using append method()
myCars.append("Toyota")
print(myCars)

# removing array elements, by using pop() method
myCars.pop(3)
print(myCars)

# or removing by using remove() method
myCars.remove("Mazda")
print(myCars)
