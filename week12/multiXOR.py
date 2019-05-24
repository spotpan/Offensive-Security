from pwn import *
from itertools import permutations
import sys


charset = "}qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_{"

with open("mbxor.txt") as handle:
    cipher = handle.read()
    cipher = cipher.decode("base64")
    print(len(cipher))
    print(cipher)
    myfile = open("hexmb.txt", "w")
    myfile.write(cipher)
    myfile.close()
    myfile = open("hexmb.txt", "r")
    text = myfile.read()
    print(text)


    #for char in cipher:
        #print(char)
    firstChar = cipher[0]
    for i in range(256):
        result = xor(firstChar, i)
        if result == "f":
            print(result, i)
    secondChar = cipher[1]
    for i in range(256):
        result = xor(secondChar, i)
        if result == "l":
            print(result, i)
    thirdChar = cipher[2]
    for i in range(256):
        result = xor(thirdChar, i)
        if result == "a":
            print(result, i)
    fourChar = cipher[3]
    for i in range(256):
        result = xor(fourChar, i)
        if result == "g":
            print(result, i)
    fifthChar = cipher[4]
    for i in range(256):
        result = xor(fifthChar, i)
        if result == "{":
            print(result, i)
    '''
    for i in range(len(cipher[5:])):
        curChar = cipher[i]
        for x in range(256):
            result = xor(curChar, x)
            if result in charset:
                print(result)
    '''
