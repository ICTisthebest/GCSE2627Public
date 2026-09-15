# Arrays 

names = ["Liyana","Maggie", "Devansshi", "Alina", "Elizabeth", "Jesse", "Laya", "Saymeen", "Debbie", "Muskaan", "Vigdis", "Mr Rodger"]
print(names[6]) # Prints Laya
print(names[3]) # Prints Alina

# FIXED LOOPS 
# Prints all names in array
for x in range (len(names)):
    print(len(names[x]))

# Prints number of characters of each name in array
for x in range(len(names)):
    print(names[x])

# ADDING A NEW NAME TO THE LIST
# Asks user for a new name
newName = input("Please enter a new name: ")
# Adds new name into the list
names.append(newName)
# Prints the lost and new names 
print(names)

# CLASS TASK 
# Write a array that is called colours which asks the user for three colours and use a fixed loop to do this.

# Empty array to enter colours from the user
colours = []

# Initialise variable (If you do not do this you lose marks in Higher)
newColour = ""

# Fixed loop to ask the user for a new colour and add it to the list three times
for x in range(3):
    newColour = input("Please enter a colour: ")
    colours.append(newColour)

# Prints the final list with added colours from the user
print(colours)




