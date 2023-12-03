#it is some variable which can used both inside and outside function
# it is some variable which can used both inside and outside function
# outside variable
x = "alma "

def myFunc():
    # inside variable
    x = "naufal"
    # inside variable call
    print(x + "rajin belajar")

myFunc()
# outside variable call
print(x + "rajin belajar")
