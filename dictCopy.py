# in case we want copying the dict we cann't using dictx = dicty because the changes made in dicty will be change dictx
# so we using copy() methods
myCar = {
    "brands": "Ford",
    "model": "Ranger Raptor",
    "year": 2022,
    "color": "Meteor Grey",
    "engine": "Diesel",
    "type": "XLT 2.0 L",
}

mydailyCar = myCar.copy()
print(mydailyCar)

# copy dict by using dict() method
myfavoriteCar = dict(myCar)
print(mydailyCar)
