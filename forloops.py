# for loops is used for iterating over a sequence (a list, a tuple, a dictionary, a set or a string)

# looping through a string, we can looping string
for a in "learning":
    print(a)

# the break statements, we can stop looping by using break
life = ["we", "make", "it", "play"]
for b in life:
    print(b)
    if b == "it":
        break

# in same case
for c in life:
    if c == "play":
        break
    print(c)

# the continue statements, we can stop the current iteration of the loop and continue with next
mission = ["learning", "dream", "consistency", "playing", "work hard"]
for d in mission:
    if d == "playing":
        continue
    print(d)


# the range() function, by using range() we can loop through code by specified number (default starting 0 by and incremets by 1)
for e in range(8):
    print(e)

print("-")

# we can make range() function by specified parameter
for f in range(1, 8):
    print(f)

print("-")

# or make range() specific increments
for g in range(1, 9, 2):
    print(g)

print("-")

# else in for loop, used for block code when the loop is finished
for h in range(3):
    print(h)
else:
    print("was stopped")

# when break used else will ignored
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("was stopped")

# nested loops, is loop inside another loop
x = ["still", "be"]
y = ["hopes", "wealth", "health", "humble", "learning", "family"]
for j in x:
    for k in y:
        print(j, k)


# the pass statements, for loops cannot empty so we can fill with pass for avoid getting an error
for x in range(3):
    pass
