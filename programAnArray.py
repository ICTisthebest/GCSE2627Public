# CLASS TASK
# Ask the user for 5 ages and then print them

# Initialise variables (If you do not do this you lose marks in Higher)
age = []
getAge = ""

# Fixed loop to ask the user for a new age and add it to the list five times
for x in range(5):
    getAge = input("Please enter an age : ")
    age.append(getAge)

# Prints the final list with added ages from the user
print(age)