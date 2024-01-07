# in dict we can access items by reffering to key name, inside square brackets
myCar = {"brands": "Ford", "model": "Ranger Raptor", "year": "2022"}
whatsmyCar = myCar["model"]
print(whatsmyCar)

# or by using get() methods will give same result
modelmyCar = myCar.get("model")
print(modelmyCar)

# by using keys() it will be return a list of all the keys in the dictionary
itsmyCar = myCar.keys()
print(itsmyCar)

# make new updates in dict
myCar["color"] = "Red"
print(itsmyCar)

# we can using values() it will be return a list of all the values in the dictionary
favoritemyCar = myCar.values()
print(favoritemyCar)

#  make new updates in dict
myCar["engine"] = "2.0 L"
print(favoritemyCar)

# we can using items() for return a list of all key and values in the dictionary
justmyCar = myCar.items()
print(justmyCar)

# and we can check if some key available in dictionary
if "engine" in myCar:
    print("Yes, myCar have engine")
