# 🔐 Project 5: PyPassword Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Level](https://img.shields.io/badge/Level-Beginner-green)

A terminal-based password generator built using Python that creates randomized passwords using:
- letters,
- numbers,
- and symbols.

This project helped me understand randomness, list manipulation, loops, and how stronger passwords can be generated programmatically.

🔗 [Basic Version Code](./main.py)  
🔗 [Clean Version Code](./main_clean.py)

---

# 🧠 Topics Covered

This project helped reinforce several important Python concepts:

- Lists
- Loops
- User Input
- Random module
- `append()` method
- `random.choice()`
- `random.shuffle()`
- String joining using `"".join()`
- Basic password generation logic

---

# 🚀 Why This Project Matters

This project was one of my first practical utility-based Python applications.

Unlike small beginner scripts, this project creates something genuinely useful:
a randomized password generator.

It helped me understand:
- how randomness works in programming,
- how data can be stored dynamically inside lists,
- and how logic can be used to generate secure-looking passwords.

This project also introduced the idea of:
- improving code readability,
- code refactoring,
- and writing cleaner Python solutions.

---

# 🔄 Flow of the Program

## 1️⃣ Importing the Random Module

```python
import random
```

The `random` module was used to:
- randomly select characters,
- and later shuffle the final password.

---

## 2️⃣ Creating Character Lists

```python
letters = [...]
numbers = [...]
symbols = [...]
```

Three separate lists were created containing:
- alphabets,
- numbers,
- and symbols.

These lists act as the source pool for generating passwords.

---

## 3️⃣ Taking User Input

```python
nr_letters = int(input())
nr_symbols = int(input())
nr_numbers = int(input())
```

The user specifies:
- how many letters,
- how many symbols,
- and how many numbers

should be included in the password.

The inputs are converted into integers using `int()`.

---

## 4️⃣ Generating the Password

```python
password.append(random.choice(letters))
```

Using loops and `random.choice()`, random characters are selected from the lists and added into the `password` list.

This process repeats for:
- letters,
- symbols,
- and numbers.

---

# 🟢 Easy Method — Sequential Password

Initially, the password is generated in sequence:

```text
letters → symbols → numbers
```

Example:

```text
abCD!@123
```

This version works correctly but follows a predictable structure.

---

# 🔴 Hard Method — Shuffled Password

To improve randomness:

```python
random.shuffle(password)
```

was used.

This rearranges all characters randomly.

Example:

```text
3@Ca1!Db2
```

This version creates stronger and less predictable passwords.

---

# 🎯 Sample Output

## User Input

```text
How many letters would you like in your password?
5

How many symbols would you like?
2

How many numbers would you like?
3
```

## Output

```text
Easy Method:
eqaIZ!&841

Hard (shuffled):
I1&e4Z8!qa
```

---

# ⚠️ Problems Faced During Development

While building this project, several issues were encountered and solved:

- Attempting list assignment before initialization
- Index out of range errors
- Incorrect random ranges
- Repeated looping logic
- Understanding why lists need `.append()`
- Learning how `"".join()` converts lists into strings

These debugging steps helped strengthen my understanding of Python fundamentals.

---

# 📈 Future Improvements

Possible future upgrades for this project:

- Password strength checker
- Minimum security requirements
- GUI version using Tkinter
- Copy password to clipboard
- Save generated passwords securely
- Option for custom password length
- Avoid repeating characters

---

# 📅 Project Update

### Updated on: 12 May 2026

Learned about:
- list manipulation,
- randomness,
- shuffling algorithms,
- cleaner Python practices,
- and debugging logic errors.

---

# 💡 Final Thoughts

This project was an important step from writing simple beginner scripts to building utility-based applications.

It introduced concepts that are widely used in real-world software development:
- randomness,
- data handling,
- logic structuring,
- and cleaner code design.

A small project — but a huge step forward in my Python journey 🚀

