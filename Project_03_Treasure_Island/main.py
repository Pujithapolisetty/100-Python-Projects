print("Welcome to Treasure Island!")
print("Your mission is to find the Tressure....")
choice1 = input("You are at a crossroad.Chose your direction.(Left,Right):").strip().upper()
if choice1 == "LEFT":
    choice2 = input("Do you want to swim or wait for a boat?").strip().upper()   
    if choice2 == "WAIT":
       choice3 = input("Chose a door :(RED,BLUE,YELLOW)").strip().upper()
       if choice3 == "RED":
           print("Burned by fire!Game Over!!")
       elif choice3 == "BLUE":
           print("Fell into a Trap!Game Over!")
       elif choice3 == "YELLOW":
          print("You found the Treasure")
       else:
           print("Game Over!!")
    else:
        print("You are attacked by taud!Game Over!!")       
else:
    print("Game Over!!")