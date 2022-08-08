from RecipeOptions import recipe

def my_deepcopy(d: dict) -> dict:
    end_copy = {}

    for entry in d:
        end_copy.update(d)
    return recipes_copy


recipes_copy = my_deepcopy(recipe)
recipes_copy["butter chicken"]["ginger"] = 300
print(recipes_copy["butter chicken"]["ginger"])
print(recipe["butter chicken"]["ginger"])