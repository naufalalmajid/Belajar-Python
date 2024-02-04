# python dates, we can use date object by import datetime
import datetime

x = datetime.datetime.now()
print(x)

# date output
print(x.year)
print(x.strftime("%j"))

# creating date objects
y = datetime.datetime(2024, 1, 1)
print(y)

# the strftime() method
print(y.strftime("%a"))
