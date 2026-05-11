# ✊📄✂️ Project 4: Rock Paper Scissors Game

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Level](https://img.shields.io/badge/Level-Beginner-green)

A simple terminal-based Rock Paper Scissors game built using Python.

This project helped me practice conditional statements, user input handling, lists, and Python's `random` module while creating an interactive game.

🔗 [View Full Code](https://github.com/YasarShaik/python_projects)

---

# 🧠 Topics Covered

This project introduces and reinforces several important Python concepts:

- `input()` function — taking user input
- Conditional statements (`if`, `elif`, `else`)
- Lists
- Random module
- String comparison
- ASCII art usage
- Program flow control
- Basic game logic

---

# 🚀 Why This Project Matters

This project was one of my first attempts at building an actual game using Python.

It helped me understand:
- how programs make decisions,
- how user choices affect outcomes,
- and how logic can be used to simulate real-world games.

It also introduced me to debugging and handling edge cases in user input.

---

# 🎮 How the Game Works

The user chooses:

- `0` → Rock
- `1` → Paper
- `2` → Scissors

The computer randomly selects one option.

The program then compares both choices and decides:
- whether the player wins,
- the computer wins,
- or the match ends in a draw.

---

# 🔄 Flow of the Program

## 1️⃣ Importing the Random Module

```python
import random
```

This allows the computer to randomly select Rock, Paper, or Scissors.

---

## 2️⃣ Creating ASCII Art

```python
rock = '''
'''
```

ASCII art was used to visually represent:
- Rock
- Paper
- Scissors

This made the terminal output more interactive and fun.

---

## 3️⃣ Creating the Sample Space

```python
SampleSpace = [rock, paper, scissors]
```

A list was created containing all three choices.

This allowed the computer to randomly select one option using:

```python
random.choice(SampleSpace)
```

---

## 4️⃣ Taking User Input

```python
playerch = input("Choose Rock(0) / Paper(1) / Scissors(2): ")
```

The program asks the user to choose between Rock, Paper, or Scissors.

The input is stored as a string.

---

## 5️⃣ Generating the Computer's Choice

```python
comp_ch = random.choice(SampleSpace)
```

The computer randomly selects one item from the sample space list.

---

## 6️⃣ Comparing Choices

```python
if playerch == '0':
```

Conditional statements were used to compare:
- the player's choice,
- and the computer's choice.

The program then determines the result according to the rules of Rock Paper Scissors.

---

# 🏆 Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

If both choices are the same:
- the game results in a draw.

---

# 🎯 Sample Output

## User Input

```text
Choose Rock(0) / Paper(1) / Scissors(2): 0
```

## Output

```text
Player chooses: rock

Computer chooses:
✂️ Scissors

Player Wins!
```

---

# ⚠️ Edge Cases Discovered

While testing the project, I realized that invalid inputs like:

```text
5
hello
@
```

were incorrectly being treated as Scissors because of the final `else` statement.

This helped me understand the importance of proper input validation.

---

# 📈 Future Improvements

Possible improvements that can be added later:

- Score tracking system
- Multiple rounds
- Replay option
- Better input validation
- GUI version using Tkinter or Pygame
- Multiplayer mode
- Cleaner logic using integers instead of ASCII comparisons

---

# 📅 Project Update

### Updated on: 11 May 2026

Learned about:
- debugging logic errors,
- edge case testing,
- cleaner conditional handling,
- and improving user input validation.

---

# 💡 Final Thoughts

This project helped me move from writing simple scripts to building interactive logic-based applications.

Even though the game is small, it introduced me to:
- decision making in programming,
- debugging,
- randomization,
- and structuring larger blocks of logic.

One small game, but a huge learning step in my Python journey 🚀
