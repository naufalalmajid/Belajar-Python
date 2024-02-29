# RegEx is Regular Exspression is sequence of characters that forms a search pattern
# we can use RegEx module by called re built-in package in python
import re

daily = "alma always trying better than yesterday"
find = re.search("better", daily)

if find:
    print("alma always trying to be better everyday")
else:
    print("alma always same with yesterday")

# the findall() function
findTrying = re.findall("trying", daily)
print(findTrying)

# the search() function
findAlma = re.search("alma", daily)
print(findAlma)
