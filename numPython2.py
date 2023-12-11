# integer, unlimited positive or negative without decimal
x = 222222222222222222
y = -99999999999999999
z = 28

print(type(x))
print(type(y))
print(type(z))

# float, unlimited values positive or negative but decimal
a = 28.0
b = 2222222222.2222222
c = -222222222.2222222

print(type(a))
print(type(b))
print(type(c))

# for float, we can use e or E as exponential power of ten

d = 28e3 # meaning 28 x 1000
e = 28000

# lets chech what e is power of ten 
if d == e:
    print(True)

# complex, for any complex values

j = 5j
k = 3 + 6j
l = 5 + j

print(type(j))
print(type(k))
print(type(l))
