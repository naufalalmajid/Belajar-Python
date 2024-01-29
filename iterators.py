# an iterator is an object that contain a countable number of values
# list, tuples, dictionaries and sets are all iterable object. all these object have a iter() method which is used to get an iterator:

myCar = ("BMW", "Isuzu", "Mitsubishi", "Toyota")
myIter = iter(myCar)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# even string are iterable object

myFord = "my Ford"
myIterator = iter(myFord)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# we can looping through an iterator by using for loop
myCarBrands = ("BMW", "Ford", "Isuzu", "Mitsubishi", "Toyota")
for brands in myCarBrands:
    print(brands)

# creating an iterator object, using __iter__()
