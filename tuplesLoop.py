# we can loop tuple by using for loop
x = ("tidak ada", "badai", "yang", "tak usai")
for i in x:
    print(i)

# loop by index number using range() and len() keywords
for a in range(len(x)):
    print(x[a])

# using while loop
y = 0
while y < len(x):
    print(x[y])
    y = y + 1
