# in python we have python conditions and if statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# from conditions we can be used if statements by using if keyword, and notice the indentation for if statements
x = 222
y = 28
if x > y:
    print("x more than y")

# elif which it is used for "if the previous conditions were not true, the try this condition"
if x < y:
    print("x less than y")
elif x > y:
    print("x more than y")

# and else keyword catches anything which is not caugh by the preceding conditions
if x < y:
    print("x less than y")
elif x == y:
    print("x are equal with y")
else:
    print("x is more than y")

# short hand if is whe you only have one statement for execute, you can put in same line in if statement
if x > y:
    print("x more than y")

# short hand if else, is if you have only one statement to execute, one for it and one for else, we can put all into same line
print("x is bigger value") if x > y else ("y is bigger value")
# this technique called as ternary operators or conditional expressions
# and we can using multiple else statement like
print("X") if x > y else print("equal") if x == y else print("Y")

# and keyword is a logical operator, and used for combine conditional statements
a = 222
b = 555
c = 28
if a < b and b > c:
    print("both conditional is true")

# or keyword is a logical operator, and used for combine conditional statements
if a > b or b > c or a == c:
    print("at least one conditional are true")

# not keyword is a logical operator, and is used to reverse the conditional statements
if not a > b:
    print("a is not bigger than b")

# nested if, is we can put if statements inside if statement
if c < a:
    print("c less than a")
    if c < b:
        print("c less than b")
    else:
        print("c is bigger than b")

# pass statements, used whe we using if statements with no contents and using pass statements is using for avoid error
if b > a and b > c:
    pass
