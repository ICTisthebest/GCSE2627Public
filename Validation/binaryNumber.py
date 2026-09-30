# Validate a binary number and convert to 10 base number 

binaryNumber = input("Please enter an 8 bit binary number: ")
valid = False
validLen = False 
validNum = False
validChar = False 

while validLen == False and validNum == False and validChar == False:
    if len(binaryNumber) == 8:
            validLen = True
            
    else:
        validLen = False

        
    validNum = True  

    for x in range(len(binaryNumber)):
            if binaryNumber[x] < "0" or binaryNumber[x] > "1":
                validNum = False 
                
            else:
                validNum = True


    for x in range(len(binaryNumber)):
         if binaryNumber[x] == "1" or binaryNumber[x] == "0":
              validChar = True 
         
         else:
              validChar = False
            
    if validLen == True and validNum == True and validChar == True:  
         print("Binary number is valid! ")

    else:
        print("Binary number is invalid!")
        binaryNumber = input("Please enter a new 8 bit binary number ")