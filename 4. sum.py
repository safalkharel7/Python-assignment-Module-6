def sum(integers): #integers is set as a parameter to create function
    total = 0 #initialized total value to add the individual items to it.
    for i in integers: #i is an item in set integers
        total = total + i #each number is added to total one after the other
    return total
list = []   #empty list created
number = str(input("Enter a number: ")) #input asked from the user as string
while number != "":#as long as the input is not empty
    number = int(number) #str converted to int to add to the list for calc in function.
    list.append(number)  #the number will be added to the list
    number = str(input("Enter a number: ")) #then another input is requested as string.
total = sum(list)    #integers in sum function changed to list
print("\nThe sum of " + str(list) + " is equal to " + str(total))