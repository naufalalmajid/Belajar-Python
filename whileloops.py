# in python we have two primitive loop commands, while and for
# the while loop, is we can execute a set of statements as long as condition is true
x = 5
while x < 25:
    print(x)
    x += 5
# when using while remember the increment value for loop, if not loop will continue forever, and we need define indexing variable

# break statement used for stop loop if while condition is true
y = 1
while y < 9:
    print(y)
    if y == 7:
        break
    y += 2

# continue statement used for stop the current iteration, and continue with the next
z = 2
while z < 10:
    z += 2
    if z >= 4 and z <= 6:
        continue
    print(z)

# else statement used for when code condition no longer true
yxz = 3
while yxz < 11:
    print(yxz)
    yxz += 3
else:
    ("counting was stopped at 9")
