# it is some variable which can used both inside and outside function
# it is some variable which can used both inside and outside function
# outside variable
x = "alma "


def myfunc():
    # inside variable
    x = "naufal"
    # inside variable call
    print(x + "rajin belajar")


myfunc()
# outside variable call
print(x + "rajin belajar")

# it is will replace with global variable
a = "al majid"
# global variable

def myfunc2():
    # global variable will make a variable can call everywhere
    global a
    a = "naufal al majid "
    print(a + "rajin belajar")


myfunc2()
print(a + "rajin belajar")
