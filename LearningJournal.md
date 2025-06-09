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

## What I Learned

- The importance of virtual environments for isolated and reproducible development.
- How to use pip for package installation and dependency management.
- How to export environment dependencies with `pip freeze` and restore them in another environment.
- How to write and execute basic Python scripts via the terminal.
- How to document a project clearly in a structured folder and `README.md`.

---

## Tools & Technologies Used

- Python 3.13.4
- venv
- pip
- IPython
- Visual Studio Code
- Git + GitHub

---

## My Goals for This Course

- Build a fully functional, professional-grade command-line Recipe App using Python.
- Gain hands-on experience with object-oriented programming.
- Learn to interact with MySQL databases using Python.
- Understand the structure and practices behind web frameworks like Django.
- Build a portfolio-ready version of the Recipe App in Django by the end of Achievement 2.

---

## Reflection

Starting from scratch helped solidify the setup and tools Python developers use daily. I learned how to freeze and replicate environments. This gave me confidence in maintaining consistency across different machines or collaborators in a project.

I also appreciated the clear connection this exercise made between development setup and long-term maintainability — it’s not just about writing code, but managing it responsibly from the beginning.

## Errors – and What I Learned

While working in IPython, I mistakenly tried to run a shell command (`pip freeze > requirements.txt`) and an exit command (`exit`) from within the IPython shell. This caused a syntax error because IPython, while more powerful than the basic Python shell, still follows Python syntax rules — it doesn’t interpret shell commands like a regular terminal does. In the future, I’ll be more mindful of which environment I am in, and avoid running shell commands inside Python REPLs.

```python
In [1]: print("Testing IPython")
In [1]: pip freeze > requirements.txt  # ← This line triggered a SyntaxError