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
print("You enter the barren land and walk for a while to reach crossroads.")
choice1 = input("You can go right or left.Type 'right' or 'left'.").lower()
if choice1 == "right":
    print("You turn right and enter a huge forest.After walking for"
          "almost 5 minutes you reach a lake. You can see a piece "
          "of land in the exact middle of the lake.")
    choice2 = input("You can either wait for a boat to come to help you"
                    " or you can yourself swim across. Type 'wait' or"
                    "'swim'.").lower()
    if choice2 == "wait":
        print("You wait for only a few minutes before a fisherman comes."
              "You ask him for a ride and he readily agrees. You finally reach "
              "the land but there are three doors right at the entrance."
              "You could not see them from across the lake. The doors are "
              "of three colours: Blue, Green and Red.")
        choice3 = input("Type blue,red or green to choose the respective"
                        " doors.").lower()
        if choice3 == "red":
            print("You opened the red door. As soon as you enter you find a "
                  "few humans. They seem like they belong to a tribe. Unfortunately"
                  "for you, they are cannibals. And you are their next meal. GAME OVER!!")
        elif choice3 == "blue":
            print("You enter the blue door and there is a beautiful ocean. The water "
                  "is really clear. In fact it is so clear that you can see something"
                  "swimming underwater. Unfortunately for you, it is not"
                  "a friendly creature. It is a 'Kraken' and it is very hungry. GAME OVER!!")
        elif choice3 == "green":
            print("You enter the green door and find yourself in a dessert."
                  "You walk for around 5 minutes and just as you were "
                  "beginning to loose hope you see something shiny in the sand."
                  "You hurry over and drop to your knees as you hurriedly dig"
                  "out what happens to be the treasure chest. CONGRATULATIONS YOU WON!!")
        else:
            print("You have made a selection which was not offered to you."
                  "In doing so you have angered the Gods. GAME OVER!!")
    elif choice2 == "swim":
        print("You confidently enter the water as you already know how to swim."
              "Unfortunately the lake is full of piranhas. And they are hungry for human flesh."
              "GAME OVER!!")
    else:
        print("You have made a selection which was not offered to you."
              "In doing so you have angered the Gods. GAME OVER!!")
elif choice1 == "left":
    print("You turn left and immediately enter a forest. Inside the forest you step on something"
          " and it makes a crunchy noise. You look down and to your horror,"
          "it is a bone. A human one to be exact. Just at that moment you hear a growl."
          "Unfortunately it is GAME OVER!!")
else:
    print("You have made a selection which was not offered to you."
          "In doing so you have angered the Gods. GAME OVER!!")
