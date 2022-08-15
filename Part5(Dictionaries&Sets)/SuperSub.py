animals = {'Turtle', 'Horse', 'Robin', 'Python', 'Swallow', 'Hedgehog', 'Wren', 'Aardvark', 'Cat'}
birds = {'Robin', 'Swallow', 'Wren'}

print(f'Birds is a subset of animals: {birds.issubset(animals)}')
print(f'Animals is a superset of birds: {animals.issuperset(birds)}')
print()
print(f'Birds is a superset of animals: {birds.issuperset(animals)}')

print(birds <= animals)
print(birds < animals)

print("*" * 70)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print("*" * 70)

more_birds = {'Wren', 'Budgie', 'Swallow'}

print(garden_birds >= more_birds)
