# we can adding some value in list
# append items, using append() it is mean adding items in last index in list
x = ["alma", "selalu", "rajin"]
x.append("belajar")
print(x)

# insert items, using insert() it is mean adding items in specific index in list
y = ["jangan", "bosan", "belajar", "ya", "alma"]
y.insert(1, "pernah")
print(y)

# extend items, using extend() it is mean adding another list to some list likes merge some list
a = ["alma", "selalu", "rajin", "belajar"]
b = ["jangan", "pernah", "bosan", "belajar", "ya", "alma"]
a.extend(b)
print(a)

# add any iterable, by using extend() not only list we can adding any iterable objects (lists, tuples, strings, dictionaries, sets)
xlist = ["meskipun", "lelah", "jangan", "berhenti"]
ytuples = ("ingat", "sebab", "yang", "membuatmu", "terus", "berjalan")
xlist.extend(ytuples)
print(xlist)

