# for removing some items in set we can using remove() or discard() methods
x = {"belajar", "konsisten", "mulai", "sekarang"}
x.remove("mulai")
print(x)
# if removed item does not exist it will be make error result

# using discard(), if items we want remove does not exist it not make error result
y = {"semua", "harus", "di mulai", "sekarang"}
y.discard("dari")
print(y)

# or we can remove by using pop() but it is random item will be deleted
z = y.pop()
# removed item
print(z)
# after removed
print(y)

# we can empties the sets by using clear() keyword
yz = {"don't", "give up"}
yz.clear()
print(yz)

# or we can deleted the sets by using del() keyword
xyz = {"don't", "give up"}
del xyz
