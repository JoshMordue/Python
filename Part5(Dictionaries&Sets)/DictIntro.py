vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple', # replaces the original value
}


vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombadier Learjet 75"
vehicles["Toy"] = "Glider"


del vehicles["starfighter"]

result = vehicles.pop("f1", None)
print(result)

plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "Not present")
print(bike)
print()

# upgrading the virago
vehicles["virago"] = "Yamaha XV535"

# for i in vehicles:
#     print(i, vehicles[i],sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")


