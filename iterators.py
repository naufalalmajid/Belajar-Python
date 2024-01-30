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

# creating an iterator object, by using __iter__() you can do operations (initializing etc.), but must always return the iterator object itself.
# __next__() method also allows you to do operations, and must return the next item in the sequence.


class myCounting:
    def __iter__(self):
        self.count = 2
        return self

    def __next__(self):
        counting = self.count
        self.count += 2
        return counting


myCount = myCounting()
myIters = iter(myCount)

print(next(myIters))
print(next(myIters))
print(next(myIters))
print(next(myIters))
print(next(myIters))

print("next counting")


# stopieration, to prevent the iteration from going on forever, we can using StopIteration statement.
class myCalc:
    def __iter__(self):
        self.calc = 2
        return self

    def __next__(self):
        if self.calc <= 28:
            y = self.calc
            self.calc += 2
            return y
        else:
            raise StopIteration


myCalculation = myCalc()
myCalcs = iter(myCalculation)

for yxz in myCalcs:
    print(yxz)
