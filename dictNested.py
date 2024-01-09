# a dictionary can contain dictionaries, it is called with nested dictionaries
myCar = {
    "dailyCar": {"brands": "Toyota", "type": "Land Cruiser", "year": 2020},
    "favoriteCar": {"brands": "Ford", "type": "Ranger Raptor XLT", "year": 2022},
    "specialCar": {"brands": "Ford", "type": "Mustang Dark Horse", "year": 2023},
    "familyCar": {"brands": "Toyota", "type": "Alphard 2.5 Hybrid", "year": 2023},
}
print(myCar)


# or we can add some dictionaries into one dictionary
premium1 = {"brands": "Lamborghini", "type": "Urus"}
premium2 = {"brands": "Nissan", "type": "GT-R"}

premiumCar = {"premium1": premium1, "premium2": premium2}
print(premiumCar)

# for accessing items in nested dictionary we can using name of dictionaries
print(myCar["familyCar"]["type"])
