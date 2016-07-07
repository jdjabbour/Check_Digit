import sys
import math



sui_id = raw_input("Enter your 7 digit SUI ID: ")
num1 = int(sui_id[0])
num2 = int(sui_id[1])
num3 = int(sui_id[2])
num4 = int(sui_id[3])
num5 = int(sui_id[4])
num6 = int(sui_id[5])
num7 = int(sui_id[6])


def Odd(num1,num3,num5,num7):
    num_odd = num1 + num3 + num5 + num7
    num_odd = num_odd * 2
    return num_odd

def Even(num2,num4,num6):
    num_even = num2 + num4 + num6
    return num_even

num_odd = Odd(num1,num3,num5,num7)
num_even = Even(num2,num4,num6)

numb_sum = num_odd + num_even
check_dig = numb_sum%10
print ("Your check digit is: "), check_dig
