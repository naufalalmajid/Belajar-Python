# in sets we cannot change the items, but we can adding new items into the sets
# we can add items by using add() methods
x = {"belajar", "konsisten", "mulai", "sekarang"}
x.add("alma")
print(x)

# and we can add sets to anothe sets by using update() methode
y = {"kita", "lakukan"}
z = {"yang", "terbaik"}
y.update(z)
print(y)

# add any iterable by using update methode
xy = {"waktu", "berjalan"}
yz = ("seiring", "kehidupan")
xy.update(yz)
print(xy)
