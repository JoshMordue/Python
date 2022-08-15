# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}
#
# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {"Sheep", "Hen", "Cow", "Horse", "Goat"}
wild_animals = {"Lion", "Elephant", "Tiger", "Goat", "Panther", "Horse"}
potential_rides = {"Donkey", "Horse", "Camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)
