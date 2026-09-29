# Task 1 
age = [3, 8, 14, 5, 11]
index = 0 
found = False 
target = int(input("Enter target number: "))

while index < len(age) and found == False:
    if age[index] == target:
        found = True 
        foundAt = index

    else: 
        index = index + 1 

print(index)