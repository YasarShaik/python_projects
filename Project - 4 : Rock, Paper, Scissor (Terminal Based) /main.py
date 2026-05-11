import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

SampleSpace = [rock,paper,scissors]

playerch = input("Choose Rock(0) / Paper(1) / Scissors(2): ")
comp_ch = random.choice(SampleSpace)

if playerch == '0':
    print(f"Player chooses: rock",rock)
    print("computer chooses:")
    if comp_ch == rock:
        print(rock)
        print("Draw, Try Again!")
    elif comp_ch == paper:
        print(paper)
        print("Computer wins!")
    else:
        print(scissors)
        print("Player Wins!")

elif playerch == '1':
    print(f"Player chooses: paper", paper)
    print("computer chooses:")
    if comp_ch == rock:
        print(rock)
        print("Player Wins!")
    elif comp_ch == paper:
        print(paper)
        print("Draw, Try Again!")
    else:
        print(scissors)
        print("Computer wins!")

elif playerch == '2':
    print(f"Player chooses: scissors", scissors)
    print("computer chooses:")
    if comp_ch == rock:
        print(rock)
        print("Computer wins!")
    elif comp_ch == paper:
        print(paper)
        print("Player Wins!")
    else:
        print(scissors)
        print("Draw, Try Again!")

else:
    print("Invalid Input")
