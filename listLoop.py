# we can loop any list items using for loop
life = [
    "optimist",
    "learning",
    "consistency",
    "humble",
]
for x in life:
    print(x)

# loop through the lists by index number using range() and len() functions
for i in range(len(life)):
    print(life[1])

# using while loop, we can using len() for length of the list
y = 0
while y < len(life):
    print(life[y])
    y = y + 1

# looping use list comprehension, more shortest sintax for looping
[print(z) for z in life]

