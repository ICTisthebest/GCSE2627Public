# # Example
# name = ["A", "B", "C", "D", "E", "F"]
# score = [34, 76, 12, 98, 47, 77]

# maxScore = score[0]
# maxScorePos = 0 

# for x in range(1, len(name)):
#     if score[x] > maxScore:
#         maxScore = score[x]
#         maxScorePos = x 

# print(maxScore)
# print(name[maxScorePos])

# # Maximum & Minimum Coding Tasks

# # Task 1

# # Initialise each variable 
# score = [48, 72, 65, 91, 54, 83]
# maxScore = score[0]

# # Fixed loop to check through every score
# for x in range(1, len(score)):
#     # Prints the current maximum score
#     print("The current max score is", (maxScore))

#     # Replaces the maximum score if the value after is higher
#     if score[x] > maxScore:
#         maxScore = score[x]
    
# # Prints the maximum score 
# print("Highest score:", maxScore)

# # Task 2 

# # Initialise variables
# temperature = [7, 3, -2, 5, 0, -6, 4]
# # We use the first index instead of 0 because some numbers are negative
# minTemp = temperature[0]

# # Fixed loop to check through every temperature
# for x in range(1, len(temperature)):
#     # Prints the current lowest temperature 
#     print("The current lowest temperature is", minTemp)

#     # Replaces the temperature if the value after is lower
#     if temperature[x] < minTemp:
#         minTemp = temperature[x]
    
# # Prints the lowest temperature
# print("Lowest temperature:", minTemp)

# # Task 3 

# # Initialise variables 
# score = [23, 8, 41, 16, 5, 37, 12]

# maxScore = score[0]
# minScore = score[0]

# # Fixed loop to check through every score 
# for x in range(1, len(score)):
#     # Prints the current maximum and minimum score
#     print("The current max score is", (maxScore))
#     print("The current min score is", (minScore))

#     # Replaces the maximum score if the value after is higher
#     if score[x] > maxScore:
#         maxScore = score[x]

#     # Replaces the minimum score if the value after is lower
#     if score[x] < minScore:
#         minScore = score[x]
    
# # Prints the highest and lowest scores 
# print("Highest score:", maxScore)
# print("Lowest score:", minScore)

# # Task 4 

# # Initialise variables 
# scores = [56, 71, 88, 63, 95, 79]

# maxScore = scores[0]
# index = 0 

# # Fixed loop to check through every score 
# for x in range(1, len(scores)):
#     # Prints the current maximum score
#     print("The current max score is", (maxScore), "found at index", index)

#     # Replaces the maximum score if the value after is higher
#     if scores[x] > maxScore:
#         maxScore = scores[x]
#         index = x
    
# # Prints the maximum score and the index it was found at 
# print("Maximum score:", maxScore)
# print("Found at index:", index)

# # Task 5 

# # Initialise variables 
# numbers = []
# askUser = ""

# # Askes the user to enter a number 8 times
# for x in range(8):
#     askUser = int(input("Enter a number: "))
#     # Adds the numbers to the array called "numbers"
#     numbers.append(askUser)

# # Prints the created array 
# print(numbers)

# # Initialise variables 
# maxNumber = numbers[0]
# minNumber = numbers[0]

# # Fixed loop to check through every number
# for x in range(1, len(numbers)):
#     # Prints the current maximum and minimum number 
#     print("The current max number is", (maxNumber))
#     print("The current min number is", (minNumber))
#     # Replaces the maximum number if the value after is higher
#     if numbers[x] > maxNumber:
#         maxNumber = numbers[x]

#     # Replaces the minimum number if the value after is lower
#     if numbers[x] < minNumber:
#                 minNumber = numbers[x]

# # Calculates the range 
# range = int((maxNumber - minNumber))  

# # Prints the highest number, lowest number and range
# print("Highest number:", maxNumber)
# print("Lowest number:", minNumber)
# print("Range:", range)

# Task 5 continued
# Initialise variables 
numbers = []
askUser = ""

# Askes the user to enter a number 8 times
for x in range(8):
    while askUser != 0:
          askUser = int(input("Enter a number: "))
          if askUser == 0:
               print("Value not accpeted.")
          else:
            # Adds the numbers to the array called "numbers"
               numbers.append(askUser)
    

# Prints the created array 
print(numbers)

# Initialise variables 
maxNumber = numbers[0]
minNumber = numbers[0]

# Fixed loop to check through every number
for x in range(1, len(numbers)):
    # Prints the current maximum and minimum number 
    print("The current max number is", (maxNumber))
    print("The current min number is", (minNumber))
    # Replaces the maximum number if the value after is higher
    if numbers[x] > maxNumber:
        maxNumber = numbers[x]

    # Replaces the minimum number if the value after is lower
    if numbers[x] < minNumber:
                minNumber = numbers[x]

# Calculates the range 
range = int((maxNumber - minNumber))  

# Prints the highest number, lowest number and range
if askUser != 0: 
      print("Highest number:", maxNumber)
      print("Lowest number:", minNumber)
      print("Range:", range)

# # Task X
# # Initialise variable
# names = ["Amir", "Beth", "Callum", "Dion", "Emma"]
# scores = [67, 81, 54, 72, 93]
# maxScore = scores[0]
# minScore = scores[0]
# indexMax = 0
# indexMin = 0 

# # Fixed loop to check through every score
# for x in range(1, len(scores)):
#     # Replaces the maximum score if the value after is higher
#     if scores[x] > maxScore:
#         maxScore = scores[x]
#         indexMax = x

#     # Replaces the minimum score if the value after is lower 
#     if scores[x] < minScore:
#         minScore = scores[x]
#         indexMin = x
    
# # Prints the highest score and the index and the lowest score with the index
# print("Highest:",names[indexMax], "with", maxScore)
# print("Lowest:",names[indexMin], "with", minScore)








