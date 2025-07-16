recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter ingredients (separated by commas): ").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    print(f"\nEntering recipe {i+1}:")
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

print("\n--- Recipes ---")
for recipe in recipes_list:
    name = recipe["name"]
    cooking_time = recipe["cooking_time"]
    ingredients = recipe["ingredients"]

    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print(f"\nRecipe: {name}")
    print(f"Cooking Time (min): {cooking_time}")
    print(f"Ingredients: {', '.join(ingredients)}")
    print(f"Difficulty: {difficulty}")

print("\n--- All Ingredients ---")
for ingredient in sorted(ingredients_list):
    print(ingredient)
