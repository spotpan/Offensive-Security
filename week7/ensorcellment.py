from pwn import *

p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1254)
p.recvuntil(":")
p.sendline("joe215")
mystr = p.recvall()
print(type(mystr))

while True:
    try:
        mystr = mystr.decode("base64")
        print("base64")
    except:
        print(mystr)
        mystr = mystr.decode("hex")
        print("hex")
    else:
        print(mystr)
        mystr = mystr.decode("bz2")
        print("bz2")
