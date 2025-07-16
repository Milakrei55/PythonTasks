import pickle

def display_recipe(recipe):
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    ingredients = data.get("all_ingredients", [])
    if not ingredients:
        print("No ingredients found.")
        return

    print("\nAvailable ingredients:")
    for index, ingredient in enumerate(ingredients):
        print(f"{index}: {ingredient}")

    try:
        choice = int(input("\nPick an ingredient by number: "))
        ingredient_searched = ingredients[choice]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        found = False
        for recipe in data.get("recipes_list", []):
            if ingredient_searched in recipe.get("ingredients", []):
                display_recipe(recipe)
                found = True
        if not found:
            print("No recipes found with that ingredient.")

filename = input("Enter the binary file name with recipe data: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please make sure the file exists.")
except Exception as e:
    print("An error occurred while loading the file:", e)
else:
    search_ingredient(data)
