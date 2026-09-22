# # TASK 1  - Playlist editor

# # Initialise variable for song
# songs = [ 

# "Neon Skyline", 

# "Midnight Code", 

# "Pixel Dreams", 

# "Static Hearts", 

# "Northern Lights", 

# "Binary Sunset" 

# ] 

# print (songs[1]) # Prints Midnight Code 
# print(songs[3]) # Static Hearts
# print(songs[5]) # Binary Hearts

# # Replaces the second position of the array
# newSong = input("Please enter a new song: ")
# songs[1] = newSong
# print(songs[1])

# # Prints every song in the array
# print(songs)

# # Prints the songs and position number not including 0
# for x in range(len(songs)):
#     print((x + 1),".", songs[x])

# # Prints the number of songs 
# print("There are", len(songs), "songs")

# # TASK 2 - Weekly Step Tracker

# # Initialise variables
# days = [ 

# "Monday", 

# "Tuesday", 

# "Wednesday", 

# "Thursday", 

# "Friday", 

# "Saturday", 

# "Sunday" 

# ] 

# steps = [ 

# 6840, 

# 9125, 

# 7550, 

# 10420, 

# 8320, 

# 12110, 

# 5890 

# ] 

# # Initialise variable
# total = 0
# count = 0 
# count2 = 0
# count3 = 0 
# userNumber = int(input("Enter the number: "))

# # Prints each day and step count 
# # Calculates the total number of steps
# for x in range(len(days)):
#     print("On", days[x], "you got", steps[x])
#     total = total + steps[x]

#     if steps[x] <=7000:
#         count = count + 1

#     elif steps[x] >=8000:
#         count2 = count2 + 1

#     if steps[x] >= userNumber:
#         count3 = count3 + 1

# # Prints the total and average 
# print(total)
# average = (total / (len(steps)))
# print(average)

# # Prints number of days with less than 7000 steps, at least 8000 steps and user input
# print("Number of days with less than 7000 steps =", count )
# print("Number of days with at least 8000 steps =", count2)
# print("Number of days with less at least", userNumber, "steps =", count3)

# TASK 3 - Bus Route Frequency
routes = [ 

4, 7, 4, 9, 12, 

4, 7, 15, 4, 9, 

7, 4, 12, 7, 4, 

18, 7, 4, 9, 7 

] 

routeNumber = input("Enter your route number: ")
count = 0

for x in range(len(routes)):
    if routes[x] == routeNumber:
        count = count + 1 

print(count)
    

    









    



    