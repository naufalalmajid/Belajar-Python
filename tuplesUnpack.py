# unpack, we can extract values in tuples to variables
# unpacking some tuples
x = ("tidak ada", "badai", "yang", "tak usai")
a, b, c, d = x
print(a)
print(b)
print(c)
print(d)

# unpacking using asterisk, using asterisk symbol (*) if variable less than tuples values
y = ("tidak ada", "badai", "yang", "tak usai")
k, l, *m = y
print(k)
print(l)
print(m)

# or another asterisk characteristic
z = ("tidak ada", "badai", "yang", "tak usai")
p, *q, r = z
print(p)
print(q)
print(r)
