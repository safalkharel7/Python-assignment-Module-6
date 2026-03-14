import random #for random operations
def dice(sides): #name given to the function that rolls the dice.
    dice_rolled = random.randint(1, sides) #random roll result. sides is defined below.
    return dice_rolled #returns the rolled number
sides = int(input("Enter the number of sides on the dice: "))
rolled_value = 0 #to enter the loop
roll = 0 #to count how many dice rolls is takes.
while rolled_value != sides:
    rolled_value = dice(sides) #calling dice function to execute
    roll += 1 #counting the number of dice rolls.
    print(f"You rolled a {rolled_value}.")
print(f"\nIt took {roll} dice rolls to finally get a {rolled_value}.")