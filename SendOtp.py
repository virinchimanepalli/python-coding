import random
import math

def generateOtp():
    digits="0123456789"
    OTP =""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def main():
    print(generateOtp()) 


if __name__=='__main__':
    main()
    