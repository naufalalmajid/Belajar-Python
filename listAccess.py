# list access is like slicing in string, but different.
# in list we can access by number index, using square bracket

x = ["learn", "anything", "new", "before", 2024]
print(x[2])

# using negative indexing
# it is meaning indexing value last in list started with -1
print(x[-1])

# range indexes
# in range we can access the range value in list by separate with colon
print(x[1:3])

# range with negative indexing
# negative indexing it is mean last value in list started with -1 but range separate with colon
print(x[-4:-2])

# some special is we can using check if else use in keyword
if 2024 in x:
    print("yes, '2024' is included in list")
