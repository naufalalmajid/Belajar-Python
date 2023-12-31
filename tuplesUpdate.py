# tuples are unchangeable, but we can change values by convert tuple into list and convert it back to tuple
x = ("alma", "selalu", "bersemangat", "meskipun", 2023, "hampir", "selesai")
y = list(x)
y[5] = "sudah"
x = tuple(y)
print(x)
print(type(x))

# add some items
# by converting to list and convert it back to tuple
a = ("hidup", "selalu", "berjalan", "jadi", "pastikan", "berjalan", "dengan", "baik")
b = list(a)
b.append("ingat")
a = tuple(b)
print(a)

# by adding tuple to a tuple
m = ("ingat",)
n = ("tidak", "ada", "badai", "yang", "tak", "usai")
m += n
print(m)

# remove items in tuple, by converting to list and convert it back to tuple
xz = ("alma", "selalu", "bersemangat", "meskipun", 2023, "sudah", "selesai")
xy = list(xz)
xy.remove("sudah")
xz = tuple(xy)
print(xz)

# removing tuple using del
xyz = ("menjelang", "tahun", 2024)
del xyz

