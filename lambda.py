# lambda function is small anonymous function
# lambda written as lambda arguments : expression
x = lambda a: a + 8
print(x(20))

# any number of arguments
y = lambda b, c: b * c
print(y(11, 2))


# why lambda is used? lambda as anonymous function inside another function
def fuels(yourfuels):
    return lambda consumptions: consumptions * yourfuels


consumptionsbio = fuels(6500)
consumptionsdexlite = fuels(14900)
print(consumptionsbio(20))
print(consumptionsdexlite(20))

