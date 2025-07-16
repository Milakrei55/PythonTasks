# Learning Journal
Python for Web Developers Specialization

---

## 1.1 Exercise Summary

This first exercise focuses on setting up a Python development environment, learning how to manage packages and environments using pip and venv, and writing a simple script. It is an introduction for the rest of the course - building a command-line Recipe App.

---

## What I Did

- Installed Python 3.13.4 on macOS.
- Created and activated a virtual environment called `cf-python-base`.
- Wrote a simple script (`add.py`) to prompt the user for two numbers and print their sum.
- Installed and tested IPython inside the virtual environment.
- Exported installed packages to a `requirements.txt` file.
- Created a new environment (`cf-python-copy`) and installed dependencies from the requirements file to simulate environment replication.
- Organized and documented all steps, screenshots, and files in the `Exercise-1.1` folder.

---

## 1.2 Exercise Summary

This exercise focused on using Python’s built-in data types to structure recipe data for the Recipe app. The goal was to model each recipe with a dictionary and store them sequentially in a list. I worked in the IPython shell to build and test each step interactively.

---

## What I Did

- Created a dictionary `recipe_1` to store the name, cooking time, and list of ingredients for Tea.
- Initialized a list called `all_recipes` and added `recipe_1`.
- Created four more recipes (`recipe_2` to `recipe_5`) using the same structure.
- Appended them all to `all_recipes` using `extend()`.
- Printed each recipe’s ingredient list using dictionary key access.
- Took screenshots of each step from inside the IPython shell.

---

## What I Learned

- How to use dictionaries to store structured data with multiple data types.
- The value of using lists to hold and modify collections of items.
- The difference between printing and returning values in IPython.
- How to build nested data structures and access values efficiently.

---

## Tools & Technologies Used

- Python 3.13.4
- IPython Shell
- Dictionary & List data structures
- Visual Studio Code
- Git + GitHub

---

## Reflection

This task made me think carefully about how data is structured and accessed in Python. It reinforced my understanding of mutable vs immutable types and the benefits of using dictionaries for clarity and flexibility. By experimenting in the IPython shell, I got real-time feedback, which made it easier to troubleshoot and understand what I was doing.

Working in small chunks using interactive prompts felt efficient and confidence-building — a great lead-in to designing larger parts of the Recipe app later in the course.
---

## 1.3 Exercise Summary

This exercise focused on combining data collection, conditionals, loops, and functions to build a more dynamic version of the Recipe app.

---

## What I Did

- Created a new script called `Exercise_1.3.py`.
- Initialized two empty lists: `recipes_list` and `ingredients_list`.
- Defined a function `take_recipe()` that takes recipe details from the user and returns a dictionary with `name`, `cooking_time`, and `ingredients`.
- Used a `for` loop to prompt the user to enter multiple recipes and ensure that unique ingredients were tracked.
- Added another `for` loop that iterates through each recipe to determine its difficulty level using control flow.
- Printed each recipe’s details and its calculated difficulty level.
- Displayed the final list of unique ingredients in alphabetical order.
- Took terminal screenshots for each step and organized them for upload.

---

## What I Learned

- How to collect structured user input using a function and return values.
- The role of conditionals (`if/elif/else`) in branching logic.
- How to use nested loops to handle related collections.
- Methods to ensure uniqueness in lists and how to alphabetically sort output.
- Importance of writing clean and reusable code using functions.

---

## Tools & Technologies Used

- Python 3.13.4
- Visual Studio Code
- IPython Shell
- Git + GitHub

---

## Reflection

This task felt like a major step forward in integrating everything I’ve learned so far. Writing a function to handle input and using multiple loops gave the script structure and flexibility. I appreciated how control flow was used to define difficulty ratings—it added a small but meaningful feature that made the app feel smarter.

Creating the script and testing it in the console helped build fluency and confidence. Organizing and presenting results clearly will also be useful when building more complex applications.

---

## 1.4 Exercise Summary

This exercise introduced file storage and retrieval using Python’s `pickle` module. The task was split into two scripts:

- `recipe_input.py` – collects recipes from the user, calculates their difficulty, and stores them in a binary file.
- `recipe_search.py` – loads stored recipes and lets the user search for recipes containing a specific ingredient.

---

## What I Did

- Defined a function `calc_difficulty()` to calculate difficulty based on cooking time and number of ingredients.
- Created a `take_recipe()` function to collect input from the user and return a structured dictionary.
- Handled file loading/saving using `pickle`, including proper error handling with `try/except/else/finally`.
- Added logic to preserve previously entered recipes across multiple script runs.
- Implemented a second script to let users search by ingredient using `enumerate()` and error-checked input.
- Captured screenshots for both recipe entry and search flow.

---

## What I Learned

- How to use the `pickle` module to read/write binary files.
- The importance of file handling and exception management.
- How to persist and retrieve complex Python objects between sessions.
- More advanced input validation using `try/except` and index checking.
- Practical applications of list scanning and conditionals to search data.

---

## Tools & Technologies Used

- Python 3.13.4
- Visual Studio Code
- IPython Shell
- Pickle module
- Git + GitHub

---

## Reflection

This exercise reinforced how useful file storage is in real-world applications. Being able to save and load recipe data across sessions made the app feel much more complete. I especially found the use of `try/except` for user input and file access helpful in making the program more robust. This was a big step in turning the recipe tracker into a functional tool.
