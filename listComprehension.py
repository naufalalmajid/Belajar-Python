# by using comprehension in list, we can make new list based on an existing list using shorter syntax
# example without comprehension
x = ["optimist", "learning", "consistency", "humble"]
y = []

for a in x:
    if "i" in a:
        y.append(a)

print(x, y)

# by using comprehension, more simple (remember simple is better)
z = [b for b in x if "i" in b]
print(z)

# syntax using comprehension, newlist = [expression for item in iterable if condition == True]
# by condition, like filter only accept if the items valuate to True
simple = [h for h in x if h != "humble"]
print(simple)

# iterable, we can any iterable objects like (lists, tuples, strings, dictionaries, sets)
value = [i for i in range(10) if i <= 5]
print(value)

# expression, we can manipulate to new list
life = [j.upper() for j in x]
print(life)

# or we can set outcome whatever we like
mylife = ["optimist" for k in x]
print(mylife)

# another expression but with condition
thislife = [l if l != "learning" else "trying" for l in x]

print(thislife)
