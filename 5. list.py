def even_list(list): #function to only have even numbers from any given list.
    for l in list:  #l is the item in any given list.
        if l % 2 == 1: #if the remainer is 1 after dividing by 2. number is odd.
            list.remove(l) #remove item l from the list.
    return list #return the given list after changes.
mylist = []     #empty list
number = str(input("Enter a number: ")) #asking number from the user in saving as string.
while number != "":  #as long as the user doesn't input empty.
    mylist.append(int(number))  #the input added in the list.
    number = str(input("Enter a number: ")) #ask for the input again and save as string.
print(f"\nThe original list is: {mylist}") #if user returns empty value. list is printed.
even_list(mylist) #function called to remove uneven numbers from the list.
print(f"\nThe new list is: {even_list(mylist)}") #new list is printed.
