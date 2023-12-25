# so after adding list, we can remove it, in this file we will learning how to remove element in list
# remove by using remove() element to removes some specific items in list, but if in the list more than one it will just removed first only
x = [
    "optimist",
    "learning",
    "consistency",
    "humble",
    "don't sleep",
    "coffee",
    "chill",
    "play",
]
x.remove("don't sleep")
print(x)

# remove some specific item in list by using pop() with number value of index we want removes
x.pop(5)
print(x)

# if we not fill any value it will ber remove last item in list
x.pop()
print(x)

# using del keywords we can remove specific item by index number
del x[4]
print(x)

# we can clear all items in lists using clear() keywords
x.clear()
print(x)

# or we can completely delete list by using del keywords

del x

