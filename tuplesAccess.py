# we can access tuples, by indexing number
# access in tuple is like access in list or string, we can do it with number index in square brackets (remember if index number started by 0)
x = ("alma", "selalu", "bersemangat", "meskipun", 2023, "hampir", "selesai")
print(x[0])

# negative indexing (last item in tuples started by -1, -2 etc.)
print(x[-5])

# range indexes, in range we can access the range value in list by separate with colon
print(x[1:3])


# range, negative indexing it is mean last value in list started with -1 but range separate with colon
print(x[-4:-2])

# some special is we can using check if else use in keyword
if 2024 in x:
    print("yes, '2023' is included in list")

print(x[5:7])
