# modules is like code library
# create a module, with name imports.py
"""
def car(diesel):
    print("Ford " + diesel)
"""

# use a module
import imports

imports.car("Ranger Raptor XLT")
# when we import function from a module, use the sintax modulename.function name

# variables in module, module can contain all tyoes (dictionaries, list, etc) so we update file imports.py to like this"""
"""
def car(diesel):
    print("Ford " + name)

toyota = {"type":"Hilux DCab 4x4","engine":"diesel","manufactured":"japan"}    
"""
x = imports.toyota["type"]
print(x)

# naming a module, we can renaming a module whatever we want but we must have file extension
# re-naming a module, we can create alias when import by using as keyword
import imports as inx

yzx = inx.toyota["manufactured"]
print(yzx)

# built-in modules
import platform

y = platform.machine()
print(y)


# using the dir() function

# import from modules, we can
