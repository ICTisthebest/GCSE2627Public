phoneNumber = input("Enter a phone number: ")
valid = False
validLen = False 
validNum = False
validStart = False

# How do we validate that it is correct
while validLen == False and validNum == False and validStart == False:

    # Check lenth is 11 characters 
    if len(phoneNumber) == 11:
        validLen = True

    else:
        validLen = False

    # Check the start of the phone number is digits 07
    if phoneNumber[0:2] == "07":
        validStart = True 

    else:
        validStart = False 

    # Checks if all the characters are numbers
    validNum = True

    for x in range(len(phoneNumber)):
        if phoneNumber[x] < "0" or phoneNumber[x] > "9":
            validNum = False 

    if validLen == True and validNum == True and validStart == True:
        print("Phone number is valid! ")
        print(phoneNumber)

    else:
        print("Invalid mobile number! ")
        phoneNumber = input("Enter a new phone number: ")









        



print(phoneNumber)