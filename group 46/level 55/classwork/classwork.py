# 1-დავალება 

car = {
    "brand": "lamborghini",
    "model": "lamborghini urus",
    "year": 2018
}

for key, value in car.items():
    print(f"{key}: {value}")

print("Keys:", list(car.keys()))
print("Values:", list(car.values()))

# 2-დავალება

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


ertad_set = set1 | set2
print("გაერთიანება:", ertad_set)

gansxvaveba_set = set1 - set2
print(gansxvaveba_set)

msgavseba_set = set1 & set2
print("მსგავსებები:", msgavseba_set)

# 3-დავალება

car = {
    "brand": "lamborghini",
    "model": "lamborghini urus",
    "year": 2018
}

for value in car.values():
    print(value)