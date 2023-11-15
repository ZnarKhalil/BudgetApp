# Budget App

## Overview
This repository is a solution for the [FreeCodeCamp Scientific Computing with Python - Budget App](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app) problem.
The Budget App is a simple command-line application that allows users to create and manage budget categories. Users can deposit money into categories, withdraw funds, transfer money between categories, and view their spending through a percentage-based chart.

## Files

- **main.py:** This file serves as the main entry point for the Budget App. It demonstrates the functionality of the `Category` class and the `create_spend_chart` function. It also runs unit tests using the `unittest` module.

- **budget.py:** Contains the implementation of the `Category` class, which represents a budget category. It includes methods for depositing, withdrawing, transferring funds, checking balances, and generating a string representation of the category. Additionally, it defines the `create_spend_chart` function to create a percentage-based spending chart for multiple categories.

- **test_module.py:** This file contains unit tests for the methods implemented in the `Category` class and the `create_spend_chart` function.

## How to Use

1. **Run the Budget App:**
   - Execute the `main.py` file to see an example of using the Budget App. It demonstrates creating categories, making deposits and withdrawals, transferring funds between categories, and generating a spending chart.

2. **Testing:**
   - The `test_module.py` file includes unit tests for the functionality of the `Category` class and the `create_spend_chart` function. Run the tests using the command `python test_module.py`.

## Project Structure

- **Category Class:**
  - The `Category` class encapsulates the budget category functionality. Users can interact with instances of this class to manage their budget.

- **create_spend_chart Function:**
  - The `create_spend_chart` function takes a list of `Category` instances and generates a percentage-based spending chart.

- **Unit Tests:**
  - The `test_module.py` file includes unit tests to ensure the correctness of the implemented methods and functions.

## Example Usage

```python
# Creating and interacting with budget categories
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.transfer(50, clothing)

# Printing category information
print(food)

# Generating a spending chart
categories = [food, clothing, auto]
print(create_spend_chart(categories))
```

## Dependencies
The project does not have external dependencies beyond the Python standard library.