# we can sort any list
# sorting by alphanumerically, sort() only will ascending sorting
x = ["optimist", "learning", "consistency", "humble"]
x.sort()
print(x)

y = [2, 2222, 28, 555, 8888]
y.sort()
print(y)

# if we want sorting by descending using reverse = True argument
x.sort(reverse=True)
print(x)

y.sort(reverse=True)
print(y)


# customize sort function using key = function, so in this function we want sort by value closer to 22
def myfunc(a):
    return abs(a - 22)


y.sort(key=myfunc)
print(y)

# if we use sort() function it will sorting case sensitive and make capital letters first before lower case
xy = ["Optimistic", "patient", "humble", "Learning"]
xy.sort()
print(xy)

# make case insensitive sort by using key function
xyz = ["Optimistic", "patient", "humble", "Learning"]
xyz.sort(key=str.lower)
print(xyz)

# reverse order
z = ["Optimist", "learning", "Consistency", "humble"]
z.reverse()
print(z)
