# list join is concatenate two or more list
# we can using + operator
x = ["hopes", "wealth", "health", "family", "life"]
y = ["education", "learning", "humble", "network"]
z = x + y
print(z)

# we can append all items from list a to list b
a = [2, 5, 8, 28, 2222, 8888]
b = [22, 222, 555, 888]
for i in b:
    a.append(i)
    a.sort()

print(a)

# we can extend list m with list n
m = ["play", "consistent", "try"]
n = ["teach", "share"]
m.extend(n)
print(m)
