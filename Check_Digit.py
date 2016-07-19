import sys
import math




counter = 0
def BarCode(sui_id):
    #adds up the numbers id odd place holders
    BCodd = sui_id[6]+sui_id[4]+sui_id[2]+sui_id[0]
    BCodd = BCodd*3
    #adds up the numbers in even place holderse
    BCeven = sui_id[1]+sui_id[3]+sui_id[5]
    BCsum = BCodd+BCeven
    #the modulo strips the sum down to the remainder
    BCmodulo = BCsum%10
    #subtracting the remainder from ten gets the difference
    #the difference is the actual check digit
    BCcheckdig = 10 - BCmodulo
    if BCcheckdig == 10:
        BCcheckdig = 0
    print ("Your check digit is: "), BCcheckdig
    return BCcheckdig

        
def CheckDigit(sui_id):
    UIodd = sui_id[0] + sui_id[2] + sui_id[4] + sui_id[6]
    UIodd = UIodd * 2
    UIeven = sui_id[1] + sui_id[3] + sui_id[5]
    UIsum = UIodd + UIeven
    UIcheckdig = UIsum%10
    print ("Your check digit is: "), UIcheckdig
    return UIcheckdig

while counter != 999999:
    print("Is this a check digit for a SUI ID or a WITHHOLDING ID?")
    Pick_ID = raw_input("Please type S for SUI or W for WITHHOLDING. ")
    if Pick_ID == "s" or Pick_ID == "S":
        Pick_Opt = raw_input("Are you using a Barcode? Y/N ")
        if Pick_Opt == "y" or Pick_Opt == "Y":
            #x stores the input as a list with the list() function
            x = list(raw_input("Enter your 7 digit SUI ID: "))
            #the map function then "maps" the list items from x
            #and converts them to integers
            sui_id = map(int, x)
            BarCode(sui_id)
            
        else:
            x = list(raw_input("Enter your 7 digit SUI ID: "))
            sui_ud=map(int, x)
            CheckDigit(sui_id)
    
    Exit = raw_input("Do you have another ID? Y/N ")
    if Exit == "y" or Exit == "Y":
        counter = counter+1
    else:
        print("Goodbye.")
        sys.exit()

