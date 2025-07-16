import pickle

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (comma separated): ").split(',')
    ingredients = [i.strip() for i in ingredients]
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }
    return recipe

filename = input("Enter the name of the binary file to store recipes: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except Exception:
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    print(f"\nEntering recipe {i+1}:")
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

with open(filename, "wb") as file:
    pickle.dump(data, file)

print(f"Recipes saved to {filename}.")
