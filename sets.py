# set is some data types in python, set is unordered, unchangeable and unindexed
# we can using set by using curly bracket {}
x = {"belajar", "konsisten", "mulai", "sekarang"}
print(type(x), x)

# and in sets we cannot have two items with same value, so duplicates value will be ignored
y = {"belajar", "konsisten", "mulai", "sekarang", "konsisten"}
print(y)

# in sets, True and 1 are the same value as are False and 0
z = {True, 1, False, 0}
print(z)

# getting length of sets by using len() keywords
print(len(x))

# in sets we can fill with any type data likes integer, string and boolean
xy = {"sedang", "menjalani", "2024", "dengan", "harapan", "yang", "baik", True}
print(xy)

# we can use set constructor to make a set, and use type() to checking type
xyz = set(("selalu", "ada", "yang", "baik"))
print(type(xyz), xyz)
