# Learning Journal

Python for Web Developers Specialization

---

## 1.1 Exercise Summary

This first exercise focuses on setting up a Python development environment, learning how to manage packages and environments using pip and venv, and writing a simple script. It is an introduction for the rest of the course - building a command-line Recipe App.

---

## What I Did

* Installed Python 3.13.4 on macOS.
* Created and activated a virtual environment called `cf-python-base`.
* Wrote a simple script (`add.py`) to prompt the user for two numbers and print their sum.
* Installed and tested IPython inside the virtual environment.
* Exported installed packages to a `requirements.txt` file.
* Created a new environment (`cf-python-copy`) and installed dependencies from the requirements file to simulate environment replication.
* Organized and documented all steps, screenshots, and files in the `Exercise-1.1` folder.

---

## 1.2 Exercise Summary

This exercise focused on using Python’s built-in data types to structure recipe data for the Recipe app. The goal was to model each recipe with a dictionary and store them sequentially in a list. I worked in the IPython shell to build and test each step interactively.

---

## What I Did

* Created a dictionary `recipe_1` to store the name, cooking time, and list of ingredients for Tea.
* Initialized a list called `all_recipes` and added `recipe_1`.
* Created four more recipes (`recipe_2` to `recipe_5`) using the same structure.
* Appended them all to `all_recipes` using `extend()`.
* Printed each recipe’s ingredient list using dictionary key access.
* Took screenshots of each step from inside the IPython shell.

---

## What I Learned

* How to use dictionaries to store structured data with multiple data types.
* The value of using lists to hold and modify collections of items.
* The difference between printing and returning values in IPython.
* How to build nested data structures and access values efficiently.

---

## Tools & Technologies Used

* Python 3.13.4
* IPython Shell
* Dictionary & List data structures
* Visual Studio Code
* Git + GitHub

---

## Reflection

This task made me think carefully about how data is structured and accessed in Python. It reinforced my understanding of mutable vs immutable types and the benefits of using dictionaries for clarity and flexibility. By experimenting in the IPython shell, I got real-time feedback, which made it easier to troubleshoot and understand what I was doing.

## Working in small chunks using interactive prompts felt efficient and confidence-building — a great lead-in to designing larger parts of the Recipe app later in the course.

## 1.3 Exercise Summary

This exercise focused on combining data collection, conditionals, loops, and functions to build a more dynamic version of the Recipe app.

---

## What I Did

* Created a new script called `Exercise_1.3.py`.
* Initialized two empty lists: `recipes_list` and `ingredients_list`.
* Defined a function `take_recipe()` that takes recipe details from the user and returns a dictionary with `name`, `cooking_time`, and `ingredients`.
* Used a `for` loop to prompt the user to enter multiple recipes and ensure that unique ingredients were tracked.
* Added another `for` loop that iterates through each recipe to determine its difficulty level using control flow.
* Printed each recipe’s details and its calculated difficulty level.
* Displayed the final list of unique ingredients in alphabetical order.
* Took terminal screenshots for each step and organized them for upload.

---

## What I Learned

* How to collect structured user input using a function and return values.
* The role of conditionals (`if/elif/else`) in branching logic.
* How to use nested loops to handle related collections.
* Methods to ensure uniqueness in lists and how to alphabetically sort output.
* Importance of writing clean and reusable code using functions.

---

## Tools & Technologies Used

* Python 3.13.4
* Visual Studio Code
* IPython Shell
* Git + GitHub

---

## Reflection

This task felt like a major step forward in integrating everything I’ve learned so far. Writing a function to handle input and using multiple loops gave the script structure and flexibility. I appreciated how control flow was used to define difficulty ratings—it added a small but meaningful feature that made the app feel smarter.

Creating the script and testing it in the console helped build fluency and confidence. Organizing and presenting results clearly will also be useful when building more complex applications.

---

## 1.4 Exercise Summary

This exercise introduced file storage and retrieval using Python’s `pickle` module. The task was split into two scripts:

* `recipe_input.py` – collects recipes from the user, calculates their difficulty, and stores them in a binary file.
* `recipe_search.py` – loads stored recipes and lets the user search for recipes containing a specific ingredient.

---

## What I Did

* Defined a function `calc_difficulty()` to calculate difficulty based on cooking time and number of ingredients.
* Created a `take_recipe()` function to collect input from the user and return a structured dictionary.
* Handled file loading/saving using `pickle`, including proper error handling with `try/except/else/finally`.
* Added logic to preserve previously entered recipes across multiple script runs.
* Implemented a second script to let users search by ingredient using `enumerate()` and error-checked input.
* Captured screenshots for both recipe entry and search flow.

---

## What I Learned

* How to use the `pickle` module to read/write binary files.
* The importance of file handling and exception management.
* How to persist and retrieve complex Python objects between sessions.
* More advanced input validation using `try/except` and index checking.
* Practical applications of list scanning and conditionals to search data.

---

## Tools & Technologies Used

* Python 3.13.4
* Visual Studio Code
* IPython Shell
* Pickle module
* Git + GitHub

---

## Reflection

This exercise reinforced how useful file storage is in real-world applications. Being able to save and load recipe data across sessions made the app feel much more complete. I especially found the use of `try/except` for user input and file access helpful in making the program more robust. This was a big step in turning the recipe tracker into a functional tool.

---

## 1.5 Exercise Summary

This exercise introduced **object-oriented programming (OOP)** in Python and applied it to the Recipe app. Instead of storing recipes as dictionaries, I created a `Recipe` class with attributes and methods for handling recipe data more efficiently. This made the app more structured, modular, and reusable.

---

### What I Did

* Created a `recipe_oop.py` script.
* Defined a `Recipe` class with attributes: `name`, `ingredients`, `cooking_time`, and `difficulty`.
* Implemented class methods for:

  * Adding ingredients (`add_ingredients`).
  * Calculating difficulty based on rules combining cooking time and ingredient count.
  * Searching for ingredients in a recipe.
  * Tracking all unique ingredients across recipes with a class variable.
* Added `__str__` and `__repr__` methods for better readability.
* Created objects for Tea, Coffee, Cake, and Banana Smoothie, displayed them, and stored them in a list.
* Implemented a `recipe_search()` method to find recipes containing Water, Sugar, and Bananas.
* Took terminal screenshots and uploaded the script and results to GitHub.

---

### What I Learned

* How to design and use classes in Python effectively.
* Importance of encapsulation, reusability, and modular design in OOP.
* Practical use of methods like getters/setters, class variables, and operator overloading (`__str__`).
* Benefits of replacing procedural data structures (dictionaries) with objects.

---

### Tools & Technologies Used

* Python 3.13.4
* Visual Studio Code
* Git + GitHub

---

### Reflection

This task made OOP click for me — recipes felt like real "objects" rather than just data blobs. Designing the methods gave me a sense of control and made the code cleaner and more extensible. It was satisfying to see how the logic for calculating difficulty and searching for ingredients became part of the class itself.

---

## 1.6 Exercise Summary

This exercise integrated the Recipe app with **MySQL** using the `mysql.connector` package. Instead of storing recipes in files or objects only, I built a persistent backend with a structured database. The app supported full CRUD functionality: create, read (search), update, and delete.

---

### What I Did

* Wrote `recipe_mysql.py` and connected it to a MySQL server.
* Created a database `task_database` and a `Recipes` table with columns for id, name, ingredients, cooking\_time, and difficulty.
* Converted ingredient lists to comma-separated strings for storage.
* Built a menu-driven CLI with options to:

  * Add a recipe (with auto-calculated difficulty).
  * Search recipes by ingredient using SQL `LIKE`.
  * Update recipes (including auto-recalculating difficulty).
  * Delete recipes by ID.
* Ensured robust looping with `while` to return to the main menu until the user exits.
* Created, searched, updated, and deleted recipes successfully, documenting each step with screenshots.
* Uploaded code, screenshots, and notes to GitHub.

---

### What I Learned

* How to connect Python scripts to MySQL databases.
* How to structure SQL tables to match Python class models.
* CRUD operations in SQL and how to integrate them with Python.
* The trade-off between arrays in Python vs. comma-separated strings in relational DBs.
* Importance of input validation and error handling in database-driven apps.

---

### Tools & Technologies Used

* Python 3.13.4
* MySQL Server
* `mysql.connector` package
* Visual Studio Code
* Git + GitHub

---

### Reflection

This task gave me a strong foundation in combining Python with SQL. Seeing recipes persist in a database felt like a big step toward "real" applications. While writing SQL queries manually was a good challenge, I realized it could get verbose and error-prone, which made me curious about more Pythonic approaches (like ORMs).

---

## 1.7 Exercise Summary

This final exercise wrapped up Achievement 1 by using **SQLAlchemy ORM** to rebuild the Recipe app with cleaner, more Pythonic database handling. The ORM abstracted SQL syntax, making database operations easier and safer. This was the capstone step in building a full-featured Recipe app.

---

### What I Did

* Wrote `recipe_app.py` using SQLAlchemy to connect to MySQL.
* Defined a `Recipe` model class with attributes and methods:

  * Columns for id, name, ingredients, cooking\_time, difficulty.
  * Methods for difficulty calculation and returning ingredients as lists.
  * `__repr__` and `__str__` for formatted display.
* Created the `final_recipes` table via `Base.metadata.create_all()`.
* Implemented main menu functions:

  * `create_recipe()` – collects inputs, creates entries, commits them.
  * `view_all_recipes()` – displays all recipes with formatting.
  * `search_by_ingredients()` – allows multi-ingredient filtering.
  * `edit_recipe()` – lets users update fields and auto-recalculate difficulty.
  * `delete_recipe()` – deletes selected entries.
* Built a main menu loop with options for all CRUD actions plus quit.
* Tested thoroughly by adding, viewing, searching, editing, and deleting recipes.
* Took screenshots of terminal runs and uploaded everything to GitHub.

---

### What I Learned

* How to use SQLAlchemy ORM to simplify database interactions.
* How models in Python map to relational database tables.
* Benefits of abstraction: cleaner code, less error-prone than raw SQL.
* How to design a user-friendly CLI with full CRUD operations.
* Confidence in connecting Python, MySQL, and ORM patterns.

---

### Tools & Technologies Used

* Python 3.13.4
* MySQL Server
* SQLAlchemy ORM
* Visual Studio Code
* Git + GitHub

---

### Reflection

This was a satisfying conclusion to the first Achievement. By the end, I had a fully functional Recipe app that combined Python, OOP, databases, and ORMs into one project. It felt like a professional application, not just a classroom script. I now see how each step (data types → functions → files → OOP → SQL → ORM) built logically toward this point.