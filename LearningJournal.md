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