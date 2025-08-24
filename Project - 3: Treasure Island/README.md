# Project - 3: Treasure Island

## 🧠 Topics Covered

This game blends several core Python concepts into a fun, immersive experience:

- **Multiline strings with `r'''...'''`**: Used to display ASCII art.
- **`print()` and `input()` functions**: For user interaction and narrative flow.
- **Variables**: Like `name`, `opt1`, `opt2`, and `opt3` to store user choices.
- **Conditional statements (`if`, `elif`, `else`)**: To control the story’s branching paths.
- **String comparison and logic**: Case-insensitive checks for user input.
- **✅ f-strings**: For dynamic storytelling with personalized messages.



## 🚀 How This Helps in Your Python Journey

This project is a **level-up** moment. Here’s why:

- You’re not just writing code—you’re **designing an experience**.
- You learn how to **structure branching logic**, which is essential in games, chatbots, and decision engines.
- You practice **user input validation** and **string handling**, which are key in real-world applications.
- You explore **ASCII art integration**, adding visual flair to your console output.
- You use **f-strings** to personalize the game, making it feel alive and responsive.

This kind of project builds your confidence and creativity, and it’s perfect for showcasing on GitHub or in a portfolio.



## 🔄 Flow of the Code

Here’s how the game unfolds:

### 1. Intro with ASCII Art  

```python
   print(r'''...''')
```
- Displays a treasure-themed ASCII banner. The r before the string ensures that backslashes are treated literally.

### 2. Welcome and Setup

```python
print("Welcome to Treasure Island.")
name = input("Enter your name: ")
```
- Greets the player and captures their name for personalized storytelling.

### 3. Story Begins
- The player is cast as a decoder in Captain Jack Sparrow’s crew. The narrative sets the stakes and immerses the player.

### 4. First Decision: Left or Right
```python
   opt1 = input("...left or right?")
if opt1 == "right":
    # Game over
else:
    # Continue
```
- A classic branching path. Choosing wrong leads to _alligators_ and a _game over_.

### 5. Second Decision: Wait or Swim

```python
opt2 = input("...wait or swim?")
if opt2 == "swim":
    # Game over
else:
    # Continue
```
- Another decision point with consequences. Waiting is the safe choice.

### 6. Final Decision: Red, Yellow, or Blue Tunnel

```python
opt3 = input("...Red | Yellow | Blue?")
if opt3.lower() == "red":
    # Fire trap
elif opt3.lower() == "blue":
    # Monsters
elif opt3.lower() == "yellow":
    # Victory!
else:
    # Invalid input
```
- The `.lower()` method could be used to simplify case-insensitive checks. Yellow leads to treasure and a celebratory ASCII trophy.

### 7. Victory Message with ASCII Art
```python
print(r'''...''')
print("Here's your prize for your work! \n[ WINNER! ]")
```
- A visual reward for making the right choices.
# 
## 🧩 Example Playthrough
If the user chooses:
- `left` → `wait` → `yellow`
They’ll see:
```text
Captain: Great job champion! I'll let you have a third of the quarter of this treasure...
[ WINNER! ]
```


### Total walkthrough and final result of the game 👇
```text
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
Enter your name: Alex

You are a member of Captain Jack Sparrow's crew, and the Captain is in desperate 
need of the treasure located near a secret island and you have been appointed 
incharge for leading the crew to treasure.
But the map is encoded and You are the decoder of the map! You reach an island and now lead their way.

Captain: Where do we go next Alex, take me to the treasure!
There is a cross-way in front, should you go 'left' or 'right'? left

Captain: Great job Alex!
Now let's swim across this river!
Choose whether to 'wait' for the tide to go down or 'swim' across the river right now! wait
Captain: Hay Ho crew!! We have a loong way to go, come on pack up your bags. 
Let's get into this cave and get back with our treasure!
.
.
.
.
Now where do we go Alex?
This place has three ways ahead!!
The three ways ahead are differentiated with the help of the light coming through them - | Red | Yellow | Blue |? yellow
Captain: Great job champion! I'll let you have a third of the quarter of this treasure for your commendable work!

*********************************************************
|                  (_v_)                                |
|                   _|_                                 |
|                   | |                                 |
|              |-----+-----|          ,%%%.             |
|              |    1ST    |          % 1 %             |
|              |   PRIZE   |          `%%%'             |
|               '---------'            ( (              |
|                \       /             )  )             |
|                 '.   .'             (   (             |
|                   | |                )'  )            |
|                  .' '.              (/ \/             |
|                 _|___|_                               |
|                [#######]                              |
|                                                       |
*********************************************************            
Here's your prize for your work! 
[ WINNER! ]

Process finished with exit code 0
```

## 💡 Ideas to Expand
- Add **score tracking** or **inventory items**.
- Use **functions** to modularize each decision.
- Add **random events** or **timed challenges**.
- Create a **GUI version** with `tkinter` or `pygame`.
