from pwn import *

with open("mbxor.txt") as cipher:
    data = cipher.read()
    dict = {}
    for char in data:
        if ord(char) in dict:
            dict[ord(char)] += 1
        else:
            dict[ord(char)] = 1
    print(dict)
    print(max(dict, key=dict.get))

with open("sbxor.txt") as other:
    data = other.read()
    dict = {}
    for char in data:
        if ord(char) in dict:
            dict[ord(char)] += 1
        else:
            dict[ord(char)] = 1
    print(dict)
    print(max(dict, key=dict.get))
