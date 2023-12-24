# list change it is mean changing the value of list
# use square brackets after the list name then value what we want change
x = ["after", "time", "passes", "everybody", "changes"]
x[3] = "everyone"
print(x)

# we can change range list value, but we use square brackets inside
x[1:3] = ["long", "time"]
print(x)

# in some case if we change list value more than value range, it will be added to the list as more value
x[1:2] = ["quite", "long"]
print(x)

# and if we change list value less than value range, it will be removed list
x[1:] = ["quite", "time"]
print(x)


# inserting values in list using insert() method

y = ["after", "quite", "long", "time", "everyone", "changes"]
y.insert(3, 2023)
print(y)
