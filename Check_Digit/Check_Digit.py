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

def WithholdingNumb(wh_id_numb):
    weight1 = wh_id[0]+(wh_id[1]*2)+(wh_id[2]*3)+(wh_id[3]*4)+(wh_id[4]*5)
    weight2 = (wh_id[5]*6)+(wh_id[6]*7)+(wh_id[7]*8)+(wh_id[8]*9)+(wh_id[9]*10)+(wh_id[10]*11)
    weight3 = weight1 + weight2
    weight4 = weight3%9
    WHcheckdig = 9-weight4
    print(WHcheckdig)
    return WHcheckdig
    

def Withholding(wh_id):
        ALPHA = {
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
            "G": 16,
            "H": 17,
            "I": 18,
            "J": 19,
            "K": 20,
            "L": 21,
            "M": 22,
            "N": 23,
            "O": 24,
            "P": 25,
            "Q": 26,
            "R": 27,
            "S": 28,
            "T": 29,
            "U": 30,
            "V": 31,
            "W": 32,
            "X": 33,
            "Y": 34,
            "Z": 34,
            " ": 0
            }

        x = int(ALPHA.get(wh_id[0]))
        y = int(ALPHA.get(wh_id[1]))
        a = int(wh_id[2])
        b = int(wh_id[3])
        c = int(wh_id[4])
        d = int(wh_id[5])
        e = int(wh_id[6])
        f = int(wh_id[7])
        g = int(wh_id[8])
        result = x+(y*2)+(a*3)+(b*4)+(c*5)+(d*6)+(e*7)+(f*8)+(g*9)
        result2 = result%9
        wh_id = 9-result2
        print(wh_id)
        return wh_id

def suffix(suffix_id):
    numb1 = suffix_id[0]+(suffix_id[1]*2)+(suffix_id[2]*3)+(suffix_id[3]*4)
    numb2 = (suffix_id[4]*5)+(suffix_id[5]*6)+(suffix_id[6]*7)+(suffix_id[7]*8)+(suffix_id[8]*9)
    numb3 = numb1 + numb2
    numb4 = numb3%9
    Suffixdig = 9-numb4
    print(Suffixdig)
    return Suffixdig


while counter != 999999:
    number=input("Please enter your number: ")
    if len(number) == 7:
        quest = input("Is this a barcode id? y/n ")
        if quest == "y" or quest == "Y":
            x = list(number)
            sui_id = map(int, x)
            BarCode(sui_id)
        else:
            x = list(number)
            sui_id=map(int, x)
            CheckDigit(sui_id)

    elif len(number) == 9:
        if number[0].isalpha() == True:
            number=number.upper()
            wh_id=list(number)
            #wh_id = map(int, x)
            Withholding(wh_id)
            
        elif number[0].isalpha() == False:
            x = list(number)
            suffix_id = map(int, x)
            suffix(suffix_id)      

    elif len(number) == 11:
        x = list(number)
        wh_id = map(int,x)
        WithholdingNumb(wh_id) 
    
    Exit = raw_input("Do you have another ID? Y/N ")
    if Exit == "y" or Exit == "Y":
        counter = counter+1
    else:
        print("Goodbye.")
        sys.exit()

