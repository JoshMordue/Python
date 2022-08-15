# farm_animals = {"Sheep", "Hen", "Cow", "Horse", "Goat"}
# wild_animals = {"Lion", "Elephant", "Tiger", "Goat", "Panther", "Horse"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

from PrescriptionData import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    # meds_to_watch |= interaction
    meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')