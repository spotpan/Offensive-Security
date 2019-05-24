from pwn import *
import sys

with open("sbxor.txt") as handle:
    cipher = handle.read()
    print(cipher)
    for i in range(256):
        result = xor(cipher, i)
        if "flag" in result:
            print(result)
            break
