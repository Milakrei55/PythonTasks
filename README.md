# Python for Web Developers – Student Exercises

This repository contains the exercises and deliverables for the Python for Web Developers specialization. It documents my learning and progress through each exercise.

---

## Exercise 1.1 – Intro to Python Programming

### Overview

This first exercise focuses on setting up the development environment and creating a simple Python script. It also introduces virtual environments and Python’s package management using pip.

### Tools & Technologies

- Python 3.13.4
- Virtual Environments (via `venv`)
- Visual Studio Code
- IPython
- pip

### Steps Completed

1. **Installed Python 3.13.4**  
   Confirmed using `python3 --version`.

2. **Created a virtual environment**  
   Created one called `cf-python-base` and activated it.

3. **Wrote and ran a Python script `add.py`**  
   A simple script that prompts the user for two integers, adds them, and prints the result.

4. **Installed and tested IPython**  
   IPython was installed and launched inside the virtual environment for enhanced shell features.

5. **Exported environment dependencies**  
   Used `pip freeze > requirements.txt` to list the installed packages.

6. **Created a second environment `cf-python-copy`**  
   Installed packages listed in `requirements.txt` to verify environment cloning.

7. **Documented the setup and learning**  
   Added all necessary files to a folder named `Exercise1-1`.

---

## Exercise 1.2 – Recipe App Data Structures

### Overview

This exercise introduced Python data structures by building a basic storage format for a Recipe app. Each recipe was modeled as a dictionary and added to a list representing a collection of recipes.

### Data Structure Choices

- Each **recipe** was stored as a `dict` with keys: `"name"`, `"cooking_time"`, and `"ingredients"`.
- All recipes were collected in a `list` called `all_recipes`, which allows ordered access and easy modification.

### Steps Completed

1. Created `recipe_1` for Tea using a dictionary.
2. Initialized a list `all_recipes` and added `recipe_1`.
3. Created `recipe_2` to `recipe_5` with custom data.
4. Appended all new recipes to the list.
5. Printed the ingredients for each recipe from the list using `print()`.

---

### Deliverables (in `Exercise1-2/` folder)

- `step1.png` to `step6.png`: Screenshots of the recipe creation process.
- `README.md`: This file.
- `LearningJournal.md`: Reflections and notes about this exercise.

---

### What I Learned

- How to use Python dictionaries to store structured data.
- How to use lists to manage multiple objects.
- How to access nested data using indexing and keys.
## Exercise 1.3 – Recipe App with Difficulty Ratings

### Overview

This exercise builds on the earlier recipe structure and introduces dynamic user input via functions and loops. The script prompts the user to enter any number of recipes, tracks all unique ingredients, and calculates each recipe’s difficulty level based on its cooking time and number of ingredients.

### Steps Completed

1. Created `Exercise_1.3.py` and defined two lists: `recipes_list` and `ingredients_list`.
2. Built a `take_recipe()` function to take user input and return a recipe dictionary.
3. Collected multiple recipes in a loop, ensuring ingredients were only added once.
4. Used control flow to determine difficulty levels (Easy, Medium, Intermediate, Hard).
5. Printed all recipes with their info and difficulty.
6. Displayed all ingredients in alphabetical order.
7. Captured terminal screenshots of each step and saved them appropriately.

---

### Deliverables (in `Exercise1-3/` folder)

- `Exercise_1.3.py`
- `Step1.png` through final step screenshot
- Updated `LearningJournal.md`

## Exercise 1.4 – Recipe App with File Storage and Search

### Overview

This exercise focused on persistent storage using the `pickle` module. It introduced a two-script system:

- `recipe_input.py`: Collects recipes from the user and writes them to a binary file.
- `recipe_search.py`: Reads the binary file and lets the user search recipes by ingredient.

### Steps Completed

**recipe_input.py**
- Defined a `take_recipe()` function to gather recipe data.
- Used `calc_difficulty()` to assign a difficulty level.
- Used a try/except/else/finally block to load existing data or initialize new data.
- Appended new recipes and ingredients, avoiding duplicates.
- Saved the updated data structure into a binary file.

**recipe_search.py**
- Loaded the binary file using `pickle`.
- Used `enumerate()` to list ingredients by index.
- Allowed user to select an ingredient and view matching recipes.
- Displayed recipe details using a helper function.

---

### Deliverables (in `Exercise1-4/` folder)

- `recipe_input.py`
- `recipe_search.py`
- Generated binary file (e.g., `my_recipes.bin`)
- Screenshots labeled `Part 1 Step 1`, `Part 2 Step 1`, etc.
- Updated `LearningJournal.md`
