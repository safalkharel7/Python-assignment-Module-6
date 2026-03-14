import random #for random operations
def dice(): #name given to the function that rolls the dice.
    dice_rolled = random.randint(1, 6) #random roll result
    return dice_rolled #returns the rolled number
rolled_value = dice() #first rolled number
if rolled_value == 6:
    print("\nYou rolled a 6 on first roll") #if 6 is achieved on first roll
else:
    print("\nYou rolled a " + str(rolled_value)+ " on first roll") #to show what was rolled.
    roll = 1 #counting roll to know exactly when 6 is achieved
    while rolled_value != 6:
        rolled_value = dice() #calling dice function to execute
        roll += 1 #adding to the number of rolls.
        print("You rolled a " + str(rolled_value) + ", on roll number " + str(roll))