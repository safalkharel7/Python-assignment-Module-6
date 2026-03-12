import random #for random operations
def dice(): #name given to the function that rolls the dice.
    dice_rolled = random.randint(1, 6) #random roll result
    return dice_rolled #returns the rolled number
rolled_value = 0
while rolled_value != 6:
    rolled_value = dice() #calling dice function to execute
    print("You rolled a ", rolled_value)