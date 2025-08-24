print(r'''
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
name = input("Enter your name: ")

print("\nYou are a member of Captain Jack Sparrow's crew, and the Captain is in desperate \nneed of the treasure located near a secret island and you have been appointed \nincharge for leading the crew to treasure.\nBut the map is encoded and You are the decoder of the map! You reach an island and now lead their way.")
print(f"\nCaptain: Where do we go next {name}, take me to the treasure!")
opt1 = input("There is a cross-way in front, should you go 'left' or 'right'? ")

if opt1=="right":
    print(f"Captain: Hey youu {name}, what are these alligators doing here in this makeshift pond? \n ...Your crew was chased away by the alligators.\n[ GAME OVER! ]...")
else:
    print(f"\nCaptain: Great job {name}!\nNow let's swim across this river!")

    opt2 = input("Choose whether to 'wait' for the tide to go down or 'swim' across the river right now! ")

    if opt2=="swim":
        print("\n Your crew was swept away by the strong waves due to the high tides at this time of the day. GAME OVER!")
    else:

        print(f"Captain: Hay Ho crew!! We have a loong way to go, come on pack up your bags. Let's get into this cave and get back with our treasure!\n.\n.\n.\n.\nNow where do we go {name}?\nThis place has three ways ahead!!")
        opt3 = input("The three ways ahead are differentiated with the help of the light coming through them - | Red | Yellow | Blue |? ")

        if opt3=="Red" or opt3=="red" or opt3=="RED":
            print(f"Captain: Come here you incompetent cartographer, now get my crew out of this fire! \n[ GAME OVER! ]")
        elif opt3=="Blue" or opt3=="BLUE" or opt3=="blue":
            print(f"Crewmate: Captaiiinnn! Don not enter here! \nThese monsters will eat you up aliiiiive! \n[ GAME OVER! ]")
        elif opt3=="Yellow" or opt3=="yellow" or opt3=="YELLOW":
            print("Captain: Great job champion! I'll let you have a third of the quarter of this treasure for your commendable work!")
            print(r'''
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
            ''')
            print("Here's your prize for your work! \n[ WINNER! ]")
        else:
            print("\n[ GAME OVER! ]")
