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