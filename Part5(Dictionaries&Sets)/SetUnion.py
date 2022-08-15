farm_animals = {"Sheep", "Hen", "Cow", "Horse", "Goat"}
wild_animals = {"Lion", "Elephant", "Tiger", "Goat", "Panther", "Horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)