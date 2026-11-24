# Question 20 
temperature = []

for x in range (7):
    temp = int(input("Enter a new tempertaure: "))
    temperature.append(temp)

highest = temperature[0]

for x in temperature: 
    if x > highest:
        highest = x

lowest = temperature[0]

for y in temperature:
    if y < lowest:
        lowest = y 

print(highest)
print(lowest)



