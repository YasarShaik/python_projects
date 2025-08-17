# Project 1. Band Name Generator.

### This project is a simple code written using the very basic function of Python.
This code marks my first steps into Python

## 🧠 Topics Covered
This simple Python script introduces several foundational programming concepts:
- `print()` function: Used to display messages to the user.
- `input()` function: Captures user input from the keyboard.
- Variables: city and pet_name store the user's responses.
- String concatenation: Combines text and variables to form a custom output.

## 🚀 How This Helps in Your Python Journey
This code is a perfect starting point for beginners because it:
- Builds confidence in writing interactive programs.
- Demonstrates user interaction, which is key in real-world applications.
- Reinforces variable usage, helping you understand how data is stored and reused.
- Introduces basic string manipulation, a skill you'll use constantly in everything from data formatting to web development.
It’s playful, creative, and gives instant feedback—making learning feel more like a game than a grind.

## 🔄 Flow of the Code
Here’s how the program runs step-by-step:

#### 1. Greeting the user
```python
print("Welcome to the brand name generator.")
```
- This line welcomes the user and sets the tone for the program.

#### 2. Asking for the city
```python
city = input("What's the city you grew up in?\n")
```
- The program pauses and waits for the user to type in a city name. That input is stored in the variable `city`.

#### 3. Asking for the pet's name
```python
pet_name = input("\nWhat's your pet's name?\n")
```
- Similarly, this captures the pet's name and stores it in `pet_name`.

#### 4. Generating the brand name
```python
print("\n\nYour band name could be called - "+"'"+city+" "+ pet_name+"'")
```
- This line combines the two inputs into a fun, personalized band name and prints it out.
- This line used basic string concatenation to combine the two strings available in the variables `city` and `pet_name`, hence genrating a band name for the user.

## 🎸 Final Output Example

If the user enters:

- City: **Mumbai**
- Pet Name: **Whiskers**

The output will be:

```text
You band name could be called – 'Mumbai Whiskers'
```
- This happens as follows:
  * After taking inputs the variables are saved as -
    `city` = **Mumbai**
    `pet_name` = **Whiskers**
  * And then while printing the print function says - `"'"+city+" "+ pet_name+"'"` -> '`city` + `pet_name`' i.e. **'Mumbai Whiskers'**
