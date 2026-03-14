import random #for random operations
def dice(sides): #name given to the function that rolls the dice.
    dice_rolled = random.randint(1, sides) #random roll result. sides is defined below.
    return dice_rolled #returns the rolled number
num_of_sides = int(input("Enter the number of sides on the dice: "))
rolled_value = dice(num_of_sides) #for the first roll value. 1st dice function executed.
if rolled_value == num_of_sides:
    print("\nYou rolled a " + str(rolled_value) + " on first attempt.")
else:
    print("\nYou rolled a " + str(rolled_value) + " on first attempt.")
    roll = 1
    while rolled_value != num_of_sides:
        rolled_value = dice(num_of_sides) #calling dice function to execute
        roll += 1 #counting the number of dice rolls.
        print(f"You rolled a {rolled_value} on roll number {roll}.")
print(f"\nIt took {roll} dice rolls to finally get a {rolled_value}.")