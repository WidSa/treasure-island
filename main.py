print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

choise1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'rigth' \n").lower()

if choise1 == "left":
     choise2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across or 'wait' to wait for a boat \n").lower()
     if choise2 == "wait":
          choise3 = input("You arrive at the island unharmed. There is a house with 3 doors. doors colors is red, yellow, and blue. whitch colour do you choose? \n").lower()
          if choise3 == "red":
               print("You enter a room of beasts. Game Over.")
          elif choise3 == "blue":
               print("You found the treasure! You Win!")
          elif choise3 == "yellow":
               print("You enter a room of beasts. Game Over.")
          else:
               print("You chose a door that doesn't exist. Game Over.")
     elif choise2 == "swim":
          print("You got attacked by an angry trout. Game over.")
     else :
          print("That not an option.")
elif choise1 == "right":
  print("You fell into a hole. Game Over.")
else :
     print("That not an option.")
