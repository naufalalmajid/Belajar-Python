# we can slicing string with using index value separated with colon in square brackets

# started index with zero value, now we want slice from 1 to 5 (excluded)
x = "we make it"
print(x[1:5])

# slicing from the start (leaving out the start, write value start we just write end position index 2 is excluded)
print(x[:2])

# slicing to the end (just from choosen value index and to the end position index 2 to the end)
print(x[2:])

# negative indexing, used from slice from end
# we want print make it so we started from -7 for m and -3
print(x[-7:-3])

