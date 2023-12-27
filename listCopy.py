# list copy is used for copying some list, because we cannt use listx = listy because if listx changes the same things will be happen to listy
# so we can copy by using copy() keywords

x = ["hopes", "wealth", "health", "family", "life"]
y = x.copy()
print(x, y)

# or we can copy by using built in method list()
z = list(x)
print(z)
