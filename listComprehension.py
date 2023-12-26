# by using comprehension in list, we can make new list based on an existing list using shorter syntax
# example without comprehension
x = ["optimist", "learning", "consistency", "humble"]
y = []

for a in x:
    if "i" in a:
        y.append(a)

print(y)

# by using comprehension, more simple (remember simple is better)
z = [b for b in x if "i" in b]
print(z)

